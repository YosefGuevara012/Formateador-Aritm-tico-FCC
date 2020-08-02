def arithmetic_arranger(problems,check=False):
    
    if len(problems) > 5:
      return"Error: Too many problems."
    
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
        return"Error: Operator must be '+' or '-'."
    
    for(num1,num2) in zip(num_1,num_2):
      if num1.isdigit() == False or num2.isdigit() == False:
        return"Error: Numbers must only contain digits."

    # checking the number of digits

    for(num1,num2) in zip(num_1,num_2):
      if len(num1) > 4  or len(num2) > 4:
        return"Error: Numbers cannot be more than four digits."
    
    result=[]

    # calculations

    for(num1,operator,num2) in zip(num_1,operators,num_2):
      if operator == "+":
        result.append(str(int(num1)+int(num2)))
      else:
        result.append(str(int(num1)-int(num2)))

    upper = []
    botton =[]
    lines = []
    
    # set the proper format on two list

    for(num1,operator,num2) in zip(num_1,operators,num_2):
      if len(num1) > len(num2):
        upper.append(" "*(2)+ num1)
        botton.append(operator + " "*(len(num1)-len(num2)+1) + num2)
        lines.append("-"*(len(num1)+2))
      elif len(num1) < len(num2):
        upper.append(" "*((len(num2) - len(num1) + 2))+ num1)
        botton.append(operator + " " + num2)
        lines.append("-"*(len(num2)+2))
      else:
        upper.append(" "*2 + num1)
        botton.append(operator + " " + num2)
        lines.append("-"*(len(num1)+2))

    arranged_problems=""

    for num in upper:
      arranged_problems = arranged_problems + num + " "*4

    arranged_problems = arranged_problems + "\n" 

    for under in botton:
      arranged_problems = arranged_problems + under + " "*4
    
    arranged_problems = arranged_problems + "\n" 

    for line in lines:
      arranged_problems = arranged_problems + line + " "*4
    
    if check == True:
      arranged_problems = arranged_problems + "\n" 
      for num in result:
        if(int(num)>0):
          arranged_problems = arranged_problems + " "*2 + num + " "*4
        if(int(num)<0):
          arranged_problems = arranged_problems + " " + num + " "*4


    return arranged_problems