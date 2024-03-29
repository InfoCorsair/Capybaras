title = input("Enter Title: ")



with open('test_output.tex', 'w') as f:
  f.write('\\title{CapyCookin}\n')
  f.write('\\begin{center}\n')
  f.write('\maketitle\n')
  
  f.write('\\textbf{' + title + '}\n') 

  ingredient = ""
  while (1):
    ingredient = input("Ingredient: ")
    if ingredient == 'STOP':
      break
    f.write('\\textbf{' + ingredient + '}\n')


  servings = input("Enter number of servings: ")
  f.write('\\textbf{' + servings + '}\n')

  recipe = input("Enter your recipe: ")
  f.write('\\textbf{' + recipe + '}\n')


  f.write('\end{center}\n')
