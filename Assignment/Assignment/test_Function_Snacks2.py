import unittest
import Function_Snacks2

class TestMaximumIn(unittest.TestCase):
	def test_that_maximum_In_function_exists(self):
		Function_Snacks2.get_maximum_In([78, 56, 45])

	def test_that_maximum_In_argument_valid(self):
		Function_Snacks2.get_maximum_In([23, 24, 13, 12, 56])

	def test_that_maximum_In_function_valid(self):
		maximum = Function_Snacks2.get_maximum_In([23, 24, 13, 12, 56])
		self.assertEqual(maximum, 56)



class TestMinimum_In(unittest.TestCase):
	def test_that_minimum_In_function_exists(self):
		Function_Snacks2.get_minimum_In([78, 56, 45])

	def test_that_minimum_In_argument_valid(self):
		Function_Snacks2.get_minimum_In([23, 24, 13, 12, 56])

	def test_that_minimum_In_function_valid(self):
		minimum = Function_Snacks2.get_minimum_In([23, 24, 13, 12, 56])
		self.assertEqual(minimum, 12)


class TestSum_Of(unittest.TestCase):
	def test_that_sum_Of_exists(self):
		Function_Snacks2.get_sum_Of([78, 56, 45])

	def test_that_sum_Of_args_valid(self):
		Function_Snacks2.get_sum_Of([23, 24, 13, 12, 56])

	def test_that_sum_Of_function_valid(self):
		sum = Function_Snacks2.get_sum_Of([23, 24, 13, 12, 56])
		self.assertEqual(sum, 128)

	def test_that_sum_Of_function_correct(self):
		sum = Function_Snacks2.get_sum_Of([23, 24, 13, 12, 56])
		self.assertRaises(ValueError)



class TestSumOfEvenNumbersIn(unittest.TestCase):
	def test_that_sum_Of_Even_Numbers_In_exists(self):
		Function_Snacks2.get_sum_Of_Even_Numbers_In([78, 56, 45])

	def test_that_get_sum_Of_Even_Numbers_In_valid(self):
		Function_Snacks2.get_sum_Of_Even_Numbers_In([23, 24, 13, 12, 56])

	def test_that_get_sum_Of_Even_Numbers_In_function_valid(self):
		sum = Function_Snacks2.get_sum_Of_Even_Numbers_In([23, 24, 13, 12, 56])
		self.assertEqual(sum, 128)

	def test_that_get_sum_Of_Even_Numbers_In_correct(self):
		sum = Function_Snacks2.get_sum_Of_Even_Numbers_In([23, 24, 13, 12, 56])
		self.assertRaises(ValueError)


class TestSumOfOddNumbersIn(unittest.TestCase):
	def test_that_sum_Of_Odd_Numbers_In_exists(self):
		Function_Snacks2.get_sum_Of_Odd_Numbers_In([78, 56, 45])

	def test_that_get_sum_Of_Odd_Numbers_In_valid(self):
		Function_Snacks2.get_sum_Of_Odd_Numbers_In([23, 24, 13, 12, 56])

	def test_that_get_sum_Of_Odd_Numbers_In_function_valid(self):
		odd = Function_Snacks2.get_sum_Of_Odd_Numbers_In([23, 24, 13, 12, 56])
		self.assertEqual(odd, 36)

	def test_that_get_sum_Of_Odd_Numbers_In_correct(self):
		odd = Function_Snacks2.get_sum_Of_Odd_Numbers_In([23, 24, 13, 12, 56])
		self.assertRaises(ValueError)


class TestMaximumAndMinimumOf(unittest.TestCase):
	def test_that_maximum_And_Minimum_Of_function_exists(self):
		Function_Snacks2.get_maximum_And_Minimum_Of([2, 4, 45, 100])

	#def test_that_maximum_valid(self):
		#maximum = Function_Snacks2.get_maximum_And_Minimum_Of([2, 4, 45, 100])
		#self.assertEqual(maximum, 100)
	
	#def test_that_minimum_valid(self):
		#minimum = Function_Snacks2.get_maximum_And_Minimum_Of([2, 4, 45, 100])
		#self.assertEqual(minimum, 2)

	def test_that_maxmin_valid(self):
		maxmin = Function_Snacks2.get_maximum_And_Minimum_Of([2, 4, 45, 100])
		self.assertEqual(maxmin, [100, 2])

