from collections import OrderedDict
from typing import Dict
from django.db.models import Q
from dataclasses import dataclass


@dataclass
class FilterType:
    name: str
    options: []
    options_actions: []


class Filtration:
    def __init__(self, fields_to_filter):
        self.fields_to_filter = fields_to_filter

    def get_filter_types(self, items):
        filter_types = {}
        for name, field in self.fields_to_filter.items():
            if 'enum' not in field:
                filter_types[field] = FilterType(name=name, options=sorted(set(items.values_list(field, flat=True))),
                                                 options_actions=[])
            else:
                options_actual = items.values_list(field['enum'], flat=True)
                options = [getattr(item, f'get_{field["enum"]}_display')() for item in items]

                filter_types[field['enum']] = FilterType(name=name, options=list(OrderedDict.fromkeys(options)),
                                                         options_actions=list(OrderedDict.fromkeys(options_actual)))
        return filter_types

    @staticmethod
    def filters_from_request(request, filter_types):
        filters = {}
        for index, (field, filter_type) in enumerate(filter_types.items()):
            filter = filter_type.options_actions if getattr(filter_type, 'options_actions') else filter_type.options
            filters[field] = [filter[int(option)] for option in request.GET.getlist(str(index), '')]
        return filters

    @staticmethod
    def filter_items(items, filters):
        query_set_and = Q()
        for key, data in filters.items():
            query_set_or = Q()
            for index in data:
                query_set_or = query_set_or | Q(**{key: index})
            query_set_and = query_set_and & query_set_or
        return items.filter(query_set_and)

    @staticmethod
    def checked_filters_from_request(request, filter_types):
        checked = []
        for index, field in enumerate(filter_types.values()):
            checked_sub = [False] * len(field.options)
            for checked_option in request.GET.getlist(str(index), ''):
                checked_sub[int(checked_option)] = True
            checked.append(checked_sub)
        return checked
