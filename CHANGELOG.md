# CHANGELOG

	## v1.0.2 

		### REFACTORS
		1. moving code into src folder!

	## v1.0.1 

		### NEW
		1. add the dir to start from

	## v1.0.0 

		### NEW
		1. add a setup.py

	## v0.1.1 

		### REFACTORS
		1. __init__ to __main__ so it can be called as a module!

	## v0.1.0 

		### NEW
		1. added the requirements; update: gitignore to ignore pretty printing package - this is in it's own repo;
		1. ProfileColumn file which is an extract of the logic from __init__ from previous version
		1. ability to call values with class.flag_name
		1. conditionally branching based on dtype which functions are run on the data
		1. helper functions to work out top k categories and imbalenced distributions
		1. adding standard stats and conditional stats
		1. default flags
		1. value errors
		### UPDATES
		1. removing anthoer library which is another repo
		1. adding simple testing for this stage in the project
		1. comment out the print which was unnecessarily triggering
		1. tweaks to match the new implimentation
		### REFACTORS
		1. code out of the main path into it's own file and function
		### DELETES
		1. module2 as this is now a named import and being used
		### MISC
		1. Update LICENSE