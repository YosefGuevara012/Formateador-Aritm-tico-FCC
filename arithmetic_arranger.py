def arithmetic_arranger(problems):
    
    if len(problems) > 5:
      raise TypeError("Error: Too many problems.")
    
    num_1=[]
    num_2=[]
    operators=[]

    # spliting the list

    for problem in problems:
      problem = problem.split()
      num_1.append(problem[0])
      operators.append(problem[1])
      num_2.append(problem[2])

    # checking the right operators

    for operator in operators:
      if operator != "+" and operator != "-":
        print("Error: Operator must be '+' or '-'.")
    
    for(num1,num2) in zip(num_1,num_2):
      if num1.isdigit() == False or num2.isdigit() == False:
        print("Error: Numbers must only contain digits.")

    # checking the number of digits

    for(num1,num2) in zip(num_1,num_2):
      if len(num1) > 4  or len(num2) > 4:
        print("Error: Numbers cannot be more than four digits.")
    
    result=[]

    # calculations

    for(num1,operator,num2) in zip(num_1,operators,num_2):
      if operator == "+":
        result.append(str(int(num1)+int(num2)))
      else:
        result.append(str(int(num1)-int(num2)))


    botton =[]
    lines = []
    
    # set the proper format on two list
    for(num1,operator,num2) in zip(num_1,operators,num_2):
      if len(num1) > len(num2):
        botton.append(operator + " "*(len(num1)-len(num2)+1) + num2)
        lines.append("-"*(len(num1)+2))
      elif len(num1) < len(num2):
        botton.append(operator + " "*(len(num2)-len(num1)) + num2)
        lines.append("-"*(len(num2)+2))
      else:
        botton.append(operator + " " + num2)
        lines.append("-"*(len(num1)+2))



    return botton[1]
    #return arranged_problems