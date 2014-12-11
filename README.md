> BEWARE! THIS PLUGIN IS NOT USABLE YET !!!


# ckanext-metaconf
## Introduction

This is an extension for the CKAN data portal platform. It adds the possibility
to configure a metadata schema for datasets and resources. You can specify your
metadata vocabulary by defining elements that are shown in the CKAN dataset
creation workflow. This specification is done by the maintainer of the portal
not the user.

There are three main things that can be done when using CKAN Datasets:

- [x] create it
- [x] show it
- [ ] update it

Only marked items are fully implemented yet. 

**ckanext-metaconf is currently under development** and you should not use it.

## How can I specify my metadata-schema?

Before messing around with this plugin, take a look at how to work with 
[CKAN Plugins!] (http://docs.ckan.org/en/latest/extensions/tutorial.html#installing-the-extension)

Now that you know how to install a extension, you can configure the metadata
schema to fit your needs. In the main directory theres a 'metaconf-schema.py'
file. It is the only file you have to edit to fully specify your schema. As a
example there is the OpenGovernmentData-Metadata format implemented so you can
see what's possible and how to implement it. *TODO it's not at the point this is
written*

Every element (shown in the creation workflow) is thereby specified as a python
McBlock object. Choose a random name (here it's 'fuenf') for your object and
write something like the following:

     fuenf = McBlock()
     fuenf.type = 'markdown'
     fuenf.name = 'Markdown-Box'
     fuenf.label = 'Eine Markdownbox'
     fuenf.validator = ['ignore_missing']
     fuenf.opt_value['checked'] = 'false'
     fuenf.opt_value['text']   =  'Another text'

As type you can show from a list shown below. It tells the plugin how the data
has to be given by the user. Every McBlock Object has to be provided with the
attributes: type,name,label and validator. In most of the cases its necessary to
give one or more opt_values to make resonable use of the element.

Implemented | Type | Description
------|-------------|-----------------------------------------
- [x] | input:      |  one line to type text into
- [x] | markdown:   |  a box to type markdown into
- [x] | textarea:   |  a box to type simple text into
- [ ] | *checkbox:  |   *radiobuttons for boolean input*
- [x] | inputpart:  |  only parts of the data saved are given by the user
- [x] | tags:       |  multiple tags
- [x] | select:     |  a dropdown menu to choose from
- [ ] | *url:*      |    *one line to input a URL*
- [ ] | numberline: |  one line to typ an integer into
- [ ] | date:       |  a field to input a date
- [x] | hidden:     |  add a hidden field
- [x] | organization: | choose from those CKAN Organizations (at the moment this is activated by default when a organization exists)


- [ ] TODO: formatierung übrschriften, ...

For validator you can choose from:

*TODO this is not cool at the time: document more and better*

    [empty, ignore_empty, ignore, ignore_missing, if_empty_save_as(identifier)]
    
    empty:            field has to be empty
    ignore:           data is ignored
    ignore_empty:     data is ignored if it's empty
    ignore_missing:   TODO nicht relevant für user
    if_empty_save_as: if its empty use the value of (identifier)
    
    For converter you can choose from:
    [remove_whitespace, clean_format]
    
    remove_whitespace: strip whitespaces
    clean_format     : format_.lower().split('/')[-1].replace('.', '')
    ```

## Temporary things the developers found to be interesting at development time

    Step 1: package_basic_fields.html
              -> 

    Step 2: resource_form.html
              -> 'stages':                   Stages snippet (1,2,3 bar at the top)

              -> 'basic_fields':             File block (Upload or Link)
              -> 'basic_fields_name':        Name textfield
              -> 'basic_fields_description': Description Field
              -> 'basic_fields_format':      Format dropdown menu

              -> 'metadata_fields' (if include_metadata): ???

              -> Form buttons (previous, save&add another, next)

    Step 3: package_metadata_fields.html
              -> package_metadata_fields_url: Resource URL
              -> package_metadata_fields_version: Version
              -> package_metadata_author    : Author && Author-Email
              -> package_metadata_fields_maintainer: Maintainer && Maintainer-Email


## Nice to know

- !!! You have to create a organization to add datasets! (At least while using
  the standard schema... ;) No you have not!

- One can access the loop index in jinja with [loop.index0]
  (http://jinja.pocoo.org/docs/dev/templates/#for) ( it's 0 indexed)

- [Jinja range function] (http://jinja.pocoo.org/docs/dev/templates/#list-of-global-functions)

- form.hidden and so on are macros! So how can we pass things to macros? --> Using CKAN Snippets u can pass variables while calling

- CKAN defines Jinja2 Tags: ['ckan_extends', 'snippet', 'url_for_static', 'url_for', 'link_for', 'resource'] (first 2 are important to know)
