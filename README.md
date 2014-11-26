ckanext-metaconf
================

Extension for CKAN to configure metadata for datasets and resources.
The following depicts ideas for the implementation.

functionality
=======

You can specify two metadata vocabularies in the config file: 
- metadata for a package (which can contain multiple resources)

- metadata for a resource (which is a specific entity)

To specify your own metadata vocabulary you have to give a identifier 
(eg 'id', 'description', ...). You have to specify a type for your data.
You can specify an MODIFIER for it. Choose out of the following lists:

TYPE
[textline, textbox, radiobutton, tags, dropdown, url, numberline, date]

textline:    one line to type text into
textbox:     a box to type text into
radiobutton: radiobuttons for boolean input
tags:        multiple tags
dropdown:    a dropdown menu to choose from
url:         one line to input a URL
numerline:   one line to typ an integer into
date:        a field to input a date

NECESSITY
[empty, ignore_empty, ignore, ignore_missing, if_empty_save_as(identifier)]

empty:            field has to be empty
ignore:           data is ignored
ignore_empty:     data is ignored if it's empty
ignore_missing:   TODO nicht relevant für user
if_empty_save_as: if its empty use the value of (identifier)

MODIFIER
[remove_whitespace, clean_format]

remove_whitespace: strip whitespaces
clean_format     : format_.lower().split('/')[-1].replace('.', '')

The specification is given as a python dictionary. The CKAN standard
vocabularies for datasets und resources would look like this:

!!! TODO maybe better examples?, clean up, add TYPE's, 

resource_mvocab = {
     'id': [ignore_empty],
     'revision_id': [ignore_missing],
     'package_id': [ignore],
     'url': [not_empty, remove_whitespace],
     'description': [ignore_missing],
     'format': [ignore_missing, clean_format],
     'hash': [ignore_missing],
     'state': [ignore],
     'position': [ignore],
     'name': [ignore_missing],
     'resource_type': [ignore_missing],
     'url_type': [ignore_missing],
     'mimetype': [ignore_missing],
     'mimetype_inner': [ignore_missing],
     'webstore_url': [ignore_missing],
     'cache_url': [ignore_missing],
     'size': [ignore_missing],
     'created': [ignore_missing],
     'last_modified': [ignore_missing],
     'cache_last_updated': [ignore_missing],
     'webstore_last_updated': [ignore_missing],
     'tracking_summary': [ignore_missing],
     'datastore_active': [ignore],
     '__extras': [ignore_missing],
 }

 package_mvocab = {
     '__before': [ignore],
     'id': [empty],
     'revision_id': [ignore],
     'name': [not_empty, name_validator, package_name_validator],
     'title': [if_empty_same_as("name")],
     'author': [ignore_missing],
     'author_email': [ignore_missing],
     'maintainer': [ignore_missing],
     'maintainer_email': [ignore_missing],
     'license_id': [ignore_missing],
     'notes': [ignore_missing],
     'url': [ignore_missing],#, URL(add_http=False)],
     'version': [ignore_missing, package_version_validator],
     'state': [ignore_not_package_admin, ignore_missing],
     'type': [ignore_missing],
     'owner_org': [owner_org_validator],
     'log_message': [ignore_missing, no_http],
     'private': [ignore_missing, boolean_validator,
                 datasets_with_no_organization_cannot_be_private],
     '__extras': [ignore],
     '__junk': [empty],
     'resources': default_resource_schema(),
     'tags': default_tags_schema(),
     'tag_string': [ignore_missing, tag_string_convert],
     'extras': default_extras_schema(),
     'save': [ignore],
     'return_to': [ignore],
     'relationships_as_object': default_relationship_schema(),
     'relationships_as_subject': default_relationship_schema(),
     'groups': {
         'id': [ignore_missing],
         'name': [ignore_missing],
         'title': [ignore_missing],
         '__extras': [ignore],
}
