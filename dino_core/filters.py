import clr
import sys

sys.path.append('C:/Program Files/Dynamo/Dynamo Revit/1.3/Revit_2019')

clr.AddReference('RevitNodes')
clr.AddReference('RevitAPI')

from Autodesk.Revit.DB import StorageType
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

def compare_equality(param1, param2):
   """
   Used to compare two parameter values for their equality
   :param param1: The first parameter
   :param param2: The second parameter to compare to
   :returns: Result of true or false
   """
   is_equal = False

   if param1.StorageType.Equals(StorageType.Double) and \
      param2.StorageType.Equals(StorageType.Double):
      
      is_equal = param1.AsDouble() == (param2.AsDouble())
      
   if param1.StorageType.Equals(StorageType.Integer) and \
      param2.StorageType.Equals(StorageType.Integer):
      
      is_equal = param1.AsInteger() == (param2.AsInteger())

   if param1.StorageType.Equals(StorageType.String) and \
      param2.StorageType.Equals(StorageType.String):
      
      is_equal = param1.AsString() == (param2.AsString())

   return is_equal

def compare_inequality(param1, param2):
   """
   Used to compare two parameter values for their inequality
   :param param1: The first parameter
   :param param2: The second parameter to compare to
   :returns: Result of true or false
   """
   is_equal = False

   if param1.StorageType.Equals(StorageType.Double) and \
      param2.StorageType.Equals(StorageType.Double):
      
      is_equal = param1.AsDouble() != param2.AsDouble()
      
   if param1.StorageType.Equals(StorageType.Integer) and \
      param2.StorageType.Equals(StorageType.Integer):
      
      is_equal = param1.AsInteger() != (param2.AsInteger())

   if param1.StorageType.Equals(StorageType.String) and \
      param2.StorageType.Equals(StorageType.String):
      
      is_equal = param1.AsString() != (param2.AsString())

   return is_equal

def filter_elements_by_parameter_equality(elements, param1, param2, is_equal):
   """
   For filtering the elements by comparing two parameter values equality
   :param elements: The list of elements
   :param param1: The first parameter name
   :param param2: The second parameter name to compare to
   :param is_equal: A boolean parameter for filtering the elements,
                    True returns the list of filtered elements based on true
                    results and False is the inversed filtered elements list
   """
   elems = []

   if is_equal:
      elems = filter(lambda e: compare_equality(e.LookupParameter(param1), e.LookupParameter(param2)), elements)

   if not is_equal:
      elems = filter(lambda e: compare_inequality(e.LookupParameter(param1), e.LookupParameter(param2)), elements)
      
   return elems
