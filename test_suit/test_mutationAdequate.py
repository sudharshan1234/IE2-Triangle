import unittest
from isTriangle import Triangle


class MutationAdequateTest(unittest.TestCase):
    def test1(self):
        actual = Triangle.classify(10, 10, 10)
        expected = Triangle.Type.EQUILATERAL
        self.assertEqual(actual, expected)

    def test2(self):
        actual = Triangle.classify(10, 5, 10)
        expected = Triangle.Type.ISOSCELES
        self.assertEqual(actual, expected)

    def test3(self):
        actual = Triangle.classify(5, 10, 10)
        expected = Triangle.Type.ISOSCELES
        self.assertEqual(actual, expected)

    def test4(self):
        actual = Triangle.classify(10, 10, 5)
        expected = Triangle.Type.ISOSCELES
        self.assertEqual(actual, expected)

    def test5(self):
        actual = Triangle.classify(10, 5, 9)
        expected = Triangle.Type.SCALENE
        self.assertEqual(actual, expected)

    def test6(self):
        actual = Triangle.classify(5, 20, 10)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def test7(self):
        actual = Triangle.classify(0, 10, 10)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
    

    def test8(self):
        actual = Triangle.classify(1, 2, 3)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def test9(self):
        actual = Triangle.classify(1, 2, 2)
        expected = Triangle.Type.ISOSCELES
        self.assertEqual(actual, expected)

    def test10(self):
        actual = Triangle.classify(1, 1, 1)
        expected = Triangle.Type.EQUILATERAL
        self.assertEqual(actual, expected)

    def test11(self):
        actual = Triangle.classify(10, 5, 5)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def test12(self):
        actual = Triangle.classify(2, 3, 10)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def test13(self):
        actual = Triangle.classify(10, 0, 10)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def test14(self):
        actual = Triangle.classify(10, 10, 0)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
    
    def test15(self):
        actual = Triangle.classify(0.5, 10, 19)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
    
 
    def test16(self):
        actual = Triangle.classify(3.5, 3.5, 5.5)
        expected = Triangle.Type.ISOSCELES
        self.assertEqual(actual, expected)
    
   
    def test17(self):
        actual = Triangle.classify(5, 5, 7)
        expected = Triangle.Type.ISOSCELES
        self.assertEqual(actual, expected)

    def test18(self):
        actual = Triangle.classify(5, 7, 0)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def test19(self):
        actual_isosceles = Triangle.Type.ISOSCELES.value
        self.assertEqual(actual_isosceles, 3)

    def test20(self):
        actual = Triangle.Type.EQUILATERAL.value
        self.assertEqual(actual, 2)

    def test21(self):
        actual = Triangle.Type.SCALENE.value
        self.assertEqual(actual, 1)

    def test22(self):
        actual = Triangle.Type.INVALID.value
        self.assertEqual(actual, 0)
    
    def test23(self):
        actual = Triangle.classify(5.1, 5.1, 10.2)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
    
if __name__ == "__main__":
    unittest.main()
