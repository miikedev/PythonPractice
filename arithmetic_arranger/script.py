def arithmetic_arranger(problems, show_results=False):  
    # Check for the maximum number of problems  
    if len(problems) > 5:  
        return "Error: Too many problems."  

    # Initialize lists to store components of the problems  
    a, b, o, r, lengths = [], [], [], [], []  

    for problem in problems:  
        # Split the problem into components  
        splitted = problem.split()  
        if len(splitted) != 3:  
            return "Error: Each problem must have 2 operands and an operator."  

        num1, operator, num2 = splitted[0], splitted[1], splitted[2]  
        
        # Check if the operator is valid  
        if operator not in ('+', '-'):  
            return "Error: Operator must be '+' or '-'."  

        # Check if both numbers are digits  
        if not (num1.isdigit() and num2.isdigit()):  
            return "Error: Numbers must only contain digits."  

        # Check the length of the operands  
        if len(num1) > 4 or len(num2) > 4:  
            return "Error: Numbers cannot be more than four digits."  

        # Append the components to their respective lists  
        a.append(num1)  
        b.append(num2)  
        o.append(operator)  

        # Calculate the maximum length needed for formatting (including space for operator)  
        lengths.append(max(len(num1), len(num2)) + 2)  

        # Calculate result only if show_results is True  
        if show_results:  
            if operator == '+':  
                result = str(int(num1) + int(num2))  
            else:  # operator == '-'  
                result = str(int(num1) - int(num2))  
            r.append(result)  

    # Prepare the formatted output lines  
    first_line, second_line, dash_line, result_line = "", "", "", ""  
    
    for i in range(len(a)):  
        first_line += a[i].rjust(lengths[i]) + "    "  
        second_line += o[i] + " " + b[i].rjust(lengths[i] - 2) + "    "  
        dash_line += '-' * lengths[i] + "    "  
        if show_results:  
            result_line += r[i].rjust(lengths[i]) + "    "  

    # Combine all lines and strip trailing spaces  
    if show_results:  
        arranged_output = "\n".join([first_line.rstrip(), second_line.rstrip(), dash_line.rstrip(), result_line.rstrip()])  
    else:  
        arranged_output = "\n".join([first_line.rstrip(), second_line.rstrip(), dash_line.rstrip()])  

    return arranged_output  

# Example usage  
print(arithmetic_arranger(["3 + 855", "988 + 40"], True))  
print(arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"], True))