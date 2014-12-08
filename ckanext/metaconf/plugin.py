#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ckan.plugins as plug
import ckan.plugins.toolkit as tk
from metaconf import McBlock

# use Unicode
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# TODOOOO!
extra_fields    = False

eins = McBlock()
eins.type = 'hidden'
eins.name = 'HiddenInformation'
eins.validator = ['ignore_missing']

zwei = McBlock()
zwei.type = 'input'
zwei.name = 'InputText'
zwei.validator = ['ignore_missing']
zwei.opt_value = {'text': 'This is the text'}

drei = McBlock()
drei.type = 'checkbox'
drei.name = 'Checkbox-Selektiert'
drei.validator = ['ignore_missing']
drei.opt_value = {'checked': True}

vier = McBlock()
vier.type = 'checkbox'
vier.name = 'Checkbox-deselektiert'
vier.label = 'label?'
vier.validator = ['ignore_missing']
vier.opt_value = {'checked': False}

fuenf = McBlock()
fuenf.type = 'markdown'
fuenf.name = 'Markdown-Box'
fuenf.label = 'Eine Markdownbox'
fuenf.validator = ['ignore_missing']
fuenf.opt_value['checked'] = 'false'
fuenf.opt_value['text']   =  'Another text'

sechs = McBlock()
sechs.type = 'textarea'
sechs.name = 'mc-textarea'
sechs.label = 'Eine Textbox'
sechs.validator = ['ignore_missing']

sieben = McBlock()
sieben.type = 'inputpart'
sieben.name = 'mc-partiinput'
sieben.label = 'Partielle Eingabe'
sieben.validator = ['ignore_missing']
sieben.opt_value['text'] = '/das/steht/schon/da/'

acht = McBlock()
acht.type = 'tags'
acht.name = 'mc-tags'
acht.label = 'Eine Tagbox'
acht.validator = ['ignore_missing']
acht.opt_value['text'] = ['eine', 'liste', 'von', 'tags']

neun = McBlock()
neun.type = 'select'
neun.name = 'mc-dropdown'
neun.label = 'Ein Dropdown-Menue'
neun.validator = ['ignore_missing']
neun.opt_value['entries'] = [{'value': 'empty', 'text': 'Select a type...'}, {'value': 'strange'}, {'value': 'data'}, {'value': 'representation'}]
neun.opt_value['preselected'] = "empty"

zehn = McBlock()
zehn.type = 'url'
zehn.name = 'mc-url'
zehn.label = 'Eine URL Eingabe'
zehn.validator = ['ignore_missing']
zehn.opt_value['text'] = "Ein toller Text"

mc_blocks = [eins, zwei, drei, vier, fuenf, sechs, sieben, acht, neun, zehn]

def metaconf_blocks(blocks):
    return blocks

# TODO werden hidden jetzt gespeichert oder nich? eher nich wahrscheinlich

def metaconf_creation_schema(default_schema, mc_blocks):
    mc_schema = {}

    for item in mc_blocks:
        mc_schema[item.name] = []
        
        for conv in item.converter:
            mc_schema[item.name].append(tk.get_converter(conv))
        for valid in item.validator:
            mc_schema[item.name].append(tk.get_validator(valid))
        mc_schema[item.name].append(tk.get_converter('convert_to_extras'))

    #THIS is standard so it'll work
    mc_schema['name'] = default_schema['name']

    #TODO So is there a problem with this group thing?
#    mc_schema['groups'] = default_schema['groups']
    
    return mc_schema

# TODO this works somehow...
def metaconf_show_schema(default_schema, mc_blocks):
    schema = metaconf_creation_schema(default_schema, mc_blocks)

    # Don't strip ids from package dicts when validating them.
    schema['id'] = []

    schema.update({
        'tags': {'__extras': [ckan.lib.navl.validators.keep_extras]}})

    # Add several keys to the 'resources' subschema so they don't get stripped
    # from the resource dicts by validation.

    schema['resources'].update({
        'created': [ckan.lib.navl.validators.ignore_missing],
        'position': [not_empty],
        'last_modified': [ckan.lib.navl.validators.ignore_missing],
        'cache_last_updated': [ckan.lib.navl.validators.ignore_missing],
        'webstore_last_updated': [ckan.lib.navl.validators.ignore_missing],
        'revision_timestamp': [],
        'resource_group_id': [],
        'cache_last_updated': [],
        'webstore_last_updated': [],
        'size': [],
        'state': [],
        'last_modified': [],
        'mimetype': [],
        'cache_url': [],
        'name': [],
        'webstore_url': [],
        'mimetype_inner': [],
        'resource_type': [],
        'url_type': [],
    })

    schema.update({
        'state': [ckan.lib.navl.validators.ignore_missing],
        'isopen': [ignore_missing],
        'license_url': [ignore_missing],
        })

    schema['groups'].update({
        'description': [ignore_missing],
        'display_name': [ignore_missing],
        'image_display_url': [ignore_missing],
        })

    # Remove validators for several keys from the schema so validation doesn't
    # strip the keys from the package dicts if the values are 'missing' (i.e. # None).
    schema['author'] = []
    schema['author_email'] = []
    schema['maintainer'] = []
    schema['maintainer_email'] = []
    schema['license_id'] = []
    schema['notes'] = []
    schema['url'] = []
    schema['version'] = []

        # Add several keys that are missing from default_create_package_schema(), so
        # validation doesn't strip the keys from the package dicts.
    schema['metadata_created'] = []
    schema['metadata_modified'] = []
    schema['creator_user_id'] = []
    schema['num_resources'] = []
    schema['num_tags'] = []
    schema['organization'] = []
    schema['owner_org'] = []
    schema['private'] = []
    schema['revision_id'] = []
    schema['revision_timestamp'] = []
    schema['tracking_summary'] = []
    schema['license_title'] = []
    
    return mc_schema


class MetaconfPlugin(plug.SingletonPlugin, tk.DefaultDatasetForm):
    plug.implements(plug.IDatasetForm)
    plug.implements(plug.IConfigurer)
    plug.implements(plug.ITemplateHelpers)

        
    """ Usage of TemplateHelpers is requirung this method """

    def get_helpers(self):
        return { 'metaconf_creation_schema': metaconf_creation_schema(super(MetaconfPlugin, self).create_package_schema(),
                                                                      mc_blocks),
                 'metaconf_blocks': metaconf_blocks(mc_blocks),
        }


    def create_package_schema(self):
        return metaconf_creation_schema(super(MetaconfPlugin, self).create_package_schema(), mc_blocks)

    def update_package_schema(self):
        return super(MetaconfPlugin, self).update_package_schema()

    def show_package_schema(self):
        return metaconf_show_schema(super(MetaconfPlugin, self).show_package_schema(), mc_blocks)


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
