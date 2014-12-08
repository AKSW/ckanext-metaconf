#!/usr/bin/env python
# -*- coding: utf-8 -*-

# use Unicode
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import uuid

class McBlock:

    def __init__(self):
        self._id   = uuid.uuid4()
        self._type = ''
        self._name = ''
        self._validator = []
        self._converter = []
        self._opt_value = {}


    @property
    def id(self):
        """I'm the 'id' property."""
        return self._id

    @property
    def type(self):
        """I'm the 'typ' property."""
        return self._type

    @type.setter
    def type(self, value):
        self._type = value

    @property
    def name(self):
        """I'm the 'name' property."""
        return self._name.decode('utf-8')

    @name.setter
    def name(self, value):
        self._name = value

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
        return { self.name: [ self.validator, self.converter ] }
