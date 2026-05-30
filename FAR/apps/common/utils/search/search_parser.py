
def wildcard_to_lookup(value: str):

    if value.endswith("*") and value.startswith("*"):
        return "icontains", value.strip("*")

    if value.endswith("*"):
        return "istartswith", value[:-1]

    if value.startswith("*"):
        return "iendswith", value[1:]

    return "iexact", value