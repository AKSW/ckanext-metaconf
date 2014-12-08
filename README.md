        !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        !!! BEWARE! THIS IS NOT USABLE YET !!!
        !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

        !!! EVEN THIS README IS SOME SORT OF IN A MIND MAP STATE !!!

        ckanext-metaconf
        ================

        Extension for CKAN to configure metadata for datasets and resources. The
        following depicts ideas for the implementation.

        There are three possibilities when using CKAN Datasets. Where does this plugin
        work by now:
        ✓  Create it
        ✓- Show it
        !  Update it

        functionality
        =============

        You can specify your metadata vocabulary by the elements shown in the CKAN
        dataset creation workflow. At this time every element is specified as python
        McBlock object. Choose an random identifier (here it's 'fuenf') for your object
        and do sth like this:

        fuenf = McBlock()
        fuenf.type = 'markdown'
        fuenf.name = 'Markdown-Box'
        fuenf.label = 'Eine Markdownbox'
        fuenf.validator = ['ignore_missing']
        fuenf.opt_value['checked'] = 'false'
        fuenf.opt_value['text']   =  'Another text'

        For type you can choose from:
        TODO: extensive documentation ob the options for those choices + there are more than that

        ✓  input:       one line to type text into
        ✓  markdown:    a box to type markdown into
        ✓  textarea:    a box to type simple text into 
        ✓- checkbox:    radiobuttons for boolean input (TODO: can we label it?)
        ✓  inputpart:   only parts of the data saved are given by the user
        ✓  tags:        multiple tags
        ✓  select:      a dropdown menu to choose from
        !  url:         one line to input a URL
        !  numberline:  one line to typ an integer into
        -  date:        a field to input a date
        ✓  hidden:      add a hidden field
        !  organization:choose from those CKAN Organizations (at the moment this is activated by default when a organization exists)

        For validator you can choose from:
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

        Developer Documentation:
        =======================

        Jinja2 blocks for creation Step1-3:
        ===================================
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


        TODO
        ====

        1) dont forget to put the required message to elements that are required
        4) organization must be provided (really?) (looks like the deployer can specify it... but dont forget to put it in show_schema too)
        5) Plugins may change the parameters of this function depending on the value of
           the ``type`` parameter, see the ``IDatasetForm`` plugin interface.
        8) currently we arent altering those update and show schemata. Should we?
        9.5) data.extras does not exist initially, where do they create it? FUU extra magic?!!? evtl einfach mal ohne plugin angucken... -.-
        10) why did step 2 vanish? -> Can we move things to step 2
        12) generate schema from selected blocks: convert to extras in create | convert from extras in show... Maybe Flags for that?
        15) TODO: alter value and error to save our custom fields (they are saved, but why?; check that)
        16) write config parser
        19) generalize metaconf-url, at this moment it's shown under title -.-

        Nice to know
        ============
        !!! You have to create a organization to add datasets! (At least while using the standard schema... ;) 

        One can access the loop index in jinja with loop.index0 (0 indexed) http://jinja.pocoo.org/docs/dev/templates/#for

        Jinja range function: http://jinja.pocoo.org/docs/dev/templates/#list-of-global-functions

        form.hidden and so on are macros! So how can we pass things to macros? --> Using CKAN Snippets u can pass variables while calling

        CKAN defines Jinja2 Tags: ['ckan_extends', 'snippet', 'url_for_static', 'url_for', 'link_for', 'resource'] (first 2 are important to know)
