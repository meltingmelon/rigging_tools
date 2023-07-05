"""
Author: Mel Ho
Website: www.mel-ware.com
Created: 07/05/2023

Tests for Open Maya API module
"""
import unittest
from maya import cmds as m
from modules.utils.open_maya_api import toMObject, toDependencyNode
from maya import OpenMaya


class Test_Maya_Open_API(unittest.TestCase):
    def setUp(self) -> None:
        self.jointName = "L_hand_JNT"
        self.joint = m.joint(n=self.jointName)

        self.baseGrp = m.group(n="BASE_GRP", em=1)
        self.subGrp = m.group(n="SUB_GRP", em=1)
        m.parent(self.subGrp, self.baseGrp)
        m.parent(self.joint, self.subGrp)

    def tearDown(self) -> None:
        m.delete(self.baseGrp)
    def test_toDependencyNode(self):
        expectedResult = "joint"

        result = toDependencyNode(self.jointName)
        nodeTypeName = result.typeName()
        self.assertEqual(nodeTypeName, expectedResult)

    def test_toMObject(self):
        expectedResult = "|BASE_GRP|SUB_GRP|L_hand_JNT"

        result = toMObject(self.jointName)
        fullPathName = OpenMaya.MFnDagNode(result).fullPathName()

        self.assertEqual(fullPathName, expectedResult)

if __name__ == "__main__":
    unittest.main()