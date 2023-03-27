import clr
import sys

sys.path.append('C:/Program Files/Dynamo/Dynamo Revit/1.3/Revit_2019')

clr.AddReference('RevitNodes')

from Revit.Elements import ElementWrapper, Parameter

def filter_by_category(elements, category):
    """
    Filters the list of element by category
    :param elements: The list of elements
    :param category: The element's category
    :returns: The list of filtered elements by category
    """
    return filter(lambda e: e.Category.Id.Equals(category.Id), elements)

def filter_by_parameter_name(elements, parameter_name):
    """
    Filters the list of elements by parameter name
    :param elements: The list of elements
    :param parameter_name: Parameter name
    :returns: The list of filtered elements by parameter name
    """
    wrap = lambda e: ElementWrapper.Wrap(e, True)
    return filter(lambda e: \
            Parameter.ParameterByName(wrap(e), parameter_name), \
            elements)

def filter_family_symbols_by_family(family_symbols, family):
    """
    Filters the family_symbols by family
    :param family_symbols: The list of family symbols
    :param family: The family of family symbols
    :returns: List of filtered family symbols
    """
    return filter(lambda fs: fs.Family.Id.Equals(family.Id), family_symbols)

def filter_elements_by_family_and_family_symbols(
        elements, family, family_symbol):
    """
    Filters the elements by family and family symbols
    :param elements: The list of elements
    :param family: The family of the elements
    :param family_symbol: The family symbol of the elements
    :returns: The list of filtered elements
    """
    return filter(lambda e: \
                    e.Symbol.Family.Id.Equals(family.Id) and \
                    e.Symbol.Id.Equals(family_symbol.Id), \
                    elements)
