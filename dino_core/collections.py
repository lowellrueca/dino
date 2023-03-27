import clr
import sys

sys.path.append('C:/Program Files/Dynamo/Dynamo Revit/1.3/Revit_2019')
sys.path.append('C:/Program Files/Autodesk/Revit 2019')

clr.AddReference('RevitAPI')
clr.AddReference('RevitNodes')

from Revit.Elements import Category
from Revit.Elements.InternalUtilities import ElementQueries

from Autodesk.Revit.DB import (
    ElementType, Family, FamilySymbol, WallKind, WallType)


def query_type(elem_type):
    """
    A decorator function that initializes list of elements data retrieved thry
    ElementQueries class to the functions.
    :param elem_type: The ElementType from Autodesk.Revit.DB
    """
    def wrapper(f):
        def fn(cat, *args, **kwargs):
            elems = ElementQueries.OfElementType(elem_type)
            return f(elems, cat, args, kwargs)
        return fn
    return wrapper

def wall_type(f):
    """
    A decortator function that retrieves the element types and filters by
    WallType elements.
    """
    def fn(*args, **kwargs):
        element_types = ElementQueries.OfElementType(ElementType)
        wall_types = filter(lambda e: \
                        e.GetType().Equals(WallType), element_types)

        return f(wall_types, args, kwargs)
    return fn

@query_type(Family)
def get_families(elements, category, *args, **kwargs):
    """
    Retrieves the families by category
    :param elements: list of Elements, an object type from Revits.Elements
    :param category: Category class from Revit.Elements
    :returns: List of elements filtered by category
    """
    cat_id = category.Id.IntegerValue
    return filter(lambda e: \
        e.InternalElement.FamilyCategoryId.IntegerValue.Equals(cat_id), \
        elements)

@query_type(FamilySymbol)
def get_family_symbols(elements, category, *args, **kwargs):
    """
    Retrieves the family symbols by category
    :param elements: list of Elements, an object type from Revits.Elements
    :param category: Category class from Revit.Elements
    :returns: List of elements filtered by category
    """
    cat_id = category.Id.IntegerValue
    return filter(lambda e: e.GetCategory.Id.Equals(cat_id), \
                elements)

def get_elements(category):
    """
    Retrieves the element instances by category
    :param elements: list of Elements, an object type from Revits.Elements
    :param category: Category class from Autodesk.Revit.DB
    :returns: List of elements filtered by category
    """
    cat = Category.ById(category.Id.IntegerValue)
    return ElementQueries.OfCategory(cat)

@wall_type
def get_basic_wall_types(elements, *args, **kwargs):
    """
    Retrieves the basic wall types
    :param elements: list of Elements, an object type from Revits.Elements
    :returns: List of wall types filtered by WallKind.Basic from
              Autodesk.Revit.DB
    """
    return filter(lambda wt: wt.InternalElement.Kind.Equals(WallKind.Basic), \
                elements)

@wall_type
def get_curtain_wall_types(elements, *args, **kwargs):
    """
    Retrieves the basic wall types
    :param elements: list of Elements, an object type from Revits.Elements
    :returns: List of wall types filtered by WallKind.Curtain from
              Autodesk.Revit.DB
    """
    return filter(lambda wt: wt.InternalElement.Kind.Equals(WallKind.Curtain), \
                elements)
