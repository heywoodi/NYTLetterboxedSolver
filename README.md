# NYTLetterboxedSolver
A program that solves the NYT letterboxed puzzle
Add todays letters to the LETTERS variable on line 7, or leave it blank to input letters from the command line

Code is split into 5 functions; one to retrive the dictionary from json, one to remove invalid words, one to check if a word solves in one, one to check if a word solves in two, and one main method to run them all.

dict.json is a combined dictionary from several sources, and not the same as the dictionary used by NYT. words will often appear as "not a word" when inputted to the puzzle. 
