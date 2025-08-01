import unittest
import Function_snacks

class TestDivideOrSqureFunction(unittest.TestCase):

	def test_that_divide_or_square_function_exist(self):
		result = Function_snacks.get_divide_or_square(25)
		self.assertEqual(result, 5)

	def test_that_divide_or_square_function_return_corect_square(self):
		result = Function_snacks.get_divide_or_square(25)
		self.assertEqual(result, 5)

	def test_that_divide_or_square_function_return_corect_remainder(self):
		result = Function_snacks.get_divide_or_square(33)
		self.assertEqual(result, 3)

	
	def test_that_divide_or_square_function_is_negtive_number(self):
		response = Function_snacks.get_divide_or_square(- 2)
		self.assertRaises(ValueError)

	def test_that_divide_or_square_function_is_alphabet(self):
		response = Function_snacks.get_divide_or_square("")
		self.assertRaises(ValueError)

	

class TestFutureInvestmentValue(unittest.TestCase):
	def test_that_investment_value_function_exist(self):
		Function_snacks.get_future_investment_value(25, 12, 34)

	def test_that_investment_amount_not_a_string(self):
		Function_snacks.get_future_investment_value("", 12, 34)
		self.assertRaises(ValueError)

	def test_that_number_of_years_valid(self):
		Function_snacks.get_future_investment_value(32000,  5, 2.5)
		self.assertRaises(ValueError)

	def test_that_monthly_interest_rate_correct(self):
		Function_snacks.get_future_investment_value(32000, - 12, 1)
		self.assertRaises(ValueError)


	def test_that_get_future_investment_value_calculation_correct(self):
		Function_snacks.get_future_investment_value(320000, 5, 3)
		self.assertRaises(ValueError)


	