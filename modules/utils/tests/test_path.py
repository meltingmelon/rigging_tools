"""
Author: Mel Ho
Website: www.mel-ware.com
Created: 07/05/2023

Tests for Paths modules
"""

import unittest
from modules.utils.path import (
    generateReprString,
    baseName,
    namespace,
    rootName
)


class Test_Path(unittest.TestCase):
    def test_namespace(self):
        name = "base_GRP|sub_GRP|namespace:sphere_GEO"
        expectedResult = "namespace"

        result = namespace(name)
        self.assertEqual(result, expectedResult)

    def test_baseName(self):
        name = "base_GRP|sub_GRP|namespace:sphere_GEO"
        expectedResult = "sphere_GEO"

        result = baseName(name)
        self.assertEqual(result, expectedResult)

    def test_rootName(self):
        name = "base_GRP|sub_GRP|namespace:sphere_GEO"
        expectedResult = "namespace:sphere_GEO"

        result = rootName(name)
        self.assertEqual(result,expectedResult)

    def test_generateReprString(self):
        clsName = "Dep_Node"
        name = "sphere_GRP"
        expectedResult = "Dep_Node('sphere_GRP')"

        result = generateReprString(clsName, name)
        self.assertEqual(result, expectedResult)


if __name__ == "__main__":
    unittest.main()
