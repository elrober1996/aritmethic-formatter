def magic(up, down, op, result, long):
    upL= ""
    downL = ""
    opL = ""
    resultL = ""
    longL = ""
    line = ""
    #print(up)
    for i in range(len(up)):
        upL += up[i].rjust(long[i]) + "    "
    #print(upL.rstrip())
    for i in range(len(up)):
        downL += op[i]+ down[i].rjust(long[i] - 1) + "    "
    #print(downL.rstrip())
    for i in range(len(up)):
        line += ("-" * long[i]) + "    "
    #print(line.rstrip())
    for i in range(len(up)):
        resultL += result[i].rjust(long[i]) + "    "
    #print(resultL.rstrip())
    #return [upL.rstrip(), downL.rstrip(), line.rstrip(), resultL.rstrip()]
    return (upL.rstrip() + "\n") + (downL.rstrip() + "\n") +line.rstrip()

def truemagic(up, down, op, result, long):
    upL= ""
    downL = ""
    opL = ""
    resultL = ""
    longL = ""
    line = ""
    #for i in range(len(result)):
     #   if int(result[i]) < 0:
      #      long[i] += 1
    #print(up)
    for i in range(len(up)):
        upL += up[i].rjust(long[i]) + "    "
    #print(upL.rstrip())
    for i in range(len(up)):
        downL += op[i]+ down[i].rjust(long[i] - 1) + "    "
    #print(downL.rstrip())
    for i in range(len(up)):
        line += ("-" * long[i]) + "    "
    #print(line.rstrip())
    for i in range(len(up)):
        resultL += result[i].rjust(long[i]) + "    "
    #print(resultL.rstrip())
    #return [upL.rstrip(), downL.rstrip(), line.rstrip(), resultL.rstrip()]
    return (upL.rstrip() + "\n") + (downL.rstrip() + "\n") +(line.rstrip() + "\n") + resultL.rstrip()


def arithmetic_arranger(*args):
    arr = []
    for arg in args:
        arr.append(arg)
    problems = arr[0]
    if len(problems) > 5:
      return "Error: Too many problems."
    arranged_problems = {}
    up = []
    down = []
    op = []
    result = []
    long = []
    for i in range(len(problems)):
      problem = problems[i].split()
      #print(problem)
      if len(problem[0]) > 4 or len(problem[2]) > 4: # Four Digits
          return "Error: Numbers cannot be more than four digits."
      if not(problem[0].isdigit()) or not(problem[2].isdigit()):
          return "Error: Numbers must only contain digits."
      if not(problem[1] == '+' or problem[1] == '-'): #Operator
          print(problem)        
          return "Error: Operator must be '+' or '-'."
      up.append(problem[0])
      down.append(problem[2])
      op.append(problem[1])
      if op[i] == "+":
          result.append(str(int(up[i]) + int(down[i])))
      else:
          result.append(str(int(up[i]) - int(down[i])))
      if len(up[i]) > len(down[i]):
          long.append(len(up[i]) + 2)
      else:
          long.append(len(down[i]) + 2)
    if len(arr) == 1:
        return magic(up, down, op, result, long)
    return truemagic(up, down, op, result, long)  