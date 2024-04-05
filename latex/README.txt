1. Files in the latex directory:

	* python_into_latex.py
	 - This file contains the pyscript that allows
	   the latex files to be generated to work with
	   export. 
	   
	   It's first input will be the name of
	   the file, then it will accept Recipe Name, the
	   Ingredients(Which is a loop that will end when
	   it sees a STOP), the amount of Servings, and the
	   recipe itself, which must be entered as a single
	   input. Then it will ask if it is the last Recipe 
	   to be added to the file, an answer of Y will
	   end the program, anything else will prompt the 
	   entry of another recipe.

           Entry Protocol

	   "File Name"
	   "Recipe Name"
	   "Ingredients" {Loop End with STOP}
	   "Amount of Servings"
	   "Recipe"
	   "Y/N to stop entering of Recipes"{Repeat from File 
	                                     Name unless Y is 
					     entered}

         - Author: Anna Fox & Jesse Johnsen
