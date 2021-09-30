# Name:         Amani Arora
# Course:       CPE 202
# Instructor:   Daniel Kauffman
# Assignment:   Postfix-It
# Term:         Spring 2021



from typing import List

def main() -> None:
    """
    Iteratively prompt the user for an infix expression and display both the
    postfix equivalent and, on the next line, the result as a float (even if it
    is a whole number) rounded to 3 decimal places. Assume the infix expression
    is properly formatted.
    """
    while True:
        try:
            infix = input(">>> ")
            # insert all code for main below this line
            postfix = infix_to_postfix(infix.split(), stack=[])
            print(postfix)
            answer = evaluate_postfix(postfix.split())
            print(answer)
        except EOFError:  # loop breaks with CTRL+d
            break
    print()  # empty line prints before program ends
    # end of main (no return statement is equivalent to |return None|)


# insert additional function definitions below this line
def infix_to_postfix(infix: List[str], stack: List[str]) -> str:
    postfix = ''
    for item in infix:
        res = is_digit_or_not(item)
        if res == True:
            if postfix == '':
                postfix = postfix + str(item)
            else:
                postfix = postfix + " " + str(item)
        else:
            if item == '^' or item == '(':
                stack = exp_or_open_para(stack, item)
            elif item == ')':
                tuple_result = close_para(stack, postfix)
                stack = tuple_result[0]
                postfix = tuple_result[1]
            else:
                tuple_result = other_operator(stack, item, postfix)
                stack = tuple_result[0]
                postfix = tuple_result[1]
    while len(stack) != 0:
        postfix = postfix + " " + str(stack[-1])
        stack.pop()
    return postfix

def is_digit_or_not(item: str) -> bool:
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for x in digits:
        if x in item:
            return True
    return False

def exp_or_open_para(stack: List[str], item: str) -> list:
    stack.append(item)
    return stack

def close_para(stack: List[str], postfix: str) -> tuple:
    while stack[-1] != '(':
        postfix = postfix + " " + str(stack[-1])
        stack.pop()
    stack.pop()
    return (stack, postfix)

def other_operator(stack: List[str], item: str, postfix: str) -> tuple:
    while len(stack) != 0:
        if item == '^':
            if stack[-1] == '*' or stack[-1] == '/':
                break
        if item == '*' or item == '/':
            if stack[-1] == '+' or stack[-1] == '-':
                break
        if stack[-1] == '(':
            break
        postfix = postfix + " " + str(stack[-1])
        stack.pop()
    stack.append(item)
    return (stack, postfix)

def evaluate_postfix(postfix: List[str]) -> str:
    stack = []
    for item in postfix:
        res = is_digit_or_not(item)
        if res == True:
            stack.append(item)
        else:
            num1 = stack[-1]
            stack.pop()
            num2 = stack[-1]
            stack.pop()
            answer = find_answer(float(num1), float(num2), item)
            stack.append(str(answer))
    result = stack[-1]
    return "{:.3f}".format(float(result))

def find_answer(num1: float, num2: float, item: str) -> float:
    if item == '^':
        answer = num2 ** num1
    elif item == '/':
        answer = num2 / num1
    elif item == '*':
        answer = num2 * num1
    elif item == '-':
        answer = num2 - num1
    else:
        answer = num2 + num1
    return answer

# do not add code below this line
if __name__ == "__main__":  # runs main with command |python3 postfixit.py|
    main()