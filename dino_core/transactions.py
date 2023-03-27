import clr
import sys

sys.path.append('C:/Program Files/Dynamo/Dynamo Revit/1.3/Revit_2019')
clr.AddReference('RevitServices')

from RevitServices.Persistence import DocumentManager as DM
from RevitServices.Transactions import TransactionManager as TM


def transaction_handler(f):
    """
    A decorator handling the transaction for tasks function
    :param f: The function that executes task
    :returns: The function that wraps the args
    """
    def func(data1, data2):
        """
        A function that wrap the args
        :param data1: The first list of data
        :param data2: The second list of data
        :returns f: The wrapped function
        """
        doc = DM.Instance.CurrentDBDocument
        tmi = TM.Instance

        try:
            tmi.EnsureInTransaction(doc)
            return f(data1, data2)

        except Exception:
            tmi.ForceCloseTransaction()

        finally:
            tmi.TransactionTaskDone()

    return func
