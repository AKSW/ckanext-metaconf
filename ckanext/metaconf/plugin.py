#!/usr/bin/env python
# -*- coding: utf-8 -*-

# daten tachen in der update geschichte nicht mehr auf ... (immer noch) TODO

# todo: anhand des typs die validatoren hinzufügen: url -> url_validator

# todo: Write documentation
# todo: Additional Info rausnehmen
# todo: make tags on/off

#further investigation: can we hack tag boxes, so we can use them for data input?
#further investigation: header have keys, but we dont store them, so we delete them
#further investigation: normal tags and custom tags not possible by now
#to_discuss: make additional information configurable
#further investigation: can we leave the update schema unchanged?
#further investigation: is there a unnamed mcblock element?

#code style: rename files to type, so we can append the type so show the file
#rdf kommt aus Wrote /usr/lib/ckan/default/src/ckan/ckan/templates_legacy/package/read.rdf

#! Aussicht: Keine Zuordnung zu Objekten möglich bzw. Schachteln von Schlüssel/Wert-Paaren
#! Aussicht: Mandatory nur wenn das nicht und das nicht und...
#! Aussicht: Diverse Validatoren wären toll
#! Aussicht: Dynamisches hinzufügen von Schlüssel/Wert-Paaren od sogar Objekten (z.B. zur Darstellung von 'Liste von String')
#! Aussicht: Collapse Funktion zur Übersichtlichkeit
#! Aussicht: i18n Lokalisierung
#! Aussicht: Mouse Over Beschreibungstext zur Erklärung der einzelnen Punkte


# sieben                                          = McBlock()
# sieben.type                                     = 'inputpart'
# sieben.key                                      = 'partialInput'
# sieben.rdf_type                                 = 'dc:todo'
# sieben.label                                    = 'Partielle Eingabe'
# sieben.validator                                = ['ignore_empty']
# sieben.opt_value['text']                        = '/das/steht/schon/da/'

# elf                                             = McBlock()
# elf.type                                        = 'h1'
# elf.rdf_type                                    = 'dc:todo'
# elf.validator                                   = ['ignore_empty']
# elf.key                                         = 'Große Überschrift (h1)'
# elf.label                                       = 'Große Überschrift (h1)'

# zwoelf                                          = McBlock()
# zwoelf.validator                                = ['ignore_empty']
# zwoelf.type                                     = 'hline'

# elfeins                                         = McBlock()
# elfeins.type                                    = 'h2'
# elfeins.validator                               = ['ignore_empty']
# elfeins.key                                     = 'Überschrift (h2)'
# elfeins.label                                   = 'Überschrift (h2)'


# elfzwei                                         = McBlock()
# elfzwei.type                                    = 'h3'
# elfzwei.validator                               = ['ignore_empty']
# elfzwei.key                                     = 'Unterüberschrift (h3)'
# elfzwei.label                                   = 'Unterüberschrift (h3)'


# dreiz                                           = McBlock()
# dreiz.type                                      = 'custom'
# dreiz.key                                       = 'custom_block'
# dreiz.validator                                 = ['ignore_empty']
# dreiz.opt_value['html']                         = "<p>We open at <time>10:00</time> every morning.</p>"


import ckan.plugins as plug
import ckan.plugins.toolkit as tk

from copy import deepcopy
# use Unicode
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from settings import *
from ckan.lib.navl.validators import (ignore_missing,
	                              keep_extras,
                                      not_empty,
                                      empty,
                                      ignore,
                                      if_empty_same_as,
                                      not_missing,
                                      ignore_empty
                                      )

from ckan.logic.validators import (package_id_not_changed,
                                   tag_length_validator,
                                   tag_name_validator,
                                   tag_string_convert,
                                   duplicate_extras_key,
                                   isodate,
                                   int_validator,
                                   name_validator,
                                   package_name_validator,
                                   natural_number_validator,
                                   owner_org_validator,
                                   is_positive_integer,
                                   boolean_validator,
	                           url_validator
	                           )

from formencode.validators import OneOf

convert_to_extras = tk.get_converter('convert_to_extras')
convert_from_extras = tk.get_converter('convert_from_extras')

def convert_to_extras(key, data, errors, context):
    extras = data.get(('extras',), [])
    if not extras:
        data[('extras',)] = extras
    # hier muss data[key] und der zugehörige rdf teil serialisiert werden
    extras.append({'key': key[-1], 'value': data[key]})

def convert_from_extras(key, data, errors, context):
                       
    def remove_from_extras(data, key):
        to_remove = []    
        for data_key, data_value in data.iteritems():
            if (data_key[0] == 'extras'
                and data_key[1] == key):
                to_remove.append(data_key)
        for item in to_remove:
            del data[item]

    for data_key, data_value in data.iteritems():
        if (data_key[0] == 'extras' and data_key[-1] == 'key' and data_value == key[-1]):
            # data_key[1] muss wohl der datensatz sein, hier deserialisieren
            data[key] = data[('extras', data_key[1], 'value')]
            break
    else:
        return
    remove_from_extras(data, data_key[1])

def metaconf_config():
    class Empty:
        pass
    
    config = Empty()
    config.show_state = show_state
    config.show_additional_info = show_additional_info
    return config


def metaconf_blocks(blocks):
    return blocks

def metaconf_creation_schema(default_schema, mc_blocks):

    # we expand the default schema to avoid complications
    mc_schema = deepcopy(default_schema)

    # add rdf type to extras
    mc_schema['extras']['rdf'] = not_missing

    # add converter specified in user configuration
    # add validator not_empty if element is mandatory else add user specified validators
    for item in mc_blocks:
        mc_schema[item.key] = []
        
        for conv in item.converter:
            mc_schema[item.key].append(tk.get_converter(conv))
            
        if item.mandatory == True:
            mc_schema[item.key].append(not_empty)
        else:
            mc_schema[item.key].append(ignore_empty)

        # All elements are stored in extras, so we add convert_to_extras
        mc_schema[item.key].append(convert_to_extras)

    return mc_schema

# not used at the moment, do we need this for sth?
def metaconf_update_schema(default_schema, mc_blocks):
    mc_schema = metaconf_creation_schema(default_schema, mc_blocks)

    # The main idea is to take our create schema and do what standard ckan ist doing:

    # Users can (optionally) supply the package id when updating a package, but
    # only to identify the package to be updated, they cannot change the id.
    mc_schema['id'] = [ignore_missing, package_id_not_changed]

    # Supplying the package name when updating a package is optional (you can
    # supply the id to identify the package instead).
    mc_schema['name'] = [ignore_missing, name_validator, package_name_validator, unicode]

    # Supplying the package title when updating a package is optional, if it's
    # not supplied the title will not be changed.
    mc_schema['title'] = [ignore_missing, unicode]
    mc_schema['owner_org'] = [ignore_missing, owner_org_validator, unicode]

    return mc_schema

class MetaconfPlugin(plug.SingletonPlugin, tk.DefaultDatasetForm):
    plug.implements(plug.IDatasetForm)
    plug.implements(plug.IConfigurer)
    plug.implements(plug.ITemplateHelpers)

       
    """ Usage of TemplateHelpers is requirung this method """
    def get_helpers(self):
        return { 'metaconf_creation_schema': metaconf_creation_schema(super(MetaconfPlugin, self).create_package_schema(), mc_blocks),
                 'metaconf_blocks': metaconf_blocks(mc_blocks),
                 'metaconf_config': metaconf_config()
        }

    def create_package_schema(self):
        return metaconf_creation_schema(super(MetaconfPlugin, self).create_package_schema(), mc_blocks)

    # not used
    def update_package_schema(self):
        return super(MetaconfPlugin, self).update_package_schema()

        #        return metaconf_update_schema(super(MetaconfPlugin, self).create_package_schema(), mc_blocks)

    # not used
    def show_package_schema(self):
        #TODO!
        return super(MetaconfPlugin, self).show_package_schema()

    
    """ Redefine if this plugin is a default fallback"""
    def is_fallback(self):
        # Return True to register this plugin as the default handler for
        # package types not handled by any other IDatasetForm plugin.
        return True

    """ Define package types this plugin should be used for
    Has to overwritten because of TODO"""
    def package_types(self):
        # This plugin doesn't handle any special package types, it just
        # registers itself as the default (above).
        return []

    def update_config(self, config):
        # Add this plugin's templates dir to CKAN's extra_template_paths, so
        # that CKAN will use this plugin's custom templates.
        tk.add_template_directory(config, 'templates')

