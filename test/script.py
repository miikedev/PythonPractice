def arithmetic_arranger(problems, show_results=True):
    print('starting arithmetic arranger...')
    if (len(problems) > 5):
        print('Error: too many problems')
        return
    a, b, o, r, length = [], [], [], [], []
    for problem in problems:
        #split into components
        splitted = problem.split(' ')
        print(splitted)
        print(len(splitted))
        if len(splitted) != 3:
            print('Error: each problem must have one operator and two operands')
            return 
        num1, operator, num2 = splitted[0], splitted[1], splitted[2]
        if operator not in ('+','-'):
            print('Error: operator must be + or -')
            return
        
        

arithmetic_arranger(['2 + 3','5 + 3','10 - 3','40 + 3','44  2'], show_results=True)

# arithmetic_arranger(['2 + 3','5 + 3','10 - 3','40 + 3','44 - 2','33 + 3'], show_results=True)