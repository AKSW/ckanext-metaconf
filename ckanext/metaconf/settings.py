#!/usr/bin/env python
# -*- coding: utf-8 -*-
# use Unicode
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# TODO validator überprüfen und nacharbeiten

from metaconf import McBlock

show_state                                        = False
show_additional_info                              = False

author                                            = McBlock()
author.type                                       = 'input'
author.key                                        = 'author'
author.label                                      = 'Ver-öffentlichende Stelle'
author.rdf_type                                   = 'rdf:todo'
author.mandatory                                  = True

author_email                                      = McBlock()
author_email.type                                 = 'input'
author_email.key                                  = 'author_email'
author_email.rdf_type                             = 'rdf:todo'
author_email.label                                = 'Ver-öffentlichende Stelle Email'


maintainer                                        = McBlock()
maintainer.type                                   = 'input'
maintainer.key                                    = 'maintainer'
maintainer.rdf_type                               = 'rdf:todo'
maintainer.label                                  = 'Daten-verantwortliche Stelle'


maintainer_email                                  = McBlock()
maintainer_email.type                             = 'input'
maintainer_email.key                              = 'maintainer_email'
maintainer_email.rdf_type                         = 'rdf:todo'
maintainer_email.label                            = 'Daten-verantwortliche Stelle Email'


notes                                             = McBlock()
notes.type                                        = 'textarea'
notes.key                                         = 'notes'
notes.rdf_type                                    = 'rdf:todo'
notes.label                                       = 'Beschreibung'
notes.mandatory                                   = True

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
    {'value': 'bevoelkerung',                    'text': 'Bevölkerung'},
    {'value': 'bildung_wissenschaft',            'text': 'Bildung und Wissenschaft'},
    {'value': 'geo',                             'text': 'Geographie, Geologie und Geobasisdaten'},
    {'value': 'gesetze_justiz',                  'text': 'Gesetze und Justiz'},
    {'value': 'gesundheit',                      'text': 'Gesundheit'},
    {'value': 'infrastruktur_bauen_wohnen',      'text': 'Infrastruktur, Bauen und Wohnen'},
    {'value': 'kultur_freizeit_sport_tourismus', 'text': 'Kultur, Freizeit, Sport und Tourismus'},
    {'value': 'politik_wahlen',                  'text': 'Politik und Wahlen'},
    {'value': 'soziales',                        'text': 'Soziales'},
    {'value': 'transport_verkehr',               'text': 'Transport und Verkehr'},
    {'value': 'umwelt_klima',                    'text': 'Umwelt und Klima'},
    {'value': 'verbraucher',                     'text': 'Verbraucherschutz'},
    {'value': 'verwaltung',                      'text': 'Öffentliche Verwaltung, Haushalt und Steuern'},
    {'value': 'wirtschaft_arbeit',               'text': 'Wirtschaft und Arbeit'},
]

tag_string                                        = McBlock()
tag_string.type                                   = 'tags'
tag_string.key                                    = 'tag_string'
tag_string.rdf_type                               = 'rdf:todo'
tag_string.label                                  = 'Schlagwörter'


url                                               = McBlock()
url.type                                          = 'url'
url.key                                           = 'url'
url.rdf_type                                      = 'rdf:todo'
url.label                                         = 'Webseite'

url.opt_value['prefix']                           = "http://"


type                                              = McBlock()
type.type                                         = 'input'
type.key                                          = 'type'
type.rdf_type                                     = 'rdf:todo'
type.mandatory                                    = True
type.label                                        = 'Typ'


language                                          = McBlock()
language.type                                     = 'input'
language.key                                      = 'language'
language.rdf_type                                 = 'rdf:todo'
language.label                                    = 'Sprache'


hash                                              = McBlock()
hash.type                                         = 'input'
hash.key                                          = 'hash'
hash.rdf_type                                     = 'rdf:todo'
hash.label                                        = 'Prüfsumme'


license_id                                        = McBlock()
license_id.type                                   = 'select'
license_id.key                                    = 'license_id'
license_id.rdf_type                               = 'rdf:todo'
license_id.label                                  = 'Lizenz-ID'
license_id.mandatory                              = True
license_id.opt_value['preselected']               = "empty"
license_id.opt_value['entries']                   = [
    {'value': '',                                'text': 'Wählen Sie eine Lizenz...'},
    {'value': 'dl-de-by-1.0',                    'text': 'Datenlizenz Deutschland Namensnennung'},
    {'value': 'dl-de-by-2.0',                    'text': 'Datenlizenz Deutschland Namensnennung 2.0'},
    {'value': 'official-work',                   'text': 'Amtliches Werk, lizenzfrei nach §5 Abs. 1 UrhG'},
    {'value': 'geonutzv-de-2013-03-19',          'text': 'Nutzungsbestimmungen für die Bereitstellung von Geodaten des Bundes'},
    {'value': 'cc-by',                           'text': 'Creative Commons Namensnennung (CC-BY)'},
    {'value': 'cc-by-4.0',                       'text': 'Creative Commons Namensnennung (CC-BY 4.0)'},
    {'value': 'cc-zero',                         'text': 'Creative Commons Zero'},
    {'value': 'cc-by-sa',                        'text': 'Creative Commons Attribution Weitergabe unter gleichen Bedingungen (CC-BY-SA)'},
    {'value': 'cc-by-sa-4.0',                    'text': 'Creative Commons Attribution Weitergabe unter gleichen Bedingungen (CC BY-SA 4.0)'},
    {'value': 'odc-odbl',                        'text': 'Open Data Commons Open Database License (ODbL)'},
    {'value': 'odc-by',                          'text': 'Open Data Commons Namensnennung'},
    {'value': 'odc-pddl',                        'text': 'Open Data Commons Public Domain Dedication and Licence (PDDL)'},
    {'value': 'other-open',                      'text': 'Andere freie Lizenz'},
    {'value': 'cc-nc',                           'text': 'Creative Commons Nicht-Kommerziell (CC-NC)'},
    {'value': 'cc-by-nc-4.0',                    'text': 'Creative Commons Nicht-Kommerziell (CC BY-NC 4.0)'},
    {'value': 'cc-by-nd',                        'text': 'Creative Commons Keine Bearbeitung (CC-BY-ND)'},
    {'value': 'cc-by-nd-4.0',                    'text': 'Creative Commons Keine Bearbeitung (CC BY-ND)'},
    {'value': 'dl-de-by-nc-1.0',                 'text': 'Datenlizenz Deutschland Namensnennung nicht-kommerziell'},
    {'value': 'dl-de-zero-2.0',                  'text': 'Datenlizenz Deutschland – Zero – Version 2.0'},
    {'value': 'geolizenz-v1.2.1-open',           'text': 'GeoLizenz V1.2.1 Open-räumlich und zeitlich unbeschränkte Einräumung aller Nutzungsrechte'},
    {'value': 'geolizenz-v1.2-1a',               'text': 'GeoLizenz V1-2 Ia-kommerziell-Weiterverarbeitung-oeffentliche_Netzwerke'},
    {'value': 'geolizenz-v1.2-1b',               'text': 'GeoLizenz V1-2 Ib-nicht-kommerziell-Weiterverarbeitung-oeffentliche_Netzwerke'},
    {'value': 'geolizenz-v1.2-2a',               'text': 'GeoLizenz V1-2 IIa-kommerziell-keine Weiterverarbeitung-oeffentliche_Netzwerke'},
    {'value': 'geolizenz-v1.2-2b',               'text': 'GeoLizenz V1-2 IIb-nicht-kommerziell-keine Weiterverarbeitung-oeffentliche_Netzwerke'},
    {'value': 'geolizenz-v1.2-3a',               'text': 'GeoLizenz V1-2 IIIa-kommerziell-Weiterverarbeitung-nicht-oeffentliche_Netzwerke'},
    {'value': 'geolizenz-v1.2-3b',               'text': 'GeoLizenz V1-2 IIIb-nicht-kommerziell-Weiterverarbeitung-nicht-oeffentliche_Netzwerke'},
    {'value': 'geolizenz-v1.2-4a',               'text': 'GeoLizenz V1-2 IVa-kommerziell-keine Weiterverarbeitung-nicht-oeffentliche_Netzwerke'},
    {'value': 'geolizenz-v1.2-4b',               'text': 'GeoLizenz V1-2 IVb-nicht-kommerziell-keine Weiterverarbeitung-nicht-oeffentliche_Netzwerke'},
    {'value': 'apache',                          'text': 'Apache Lizenz'},
    {'value': 'app_commercial',                  'text': 'Andere kommerzielle Lizenz'},
    {'value': 'app_freeware',                    'text': 'Andere kostenfreie Lizenz'},
    {'value': 'app_opensource',                  'text': 'Andere Open Source Lizenz'},
    {'value': 'bsd-license',                     'text': 'BSD Lizenz'},
    {'value': 'gfdl',                            'text': 'GNU Free Documentation License'},
    {'value': 'gpl-3.0',                         'text': 'GNU General Public License version 3.0 (GPLv3)'},
    {'value': 'mozilla',                         'text': 'Mozilla Public License 1.0 (MPL)'},
    {'value': 'other-closed',                    'text': 'Andere eingeschränkte Lizenz'}]

trenner                                           = McBlock()

trenner.type                                      = 'custom'
trenner.opt_value["html"]                         = '<br><br><hr>'

contact_header                                    = McBlock()
contact_header.type                               = 'h2'

contact_header.key                                = 'Kontaktinformationen'
contact_header.label                              = 'Kontaktinformationen'

role                                              = McBlock()
role.type                                         = 'input'
role.key                                          = 'role'
role.rdf_type                                     = 'rdf:todo'
role.label                                        = 'Rolle'


person_name                                       = McBlock()
person_name.type                                  = 'input'
person_name.key                                   = 'person_name'
person_name.rdf_type                              = 'rdf:todo'
person_name.label                                 = 'Name'
person_name.mandatory                             = True

contact_url                                       = McBlock()
contact_url.type                                  = 'url'
contact_url.key                                   = 'contact_url'
contact_url.rdf_type                              = 'rdf:todo'
contact_url.label                                 = 'Webseite'

contact_url.opt_value['prefix']                   = "http://"

contact_mail                                      = McBlock()
contact_mail.type                                 = 'input'
contact_mail.key                                  = 'contact_mail'
contact_mail.rdf_type                             = 'rdf:todo'
contact_mail.label                                = 'Email'

contact_address                                   = McBlock()
contact_address.type                              = 'input'
contact_address.key                               = 'contact_address'
contact_address.rdf_type                          = 'rdf:todo'
contact_address.label                             = 'Adresse'

calendar_header                                   = McBlock()
calendar_header.type                              = 'h2'

calendar_header.key                               = 'Kalender-Daten'
calendar_header.label                             = 'Kalender-Daten'

calendar_created                                  = McBlock()
calendar_created.type                             = 'input'
calendar_created.key                              = 'calendar_created'
calendar_created.rdf_type                         = 'rdf:todo'
calendar_created.label                            = 'Erstellungs-datum'
calendar_created.mandatory                        = True

calendar_published                                = McBlock()
calendar_published.type                           = 'input'
calendar_published.key                            = 'calendar_published'
calendar_published.rdf_type                       = 'rdf:todo'
calendar_published.label                          = 'Veröffentlichungs-datum'

calendar_updated                                  = McBlock()
calendar_updated.type                             = 'input'
calendar_updated.key                              = 'calendar_updated'
calendar_updated.rdf_type                         = 'rdf:todo'
calendar_updated.label                            = 'Aktualisierungs-datum'

terms_of_use_header                               = McBlock()
terms_of_use_header.type                          = 'h2'

terms_of_use_header.key                           = 'Nutzungsbedingungen'
terms_of_use_header.label                         = 'Nutzungsbedingungen'

free_text                                         = McBlock()
free_text.type                                    = 'markdown'
free_text.key                                     = 'other'
free_text.rdf_type                                = 'rdf:todo'
free_text.label                                   = 'Freitext'


license_url                                       = McBlock()
license_url.type                                  = 'input'
license_url.key                                   = 'license_url'
license_url.rdf_type                              = 'rdf:todo'
license_url.label                                 = 'URL'


attribution_text                                  = McBlock()
attribution_text.type                             = 'markdown'
attribution_text.key                              = 'attribution_text'
attribution_text.rdf_type                         = 'rdf:todo'
attribution_text.label                            = 'Namensnennungs-Text'


is_free_to_use                                    = McBlock()
is_free_to_use.type                               = 'checkbox'
is_free_to_use.key                                = 'is_free_to_use'
is_free_to_use.rdf_type                           = 'rdf:todo'
is_free_to_use.label                              = 'Nutzungsfreiheit'

is_free_to_use.opt_value['checked']               = True
is_free_to_use.opt_value['helptext']              = ''

subgroups                                         = McBlock()
subgroups.type                                    = 'select'
subgroups.key                                     = 'subgroups'
subgroups.rdf_type                                = 'rdf:todo'
subgroups.label                                   = 'Unterkategorien'

subgroups.opt_value['preselected']                = "empty"
subgroups.opt_value['entries']                    = [
    {'value': '',                                'text': 'Wählen Sie eine Unterkategorie...'},
    {'value': 'wirtschaft',                      'text': 'Wirtschaft'},
    {'value': 'transport',                       'text': 'Transport und Verkehr'},
    {'value': 'umwelt',                          'text': 'Umwelt und Klima'},
    {'value': 'verentsorgung',                   'text': 'Ver- und Entsorgung'},
    {'value': 'geo',                             'text': 'Geographie und Stadtplanung'},
    {'value': 'gesundheit',                      'text': 'Gesundheit '},
    {'value': 'verbraucher',                     'text': 'Verbraucherschutz '},
    {'value': 'sicherheit',                      'text': 'Öffentliche Sicherheit'},
    {'value': 'wohnen',                          'text': 'Wohnen und Immobilien'},
    {'value': 'bildung',                         'text': 'Bildung'},
    {'value': 'verwaltung',                      'text': 'Öffentliche Verwaltung}, Haushalt und Steuern'},
    {'value': 'justiz',                          'text': 'Gesetze und Justiz'},
    {'value': 'demographie',                     'text': 'Demographie'},
    {'value': 'arbeit',                          'text': 'Arbeitsmarkt'},
    {'value': 'wahl',                            'text': 'Wahlen'},
    {'value': 'sozial',                          'text': 'Sozialleistungen'},
    {'value': 'kultur',                          'text': 'Kunst und Kultur'},
    {'value': 'erholung',                        'text': 'Sport und Erholung'},
    {'value': 'tourismus',                       'text': 'Tourismus'},
    {'value': 'sonstiges',                       'text': 'Sonstiges'}
]

metadata_original_portal                          = McBlock()
metadata_original_portal.type                     = 'input'
metadata_original_portal.key                      = 'metadata_original_portal'
metadata_original_portal.rdf_type                 = 'rdf:todo'
metadata_original_portal.label                    = 'Original-Metadaten-Portal'


metadata_original_id                              = McBlock()
metadata_original_id.type                         = 'input'
metadata_original_id.key                          = 'metadata_original_id'
metadata_original_id.rdf_type                     = 'rdf:todo'
metadata_original_id.label                        = 'Original-Metadaten-Schlüssel'


metadata_original_xml                             = McBlock()
metadata_original_xml.type                        = 'input'
metadata_original_xml.key                         = 'metadata_original_xml'
metadata_original_xml.rdf_type                    = 'rdf:todo'
metadata_original_xml.label                       = 'Original-Metadaten-XML'


metadata_original_html                            = McBlock()
metadata_original_html.type                       = 'input'
metadata_original_html.key                        = 'metadata_original_html'
metadata_original_html.rdf_type                   = 'rdf:todo'
metadata_original_html.label                      = 'Original-Metadaten-HTML'


metadata_transformer                              = McBlock()
metadata_transformer.type                         = 'select'
metadata_transformer.key                          = 'metadata_transformer'
metadata_transformer.rdf_type                     = 'rdf:todo'
metadata_transformer.label                        = 'Metadaten-Transformator'

metadata_transformer.opt_value['preselected']     = 'empty'
metadata_transformer.opt_value['entries']         = [
    {'value': '',                                'text': 'Wählen Sie...'},
    {'value': 'author',                          'text': 'author'},
    {'value': 'harvester',                       'text': 'harvester'}
]

spatial_header                                    = McBlock()
spatial_header.type                               = 'h2'

spatial_header.key                                = 'Geoinformationen'
spatial_header.label                              = 'Geoinformationen'

spatial_type                                      = McBlock()
spatial_type.type                                 = 'select'
spatial_type.key                                  = 'spatial_type'
spatial_type.rdf_type                             = 'rdf:todo'
spatial_type.label                                = 'Art der Form'

spatial_type.opt_value['preselected']             = 'polygon'
spatial_type.opt_value['entries']                 = [
    {'value': 'polygon',                         'text': 'polygon'}
]

spatial_coordinates                               = McBlock()
spatial_coordinates.type                          = 'textarea'

spatial_coordinates.rdf_type                      = 'rdf:todo'
spatial_coordinates.key                           = 'spatial_coordinates'
spatial_coordinates.label                         = 'LinearRing Koordinaten-Liste'

spatial_ags                                       = McBlock()
spatial_ags.type                                  = 'input'
spatial_ags.key                                   = 'spatial_ags'
spatial_ags.rdf_type                              = 'rdf:todo'
spatial_ags.label                                 = 'Geographische Abdeckung durch den Amtlichen Gemeindeschlüssel (AGS)'


spatial_nuts                                      = McBlock()
spatial_nuts.type                                 = 'input'
spatial_nuts.key                                  = 'spatial_nuts'
spatial_nuts.rdf_type                             = 'rdf:todo'
spatial_nuts.label                                = 'Geographische Abdeckung durch NUTS-Code'


spatial_nuts                                      = McBlock()
spatial_nuts.type                                 = 'input'
spatial_nuts.key                                  = 'spatial_nuts'
spatial_nuts.rdf_type                             = 'rdf:todo'
spatial_nuts.label                                = 'Geographische Abdeckung durch NUTS-Code'


spatial_uri                                       = McBlock()
spatial_uri.type                                  = 'input'
spatial_uri.key                                   = 'spatial_uri'
spatial_uri.rdf_type                              = 'rdf:todo'
spatial_uri.label                                 = 'URI zur geographischen Abdeckung'


spatial_text                                      = McBlock()
spatial_text.type                                 = 'input'
spatial_text.key                                  = 'spatial_text'
spatial_text.rdf_type                             = 'rdf:todo'
spatial_text.label                                = 'Abdeckung als Freitext'


geographical_granularity                          = McBlock()
geographical_granularity.type                     = 'select'
geographical_granularity.key                      = 'geographical_granularity'
geographical_granularity.rdf_type                 = 'rdf:todo'
geographical_granularity.label                    = 'Räumliche Auflösung'

geographical_granularity.opt_value['preselected'] = "empty"
geographical_granularity.opt_value['entries']     = [
    {'value': '',                                'text': 'Wählen Sie...'},
    {'value': 'bund',                            'text': 'bund'},
    {'value': 'land',                            'text': 'land'},
    {'value': 'kommune',                         'text': 'kommune'},
    {'value': 'stadt',                           'text': 'stadt'},
]

date_header                                       = McBlock()
date_header.type                                  = 'h2'

date_header.key                                   = 'Zeit- und Datumsinformationen'
date_header.label                                 = 'Zeit- und Datumsinformationen'

temporal_coverage_from                            = McBlock()
temporal_coverage_from.type                       = 'input'
temporal_coverage_from.key                        = 'temporal_coverage_from'
temporal_coverage_from.rdf_type                   = 'rdf:todo'
temporal_coverage_from.label                      = 'Start-Datum'


temporal_coverage_to                              = McBlock()
temporal_coverage_to.type                         = 'input'
temporal_coverage_to.key                          = 'temporal_coverage_to'
temporal_coverage_to.rdf_type                     = 'rdf:todo'
temporal_coverage_to.label                        = 'End-Datum'


temporal_granularity                              = McBlock()
temporal_granularity.type                         = 'select'
temporal_granularity.key                          = 'temporal_granularity'
temporal_granularity.rdf_type                     = 'rdf:todo'
temporal_granularity.label                        = 'Räumliche Auflösung'

temporal_granularity.opt_value['preselected']     = 'empty'
temporal_granularity.opt_value['entries']         = [
    {'value': '',                                'text': 'Wählen Sie...'},
    {'value': 'sekunde',                         'text': 'sekunde'},
    {'value': 'minute',                          'text': 'minute'},
    {'value': 'stunde',                          'text': 'stunde'},
    {'value': 'tag',                             'text': 'tag'},
    {'value': 'woche',                           'text': 'woche'},
    {'value': 'monat',                           'text': 'monat'},
    {'value': 'quartal',                         'text': 'quartal'},
    {'value': 'jahr',                            'text': 'jahr'},
    {'value': '5-jahre',                         'text': '5-jahre'},
]

temporal_granularity_factor                       = McBlock()
temporal_granularity_factor.type                  = 'input'
temporal_granularity_factor.key                   = 'temporal_granularity_factor'
temporal_granularity_factor.rdf_type              = 'rdf:todo'
temporal_granularity_factor.label                 = 'Faktor für zeitliche Auflösung'


various_header                                    = McBlock()
various_header.type                               = 'h2'

various_header.key                                = 'Verschiedene Informationen'
various_header.label                              = 'Verschiedene Informationen'

used_datasets                                     = McBlock()
used_datasets.type                                = 'textarea'

used_datasets.rdf_type                            = 'rdf:todo'
used_datasets.key                                 = 'used_datasets'
used_datasets.label                               = 'Verwendete Datensätze'

sector                                            = McBlock()
sector.type                                       = 'select'
sector.key                                        = 'sector'
sector.rdf_type                                   = 'rdf:todo'
sector.label                                      = 'Sektor'

sector.opt_value['preselected']                   = ''
sector.opt_value['entries']                       = [
    {'value': '',                                'text': 'Wählen Sie...'},
    {'value': 'oeffentlich',                     'text': 'oeffentlich'},
    {'value': 'privat',                          'text': 'private'},
    {'value': 'andere',                          'text': 'andere'},
]

images                                            = McBlock()
images.type                                       = 'textarea'

images.rdf_type                                   = 'rdf:todo'
images.key                                        = 'images'
images.label                                      = 'Bilder'

ogd_version                                       = McBlock()
ogd_version.type                                  = 'hidden'
ogd_version.rdf_type                              = 'rdf:todo'
ogd_version.key                                   = 'ogd_version'
ogd_version.opt_value['text']                     = 'v1.1'

mc_blocks                                         = [
    author,
    author_email,
    maintainer,
    maintainer_email,
    notes,
    ogd_groups,
    tag_string,
    url,
    language,
    hash,
    license_id,
    trenner,

    contact_header,
    role,
    contact_url,
    contact_mail,
    contact_address,
    trenner,

    calendar_header,
    calendar_created,
    calendar_published,
    calendar_updated,
    trenner,

    terms_of_use_header,
    free_text,
    license_url,
    attribution_text,
    is_free_to_use,

    subgroups,
    metadata_original_portal,
    metadata_original_id,
    metadata_original_xml,
    metadata_original_html,
    metadata_transformer,
    trenner,
    
    spatial_header,
    spatial_type,
    spatial_coordinates,

    spatial_ags,
    spatial_nuts,
    spatial_uri,
    spatial_text,
    geographical_granularity,
    trenner,
    
    date_header,
    temporal_coverage_from,
    temporal_coverage_to,
    temporal_granularity,
    temporal_granularity_factor,
    trenner,
    
    various_header,
    used_datasets,
    sector,
    images,
    ogd_version
]
