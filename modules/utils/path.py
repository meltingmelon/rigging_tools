"""
Author: Mel Ho
Website: www.mel-ware.com
Created: 07/03/2023

String funcationality for maya object paths
"""

def namespace(name):
    """ This function will return the namespace if any existr.

    Args:
        name (str): The name containing group information

    Returns:
        str: The namespace

    Example:
        name = "base_GRP|sub_GRP|namespace:sphere_GEO"
        namespace(name)
        Output: "namespace"
    """
    if not name:
        return name

    # returns the namespace if it exists
    if name.find(":") != -1:
        return rootName(name).rsplit(":", 1)[0]

    return ""


def baseName(name):
    """ This function will strip the namespaces and grouping information
        of a name. This is useful when working with full paths but needing
        the base for naming.

    Args:
        name (str): The name containing group information

    Returns:
        str: The name without grouping or namespace information

    Example:
        name = "base_GRP|sub_GRP|namespace:sphere_GEO"
        baseName(name)
        Output: "sphere_GEO"
    """
    if not name:
        return name

    return name.split("|")[-1].split(":")[-1]

def rootName(name):
    """ Strips grouping information from a given full path.

    Args:
        name (str): The name containing group information

    Returns:
        str: The name without grouping information

    Example:
        name = "base_GRP|sub_GRP|namespace:sphere_GEO"
        Output: "namespace:sphere_GEO"
    """
    if not name:
        return name

    return name.split("|")[-1]


def generateReprString(cls, name):
    """ Generates the string representation for the __repr__ dunder method.

    Args:
        cls (str): The cls.__name__ of the class
        name (str): The node used

    Returns:
        str: The string representation for the __repr__ special method.

    Example:
        __repr__ = generateReprString(
            self.__class__.__name__,
            self.fullPath
        )
        Output: Dep_Node('sphere_GRP')
    """
    return "{cls}('{node}')".format(cls=cls, node=rootName(name))
