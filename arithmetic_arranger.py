# https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/arithmetic-formatter

# For public execution and test
# https://replit.com/@ToniG4/boilerplate-arithmetic-formatter


import re

def arithmetic_arranger(problems, results = False):

    top_line = ""
    bottom_line = ""
    dash_line = ""
    result_line = ""

    if len(problems) > 5 :
        return "Error: Too many problems."

    for problem in problems :
        
        top_num, sign, bottom_num = problem.split()

        if re.fullmatch("[0-9]+", top_num) == None or re.fullmatch("[0-9]+", bottom_num) == None :
            return "Error: Numbers must only contain digits."        
        
        if len(top_num) > 4 or len(bottom_num) > 4 :
            return "Error: Numbers cannot be more than four digits."

        if sign != "+" and sign != "-" :
            return "Error: Operator must be '+' or '-'."

        # Determine the length of the operation for alignment
        if len(top_num) > len(bottom_num) : max_len = len(top_num)
        elif len(top_num) < len(bottom_num) : max_len = len(bottom_num)
        else : max_len = len(top_num)

        # Dashes include a space and the sign
        dashes = max_len + 2

        # Determine the spaces at the left of each operand and the result
        # (the sign is placed with the second operand)
        top_num_spaces = dashes - len(top_num)
        bottom_num_spaces = dashes - len(bottom_num) - 1

        if sign == '+' : result_num = int(top_num) + int(bottom_num)
        else : result_num = int(top_num) - int(bottom_num)

        result_num = str(result_num)
        result_num_spaces = dashes - len(result_num)

        # Create the string for each line
        # There are 4 spaces in between each operation
        i = 0
        top_line_spaces = ""
        while i < top_num_spaces :
            top_line_spaces = top_line_spaces + " "
            i = i + 1

        top_line = top_line + top_line_spaces + top_num + "    "
        
        i = 0
        bottom_line_spaces = ""
        while i < bottom_num_spaces :
            bottom_line_spaces = bottom_line_spaces + " "
            i = i + 1

        bottom_line = bottom_line + sign + bottom_line_spaces + bottom_num + "    "

        i = 0
        while i < dashes :
            dash_line = dash_line + "-"
            i = i + 1
        
        dash_line = dash_line + "    "

        i = 0
        result_line_spaces = ""
        while i < result_num_spaces :
            result_line_spaces = result_line_spaces + " "
            i = i + 1

        result_line = result_line + result_line_spaces + result_num + "    "

    # Remove the last 4 spaces
    arranged_problems = top_line[: len(top_line) - 4 ] + "\n" + bottom_line[: len(bottom_line) - 4 ] + "\n" + dash_line[: len(dash_line) - 4 ]

    if results == True : arranged_problems = arranged_problems + "\n" + result_line[: len(result_line) - 4 ]

    return arranged_problems


# Example execution:
print( arithmetic_arranger( ['44 + 815', '909 - 2', '45 + 43', '123 + 49', '888 + 40'], True ) )

