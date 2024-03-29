#!/usr/bin/env python
import sys, os, os.path
filename = sys.argv[1]
opfile = sys.argv[1] + '.tex'
outfile = open(opfile, 'w')
pageAry = []
def a_tex_file(title):
    global pageAry
#    pageAry.append('\\begin{document}')
    pageAry.append('\\begin{center}\n')
    pageAry.append('\\{LARGE CapyCookin}\n')
    pageAry.append('\\end{center}\n')
#	\\bigskip\\begin{recipe}{Title} {Number of servings} {Preparation time}\\end{recipe}\n')
    return 1

a_tex_file("blunk")

for i in pageAry:
    outfile.writelines(i)
outfile.close()
os.system('tex '+ opfile)
os.system('xdvi ' + filename + '.dvi & ')

