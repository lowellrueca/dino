import clr
from datetime import datetime


def padding(f):
    """
    A function decorator for appending '0' padding on numbering
    """
    def func(data):
        """
        Generates new numbering format of data with the applied padding
        :returns: A list of new numbering data
        """
        data_ = []
        data_count = len(data)
        res = f(data)
        to_pad = lambda x, y: x.ToString().PadLeft(y, "0")

        if data_count >= 100:
            data_ = map(lambda r: to_pad(r, 3), res)

        else:
            data_ = map(lambda r: to_pad(r, 2) if data_count >= 10 else r, res)

        return data_

    return func

def created_at():
    """
    Generates date and time in COBie format
    :returns: string formatted date and time in the form of 2000-01-01T08:10:10
    """
    dt_now = datetime.now()
    year = dt_now.year
    month = dt_now.month
    day = dt_now.day

    yy_mm_dd = "{0}-{1}-{2}".format(year, month, day)

    hour = dt_now.hour
    minute = dt_now.minute
    second = dt_now.second

    hh_mm_ss = "T{0}:{1}:{2}".format(hour, minute, second)

    date = "{0}{1}".format(yy_mm_dd, hh_mm_ss)

    return date

def generate_keys(data, key, separator):
    """
    Generates a numerize key according to the data's count
    :param data: Any type of list data
    :param key: Any data that can be prepend as a key
    :returns: A list of keys
    """
    return map(lambda d: "{0}{1}{2}".format(key, separator, d), data)

def join_data(data1, data2, separator):
    """
    Joins the 2 sets of data
    :param data1: The first list of data
    :param data2: The second list of data
    :param separator: The separator between the 2 sets of data
    :returns: The list of joined data
    """
    return map(lambda d1, d2: \
            "{0}{2}{1}".format(d1.ToString(), d2.ToString(), separator), data1, data2)

@padding
def numerize(data):
    """
    Generates series of number base on the data's count
    :param data: Any type of list data
    :returns: List of numbers in string
    """
    return map(lambda d: data.IndexOf(d)+1, data)
