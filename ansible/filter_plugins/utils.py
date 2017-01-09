import os


def lookupValue(value, arg):
    result = value
    for key in arg.split("."):
        result = result[key]
    return result


def lastPath(value):
    return os.path.basename(os.path.normpath(value))

def unsafe(value):
    return value.replace("<<<<", "{{").replace(">>>>", "}}").replace("||","'")


class FilterModule(object):

    filter_map =  {
        'lookupValue': lookupValue,
        'lastPath': lastPath,
        'unsafe': unsafe
    }

    def filters(self):
        return self.filter_map
