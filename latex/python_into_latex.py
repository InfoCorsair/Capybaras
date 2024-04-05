endDocument = 0;
fileName = input("Enter file name: ")
path = "latex_output/" + fileName + ".tex"
with open(path, 'w') as f:
  f.write('\\documentclass[a4paper,12pt]{article}\n')
  f.write('\\begin{document}\n')
  f.write('\\title{\LARGE CapyCookin}\n')

  f.write('\\maketitle\n')
  while(endDocument == 0):
    title = input("Enter Title: ")

    f.write('\\begin{center}\n')
    f.write('\\textbf{' + title + '}\\newline\n') 
    f.write('\\end{center}\n')

    ingredient = ""
    while (1):
      ingredient = input("Ingredient: ")
      if ingredient == 'STOP':
        break
      f.write('\\textbf{' + ingredient + '}\\newline\n')


    servings = input("Enter number of servings: ")
    f.write('\\textbf{' + servings + '}\\newline\n')

    recipe = input("Enter your recipe: ")
    f.write('\\textbf{' + recipe + '}\\newline\n')
    f.write('\\newline\n')

    finish = input("Final Recipe? Y/N: ")
    if finish == "Y":
      endDocument = 1
    else:
      endDocument = 0

  

  f.write('\end{document}\n')
