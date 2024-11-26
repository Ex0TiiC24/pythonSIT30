# c07 Unittest 2024-09-25 Group Wed No.09
# 005 Jackapong Karapinwong
# 009 Nattaphan Phoomiphak
# 010 Natthasith Boonheng
# 011 Taiyo yamamoto
# 028 Phakaphol Dherachaisuphaki

import c07_wed09_review as review
import unittest

class testReview(unittest.TestCase):

    # km to miles test
    def testkm_valid(self):
        print("testkm_valid")
        valid = [10,20,30,40,50]
        for v in valid:
            self.assertAlmostEqual(review.km_to_miles(v),v*0.62137119)
    def testkm_type(self):
        print("testkm_invalid")
        invalid = ["ok","lol","Siam","w"]
        for v in invalid:
            with self.assertRaises(TypeError):
                review.km_to_miles(v)
    def testkm_neg(self):
        print("testkm_neg")
        neg = [-1,-60,-2,-9.5]
        for v in neg:
           with self.assertRaises(ValueError):
               review.km_to_miles(v)

    # consecutive test
    def testconsec_valid(self):
        print("testconsec_valid")
        valid = ["oo","loppo","meowoo","digg"]
        for v in valid:
            self.assertTrue(review.consecutive(v),"Value is not True")

    def testconsec_invalid(self):
        print("testconsec_invalid")
        invalid = ["olo","dicg","dog","meow"]
        for v in invalid:
            self.assertFalse(review.consecutive(v),"Value is not False")
        
    def testconsec_type(self):
        print("testconsec_type")
        invalid = [1,2,3,4,-1,0.4,0.232,-40]
        for v in invalid:
            with self.assertRaises(TypeError):
                review.consecutive(v)
    
    # dulpicate test
    def testdulp_valid(self):
        print("testdulp_valid")
        valid = ["oo","loppo","meowoo","digog"]
        for v in valid:
            self.assertTrue(review.duplicate(v),"Value is not True")

    def testdulp_invalid(self):
        print("testdulp_invalid")
        invalid = ["ok","god","yogt","nope"]
        for v in invalid:
            self.assertFalse(review.duplicate(v),"Value is not False")
        
    def testdulp_type(self):
        print("testdulp_type")
        invalid = [1,2,3,4,-1,0.4,0.232,-40]
        for v in invalid:
            with self.assertRaises(TypeError):
                review.duplicate(v)

    def testmax_type(self):
        print("testmax_type")
        invalid = [["dw",1,"dwdw"],["dede","siam","cool"]]
        for v in invalid:
            with self.assertRaises(TypeError):
                review.max_value(*v)

    def testmax_valid(self):
        print("testmax_valid")
        valid = [[1,2,3],[4,6,5],[679,1000,999]]
        for v in valid:
            self.assertEqual(review.max_value(*v),max(*v))
    
if __name__ == '__main__':
    unittest.main()