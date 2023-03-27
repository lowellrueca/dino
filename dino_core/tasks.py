import clr
import sys

sys.path.append('C:/Program Files/Autodesk/Revit 2019')
clr.AddReference('RevitAPI')

from Autodesk.Revit.DB import Element
from transactions import transaction_handler

@transaction_handler
def set_element_name(elements, data):
	"""
	Set the elements new name
	:param elements: The list of elements
	:param data: The list of new name
	"""
	map(lambda e, d: Element.Name.SetValue(e, d), elements, data)
