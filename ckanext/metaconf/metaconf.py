#!/usr/bin/env python
# -*- coding: utf-8 -*-

# use Unicode
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import uuid

class McBlock:

    def __init__(self):
        self._type = ''
        self._rdf_type = ''
        self._key = ''
        self._label = ''
        self._validator = []
        self._converter = []
        self._opt_value = {}
        self._mandatory = False
        
    @property
    def mandatory(self):
        """I'm the 'mandatory' property."""
        return self._mandatory

    @mandatory.setter
    def mandatory(self, value):
        self._mandatory = value

    @property
    def type(self):
        """I'm the 'typ' property."""
        return self._type

    @type.setter
    def type(self, value):
        if value == 'hline':
            self._key = 'hline'
        self._type = value

    @property
    def label(self):
        """I'm the 'label' property."""
        return self._label

    @label.setter
    def label(self, value):
        self._label = value

    @property
    def rdf_type(self):
        """I'm the 'rdf_typ' property."""
        return self._rdf_type

    @type.setter
    def rdf_type(self, value):
        self._rdf_type = value

    @property
    def key(self):
        """I'm the 'key' property."""
        return self._key.decode('utf-8')

    @key.setter
    def key(self, value):
        self._key = value

    @property
    def validator(self):
        """I'm the 'validator' property."""
        return self._validator

    @validator.setter
    def validator(self, value):
        self._validator = value
        
    @property
    def converter(self):
        """I'm the 'converter' property."""
        return self._converter

    @converter.setter
    def converter(self, value):
        self._converter = value

    @property
    def opt_value(self):
        """I'm the 'opt_value' property."""
        return self._opt_value

    @opt_value.setter
    def opt_value(self, value):
        self._opt_value = value

    def create_schema_entry(self):
        return { self.key: [ self.validator, self.converter ] }
