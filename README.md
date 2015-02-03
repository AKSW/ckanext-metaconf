# ckanext-metaconf
## Introduction

This is an extension for the CKAN data portal platform. It adds the possibility
to configure the metadata schema for datasets and resources. You can specify your
metadata vocabulary by defining elements that are shown in the CKAN dataset
creation workflow. This specification is done by the maintainer of the portal
not the user.

There are many things that can be done when using CKAN Datasets:

- [x] create it
- [x] show it
- [x] update it
- [x] export metadata as rdf

These are modified by this plugin to reflect your changes to the metadata schema.

## How can I specify my metadata-schema?

Before messing around with this plugin, take a look at how to work with 
[CKAN Plugins!] (http://docs.ckan.org/en/latest/extensions/tutorial.html#installing-the-extension)

Now that you know how to install a extension, you can configure the metadata
schema to fit your needs. In the main directory theres a settings.py'
file. It is the only file you have to edit to fully specify your schema. As a
example there is the OpenGovernmentData-Metadata format implemented so you can
see what's possible and how to implement it. 

Every element (shown in the creation workflow) is thereby specified as a python
McBlock object. Choose a random name (here it's 'fuenf') for your object and
write something like the following:

    ogd_groups                                        = McBlock()
    ogd_groups.type                                   = 'select'
    ogd_groups.key                                    = 'ogd_groups'
    ogd_groups.rdf_type                               = 'rdf:todo'
    ogd_groups.label                                  = 'Kategorien'
    ogd_groups.mandatory                              = True
    ogd_groups.opt_value['preselected']               = "empty"
    ogd_groups.opt_value['entries']                   = [
        {'value': '',                                'text': 'Wählen Sie eine Lizenz...'},
        {'value': 'dl-de-by-1.0',                    'text': 'Datenlizenz Deutschland Namensnennung'},
    ]

As type you can show from a list shown below. It tells the plugin how the data
has to be given by the user. Every McBlock Object has to be provided with the
attributes: type,name,label and validator. In most of the cases its necessary to
give one or more opt_values to make resonable use of the element.

Implemented | Type | Description
---|---------------|--------------------------------------
✓ | input:        | one line to type text into
✓ | markdown:     | a box to type markdown into
✓ | textarea:     | a box to type simple text into
✓ | checkbox:     | radiobuttons for boolean input
✓ | inputpart:    | only parts of the data saved are given by the user
✓ | tags:         | multiple tags
✓ | select:       | a dropdown menu to choose from
✓ | url:          | one line to input a URL
✓ | hidden:       | add a hidden field
✓ | organization: | choose from those CKAN Organizations (at the moment this is activated by default when a organization exists)
✓ | custom        | your custom HTML to nicen up the form
✓ | h1,h2,h3      | headings in different sizes
✓ | hline         | a horizontal line (simple html)

## Nice to know

- !!! You have to create a organization to add datasets! (At least while using
  the standard schema... ;) No you have not!

- One can access the loop index in jinja with [loop.index0]
  (http://jinja.pocoo.org/docs/dev/templates/#for) ( it's 0 indexed)

- [Jinja range function] (http://jinja.pocoo.org/docs/dev/templates/#list-of-global-functions)

- form.hidden and so on are macros! So how can we pass things to macros? --> Using CKAN Snippets u can pass variables while calling

- CKAN defines Jinja2 Tags: ['ckan_extends', 'snippet', 'url_for_static', 'url_for', 'link_for', 'resource'] (first 2 are important to know)
