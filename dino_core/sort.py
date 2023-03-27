def sort_elements_by_param_of_int(elems, params):
    """
    Sorts the elements by parameter thru LookupParameter and AsInteger method
    :param elems: The list of elements
    :param params: The list of parameters to lookup
    :returns: Sorted elements
    """
    result = []

    if len(params) == 1:
        param1 = params[0]
        result = sorted(elems, \
                    key=lambda e: e.LookupParameter(param1).AsInteger())

    if len(params) == 2:
        param1 = params[0]
        param2 = params[1]
        result = sorted(\
                    sorted(elems, \
                    key=lambda e: e.LookupParameter(param2).AsInteger()), \
                    key=lambda e: e.LookupParameter(param1).AsInteger())

    if len(params) == 3:
        param1 = params[0]
        param2 = params[1]
        param3 = params[2]
        result = sorted(\
                    sorted(\
                    sorted(elems, \
                    key=lambda e: e.LookupParameter(param3).AsInteger()), \
                    key=lambda e: e.LookupParameter(param2).AsInteger()), \
                    key=lambda e: e.LookupParameter(param1).AsInteger())

    return result

def sort_elements_by_param_of_double(elems, params):
    """
    Sorts the elements by parameter thru LookupParameter and AsInteger method
    :param elems: The list of elements
    :param params: The list of parameters to lookup
    :returns: Sorted elements
    """
    result = []

    if len(params) == 1:
        param1 = params[0]
        result = sorted(elems, \
                    key=lambda e: e.LookupParameter(param1).AsDouble())

    if len(params) == 2:
        param1 = params[0]
        param2 = params[1]
        result = sorted(\
        sorted(elems, \
        key=lambda e: e.LookupParameter(param2).AsDouble()), \
        key=lambda e: e.LookupParameter(param1).AsDouble())

    if len(params) == 3:
        param1 = params[0]
        param2 = params[1]
        param3 = params[2]
        result = sorted(\
                    sorted(\
                    sorted(elems, \
                    key=lambda e: e.LookupParameter(param3).AsDouble()), \
                    key=lambda e: e.LookupParameter(param2).AsDouble()), \
                    key=lambda e: e.LookupParameter(param1).AsDouble())

    return result

def sort_elements_by_param_of_string(elems, params):
    """
    Sorts the elements by parameter thru LookupParameter and AsString method
    :param elems: The list of elements
    :param params: The list of parameters to lookup
    :returns: Sorted elements
    """
    result = []

    if len(params) == 1:
        param1 = params[0]
        result = sorted(elems, \
                    key=lambda e: e.LookupParameter(param1).AsString())

    if len(params) == 2:
        param1 = params[0]
        param2 = params[1]
        result = sorted(\
                    sorted(elems, \
                    key=lambda e: e.LookupParameter(param2).AsString()), \
                    key=lambda e: e.LookupParameter(param1).AsString())

    if len(params) == 3:
        param1 = params[0]
        param2 = params[1]
        param3 = params[2]
        result = sorted(\
                    sorted(\
                    sorted(elems, \
                    key=lambda e: e.LookupParameter(param3).AsString()), \
                    key=lambda e: e.LookupParameter(param2).AsString()), \
                    key=lambda e: e.LookupParameter(param1).AsString())

    return result

def sort_elements_by_param_of_value_string(elems, params):
    """
    Sorts the elements by parameter thru LookupParameter and AsValueString method
    :param elems: The list of elements
    :param params: The list of parameters to lookup
    :returns: Sorted elements
    """
    result = []

    if len(params) == 1:
        param1 = params[0]
        result = sorted(elems, \
                    key=lambda e: e.LookupParameter(param1).AsValueString())

    if len(params) == 2:
        param1 = params[0]
        param2 = params[1]
        result = sorted(\
                    sorted(elems, \
                    key=lambda e: e.LookupParameter(param2).AsValueString()), \
                    key=lambda e: e.LookupParameter(param1).AsValueString())

    if len(params) == 3:
        param1 = params[0]
        param2 = params[1]
        param3 = params[2]
        result = sorted(\
                    sorted(\
                    sorted(elems, \
                    key=lambda e: e.LookupParameter(param3).AsValueString()), \
                    key=lambda e: e.LookupParameter(param2).AsValueString()), \
                    key=lambda e: e.LookupParameter(param1).AsValueString())

    return result
