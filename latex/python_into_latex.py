title = input("Enter Title: ")

with open('test_output.tex', 'w') as f:
  f.write('\\title{CapyCookin}\n')
  f.write('\\documentclass[a4paper,12pt]{article}\n')
  f.write('\\begin{document}\n')
  f.write('\maketitle\n')
  
  f.write('\\textbf{' + title + '}\\newline\n') 

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


  f.write('\end{document}\n')
