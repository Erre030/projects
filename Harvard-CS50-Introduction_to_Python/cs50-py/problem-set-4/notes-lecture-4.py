#------------------------------------------------libraries----------------------------------

#libraries are modules which encompass specific functions, methods, variables, constants, variables --> code in general
#keywords needed: import ... --> imports whole library // from ... import --> imports just some parts of library

#e.g. usage:
        #import random , random.choice(["heads","tails"]) --> random choice of heads or tails out of list (a function which is inside of a library is an attribute of this library and doesn't become a method once imported)
            #if you have multiple functions/methods with name "choice", they do not collide
        #from random import choice , choice(["head","tails"]) --> random choce of heads or tails out of list (if single parts imported, they can be used solely by their name (loaded into local name space/vocabulary))
            #if you use the choice method in many places and you have no own function named choice, it is quicker to write just choice

#-----------------------------------------------------------------------
#example libraries:
	#random.randint(a,b) --> int between a and b (inclusive)
	#random.shuffle(x) --> randomize item x inplace (no seperate output, item is directly edited --> e.g. list
	#statistics --> mean,etc.

#-------------------------------------------------------------------------
#cmd-arguments: using sys library to get access to cmd-line --> less user-friendly but more efficient for coders/people with knowledge in domain --> faster workflow (no need to code and answer questions for everything)
	#sys.argv: list which contains all inputs typed into the cmd-line after the prompt which runs the program
		#e.g. program: import sys, print("Hello", sys.argv[1]) // cmd-input: python name.py David ---> leads to output: Hello David

		#sys.argv[0] --> displays program name

		#to avoid IndexError (out of the list/element index) --> use try/except block or conditionals (conditionals prevent errorsin the  first place)

		#sys.exit("message displayed") --> exits program prematurely, if we do not receive the right input

		#example for functions above: (it is better design to seperate your "main"-program and your conditions for allowed input--> but you can also use it inside if/elif/else)
			#import sys
			#if len(sys.argv) < 2:
				#sys.exit("Too few arguments")
			#elif len(sys.argv) > 2:
				#sys.exit("Too many arguments")

			#print("Hello my name is", sys.argv[1])

				#--> generates output if the right amount of sys.argv-inputs is met

#------------------------------------------------------------------
#slice [start:end]
	#subset of datastructure (e.g. list)
		# -->e.g. list-name[start-index:end-index]
			# --> if the end is the current end of list, number can be omitted
			# --> you can also use negative values to determine the element till where you want to go from the current end of the list, e.g. [1:-3] (--> only temporarily saved if not assigned to variable)

#-------------------------------------------
#packages
	#third party libraries developed by other users which are not in python by default -->(good source: PyPI-website: pypi.org)
		#use paket manager to download packages (pip-program) --> pip install ... --> afterward you can use the packages by import .../from ... import ...

#-------------------------------------------------
#APIs (intersection between own program and other "service/program")
	#write code pretends to be a browser, connects to third party API on a server and downloads some data you can then incorporate into your program
	#libraries:
		#requests (make web-requests) (package) --> using json-format


#--------------------------------------------
#JSON
	#used to transfer data between computers --> information stored and transfered in textfile
	#often consists of lists and dictionaries
	#json --> integrated library in python for json-fomrat to handle it better, e.g. pretty print, ...





#e.g. use case for APIs using json: --> search songs of wheezer with itunes-APIs


#1. inspect available data-----------------------------------------------


# Demonstrates json(get a better overview about data contained in json by pretty printing it)

#	import json
#	import sys
#	import requests
#
#	if len(sys.argv) != 2:
 #   	sys.exit()
#
#	response = requests.get( 				#--> get data from specific API-URL
 #   	"https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1] (--> search parameter = sys.argv[1])
#	)
#	print(json.dumps(response.json(), indent=2))  					#(-->show the response in json-format, pretty printed, where every entry is indented by 2)


	#-->pre-step for number 2, to get overview over data in the json-file (delete afterwards/comment out)


#2. provide wanted answer-----------------------------------------

	# Demonstrates iterating over JSON

#	import json
#	import sys
#	import requests
#
#	if len(sys.argv) != 2:
 #   	sys.exit()
#
#	response = requests.get(			#--> get data from specific API-URL
 #   	"https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1]
#	)
#	o = response.json()
#	for result in o["results"]: 		#(--> use given parameters from API-URL)
 #   	print(result["trackName"])


	#--> output: 50 songs of search-term (sys.argv[1])









#1:09:30
