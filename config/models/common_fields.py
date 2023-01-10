from django.db import models, connections

from django.core.exceptions import ValidationError
from django.utils.functional import cached_property
from bs4 import BeautifulSoup as bs


class ParsedSoup(bs):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    @property
    def images(self):
        return [img['src'] for img in self.select('img')]
    
    @property
    def texts(self):
        return list(self.stripped_strings)


class HTMLField(models.TextField):
    description = "HTML Field"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def from_db_value(self, value, expression, connection):
        if value is None:
            return value
        return ParsedSoup(value, 'lxml')

    def to_python(self, value):
        if value is None:
            return value
        return ParsedSoup(value, 'lxml')

    def get_prep_value(self, value):
        if value is None:
            return value
        return str(value)

    def value_to_string(self, obj):
        value = self.value_from_object(obj)
        return self.get_prep_value(value)
