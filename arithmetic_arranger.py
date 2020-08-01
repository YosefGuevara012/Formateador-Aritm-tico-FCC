def arithmetic_arranger(problems):
    
    if len(problems) > 5:
      raise TypeError("Too many problems.")
    
    problems_list = []
    num_1=[]
    num_2=[]
    operators=[]
    result=[]

    for i in range(len(problems)):

      problems_list.append(problems[i].split())

      if problems_list[i][1] != '+' and problems_list[i][1]!= "-":

        raise TypeError("Operator must be '+' or '-'.")

      num_1.append(problems_list[i][0])
      operators.append(problems_list[i][1])
      num_2.append(problems_list[i][2])

    result=[]
    
    for(num1,num2) in zip(num_1,num_2):
      if len(num1) > 4 or len(num2) > 4:
        raise TypeError("too long")

    for i in range(len(problems)):
      if operators[i] == '+':
        result[i] = int(num_1[i]) + int(num_2[i])

    return problems_list
    #return arranged_problems