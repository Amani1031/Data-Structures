# Name:         Amani Arora
# Course:       CPE 202
# Instructor:   Daniel Kauffman
# Assignment:   Postfix-It
# Term:         Spring 2021

import unittest

import postfixit

class TestInfixToPostfix(unittest.TestCase):

    def test_infix_to_postfix_1(self):
        infix = '1 + 2 / ( 3 * 7 )'
        postfix = '1 2 3 7 * / +'
        self.assertEqual(postfixit.infix_to_postfix(infix.split(), stack=[]),
                         postfix)

    def test_infix_to_postfix_2(self):
        infix = '9 * 2 / 8 - 8 + 9 * 7'
        postfix = '9 2 * 8 / 8 - 9 7 * +'
        self.assertEqual(postfixit.infix_to_postfix(infix.split(), stack=[]),
                         postfix)

    def test_infix_to_postfix_3(self):
        infix = '6 * 7 + ( 9 / 3 + ( 9 - 8 ) )'
        postfix = '6 7 * 9 3 / 9 8 - + +'
        self.assertEqual(postfixit.infix_to_postfix(infix.split(), stack=[]),
                         postfix)

    def test_infix_to_postfix_4(self):
        infix = '3 * 2 / 2 + ( 4 + 100 )'
        postfix = '3 2 * 2 / 4 100 + +'
        self.assertEqual(postfixit.infix_to_postfix(infix.split(), stack=[]),
                         postfix)

    def test_infix_to_postfix_5(self):
        infix = '4 * 9 / 12 + 1 - ( 4 + 6 )'
        postfix = '4 9 * 12 / 1 + 4 6 + -'
        self.assertEqual(postfixit.infix_to_postfix(infix.split(), stack=[]),
                         postfix)

    def test_infix_to_postfix_6(self):
        infix = '4 * 9 / 12 + 1 - ( 2 ^ 2 + 6 )'
        postfix = '4 9 * 12 / 1 + 2 2 ^ 6 + -'
        self.assertEqual(postfixit.infix_to_postfix(infix.split(), stack=[]),
                         postfix)

class TestIsDigitOrNot(unittest.TestCase):

    def test_is_digit_or_not_1(self):
        self.assertEqual(postfixit.is_digit_or_not('-8'),
                         True)

    def test_is_digit_or_not_2(self):
        self.assertEqual(postfixit.is_digit_or_not('^'),
                         False)

    def test_is_digit_or_not_3(self):
        self.assertEqual(postfixit.is_digit_or_not('*'),
                         False)

    def test_is_digit_or_not_4(self):
        self.assertEqual(postfixit.is_digit_or_not('9.78'),
                         True)

    def test_is_digit_or_not_5(self):
        self.assertEqual(postfixit.is_digit_or_not('-4.2'),
                         True)

class TestExpOrOpenPara(unittest.TestCase):

    def test_exp_or_open_para_1(self):
        stack = ['1', '2', '*']
        item = '4'
        stack_new = ['1', '2', '*', '4']
        self.assertEqual(postfixit.exp_or_open_para(stack, item),
                         stack_new)

    def test_exp_or_open_para_2(self):
        stack = ['1', '6', '/', '4']
        item = '*'
        stack_new = ['1', '6', '/', '4', '*']
        self.assertEqual(postfixit.exp_or_open_para(stack, item),
                         stack_new)

    def test_exp_or_open_para_3(self):
        stack = ['1']
        item = '5'
        stack_new = ['1', '5']
        self.assertEqual(postfixit.exp_or_open_para(stack, item),
                         stack_new)

    def test_exp_or_open_para_4(self):
        stack = ['1', '7', '+']
        item = '9'
        stack_new = ['1', '7', '+', '9']
        self.assertEqual(postfixit.exp_or_open_para(stack, item),
                         stack_new)

    def test_exp_or_open_para_5(self):
        stack = ['1', '7', '+', '(']
        item = ')'
        stack_new = ['1', '7', '+', '(', ')']
        self.assertEqual(postfixit.exp_or_open_para(stack, item),
                         stack_new)

class TestClosePara(unittest.TestCase):

    def test_close_para_1(self):
        stack = ['1', '2', '*', '(', '5']
        postfix = '4 5 +'
        tuple_result = (['1', '2', '*'], '4 5 + 5')
        self.assertEqual(postfixit.close_para(stack, postfix),
                         tuple_result)

    def test_close_para_2(self):
        stack = ['1', '4', '(', '*', '9', '5', '+']
        postfix = '7 3 *'
        tuple_result = (['1', '4'], '7 3 * + 5 9 *')
        self.assertEqual(postfixit.close_para(stack, postfix),
                         tuple_result)

    def test_close_para_3(self):
        stack = ['1', '(', '5', '9', '/']
        postfix = '9 4 * 9 8 +'
        tuple_result = (['1'], '9 4 * 9 8 + / 9 5')
        self.assertEqual(postfixit.close_para(stack, postfix),
                         tuple_result)

    def test_close_para_4(self):
        stack = ['1', '6', '(', '*', '9']
        postfix = '7 9 /'
        tuple_result = (['1', '6'], '7 9 / 9 *')
        self.assertEqual(postfixit.close_para(stack, postfix),
                         tuple_result)

    def test_close_para_5(self):
        stack = ['9', '6', '(', '3', '11', '+', '5', '*']
        postfix = '7 5 +'
        tuple_result = (['9', '6'], '7 5 + * 5 + 11 3')
        self.assertEqual(postfixit.close_para(stack, postfix),
                         tuple_result)

class TestOtherOperator(unittest.TestCase):

    def test_other_operator_1(self):
        stack = ['9', '6', '(', '3', '11', '+', '5', '*']
        item = '^'
        postfix = '7 5 +'
        tuple_result = (['9', '6', '(', '3', '11',
                         '+', '5', '*', '^'], '7 5 +')
        self.assertEqual(postfixit.other_operator(stack, item, postfix),
                         tuple_result)

    def test_other_operator_2(self):
        stack = ['1', '2', '*', '(', '5']
        postfix = '4 5 +'
        item = '8'
        tuple_result = (['1', '2', '*', '(', '8'], '4 5 + 5')
        self.assertEqual(postfixit.other_operator(stack, item, postfix),
                         tuple_result)

    def test_other_operator_3(self):
        stack = ['1', '6', '(', '*', '9']
        postfix = '7 9 /'
        item = '4'
        tuple_result = (['1', '6', '(', '4'], '7 9 / 9 *')
        self.assertEqual(postfixit.other_operator(stack, item, postfix),
                         tuple_result)

    def test_other_operator_4(self):
        stack = ['8', '2', '+', '9', '11', '^']
        postfix = '7 9 /'
        item = '+'
        tuple_result = (['+'], '7 9 / ^ 11 9 + 2 8')
        self.assertEqual(postfixit.other_operator(stack, item, postfix),
                         tuple_result)

    def test_other_operator_5(self):
        stack = ['8', '2', '7', '+', '*']
        postfix = '2 3'
        item = '+'
        tuple_result = (['+'], '2 3 * + 7 2 8')
        self.assertEqual(postfixit.other_operator(stack, item, postfix),
                         tuple_result)

class TestEvaluatePostfix(unittest.TestCase):

    def test_evaluate_postfix_1(self):
        postfix = '7 5 +'
        answer = '12.000'
        self.assertEqual(postfixit.evaluate_postfix(postfix.split()),
                         answer)

    def test_evaluate_postfix_2(self):
        postfix = '4 7 6 ^ +'
        answer = '117653.000'
        self.assertEqual(postfixit.evaluate_postfix(postfix.split()),
                         answer)

    def test_evaluate_postfix_3(self):
        postfix = '1 -8 9 2 - 1 ^ * +'
        answer = '-55.000'
        self.assertEqual(postfixit.evaluate_postfix(postfix.split()),
                         answer)

    def test_evaluate_postfix_4(self):
        postfix = '11 22 3 16 2 / + / -'
        answer = '9.000'
        self.assertEqual(postfixit.evaluate_postfix(postfix.split()),
                         answer)

    def test_evaluate_postfix_5(self):
        postfix = '8 7 4 3 - ^ -'
        answer = '1.000'
        self.assertEqual(postfixit.evaluate_postfix(postfix.split()),
                         answer)

class TestFindAnswer(unittest.TestCase):

    def test_find_answer_1(self):
        num1 = '2.3'
        num2 = '2'
        item = '^'
        self.assertEqual(postfixit.find_answer(float(num1), float(num2), item),
                         4.924577653379664)

    def test_find_answer_2(self):
        num1 = '5'
        num2 = '2'
        item = '+'
        self.assertEqual(postfixit.find_answer(float(num1), float(num2), item),
                         7)

    def test_find_answer_3(self):
        num1 = '9'
        num2 = '16.6'
        item = '-'
        self.assertEqual(postfixit.find_answer(float(num1), float(num2), item),
                         7.600000000000001)

    def test_find_answer_4(self):
        num1 = '7'
        num2 = '8'
        item = '*'
        self.assertEqual(postfixit.find_answer(float(num1), float(num2), item),
                         56)

    def test_find_answer_5(self):
        num1 = '6'
        num2 = '81'
        item = '/'
        self.assertEqual(postfixit.find_answer(float(num1), float(num2), item),
                         13.5)


if __name__ == "__main__":
    unittest.main()
