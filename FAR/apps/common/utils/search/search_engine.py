import re
from django.db.models import Q
from .search_config import SEARCH_FIELD_MAPS
from .search_parser import wildcard_to_lookup


class SearchEngine:

    @staticmethod
    def build_condition(model_key: str, field: str, value: str):
        """
        model_key: location / branch / currency
        field: user input field (code, name, etc.)
        value: search value (C00*, Yangon*)
        """

        field_map = SEARCH_FIELD_MAPS.get(model_key)

        if not field_map:
            return None

        field = field.strip().lower()
        value = value.strip()

        model_field = field_map.get(field)

        if not model_field:
            print("INVALID FIELD:", field)
            return None

        lookup, cleaned_value = wildcard_to_lookup(value)

        print("DEBUG CONDITION:", model_field, lookup, cleaned_value)

        return Q(**{f"{model_field}__{lookup}": cleaned_value})

    

    @staticmethod
    def build_condition(model_key: str, field: str, value: str):

        field_map = SEARCH_FIELD_MAPS.get(model_key)

        if not field_map:
            print("NO FIELD MAP")
            return None

        field = field.strip().lower()
        value = value.strip()

        model_field = field_map.get(field)

        if not model_field:
            print(f"INVALID FIELD: {field}")
            return None

        lookup, cleaned_value = wildcard_to_lookup(value)

        print("BUILD:", model_field, lookup, cleaned_value)

        return Q(**{f"{model_field}__{lookup}": cleaned_value})