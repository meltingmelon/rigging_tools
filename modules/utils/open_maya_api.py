"""
Author: Mel Ho
Website: www.mel-ware.com
Created: 07/03/2023

A utility function that facilitates the conversion of Maya nodes into various API objects like "MObject", or "MDagPath"
"""

from maya import OpenMaya


def toDependencyNode(node):
    """ Converts a node into an OpenMaya Dependency Node.

    Args:
        node (str): The maya node

    Returns:
        object: The OpenMaya Dependency Object.

    Example:
        name = "L_hand_JNT"
        obj = toDependencyNode(name)
        print(obj.typeName())
        Output: joint
    """
    obj = toMObject(node)
    return OpenMaya.MFnDependencyNode(obj)


def toMObject(node):
    """ Converts a node into an OpenMaya Object.

    Args:
        node (str): The maya node.

    Returns:
        object: The OpenMaya object

    Example:
        name = "L_hand_JNT"
        obj = toMObject(name)
        print(obj.fullPathName())
        Output: BASE_GRP|SUB_GRP|L_hand_JNT

    """
    selectionList = OpenMaya.MSelectionList()
    selectionList.add(node)
    obj = OpenMaya.MObject()
    selectionList.getDependNode(0, obj)
    return obj