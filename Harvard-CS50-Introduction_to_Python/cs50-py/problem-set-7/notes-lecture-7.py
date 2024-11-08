#-----------------------------------------------------------regular expressions---------------------------------------------------------------------------------
#----------------------------------------------
#general

#library re

    #re.search(pattern,string,flags(modify behaviour)) --> search for pattern in string
        #flags usable: re.IGNORECASE = ignore case of users input, re.MULTILINE = search regex over multiple lines, re.DOTALL = . will accept every character also newlines

        #simplifications:
        #re.match(pattern,string,flags(modify behaviour)) --> uses ^ automatically for start of string
        #re.fullmatch(pattern,string,flags(modify behaviour)) --> uses ^ and $ automatically for start and end of string

    #re.sub(pattern, replacement string, string(your input), count=0, flags=0))
        #replace pattern with replacement string on specific input. Count defines how many times we want to do this replacement

    #re.split(pattern, string, maxsplit=0, flags=0)
        #split string on multiple characters

    #re.findall(pattern, string, flags=0)
        #search for multiple copies of same pattern in different places of same string so you can manipulate more than just one


#------------------------------------------------------
#syntax/vocabulary for regex:

    #always operating on the previous character

    # . = any character except a newline
    # * = zero or more repetitions
    # + = one or more repetitions
    # ? = zero or one repetition
    # {m} = m repetitions
    # {m,n} = m-n repetitions
    # ^ = symbolized start of string
    # $ = symbolize end of string
    # [] = look for exactly the symbols in the parantheses (set) --> ranges e.g. [a-z]
    # [^] = complement: symbols in parantheses are not allowed (set) --> ranges e.g. [a-z]
    # ...
    # use \  as escape character before a character to use the originally meaning and a r (raw string) at the beginning of a string, to make sure backslahses are not part of the search pattern --> e.g. (r".+@.+\.edu")
        #best: use raw-strings for all of your regexes



    #some preconfigured patterns usable:
        # \d = decimal digit
        # \D = not a decimal digit
        # \s = whitespace characters (spaces, tabs)
        # \S = not a whitespace character
        # \w = word character, as well as numbers and underscore --> range [a-zA-z0-9] = \w
        # \W = not a word character

    #more syntax:
        # | = or (e.g. (com | net))
        # grouping things by putting them into parantheses and taking whole group into account for used operator--> eg (\w+\.)?

#---------------------------------------------------------------
# further / further functionalities

#keep track of input by using automatons --> regular expression is a valid input to an automaton


# e.g. check for edu-mail regex without dot in username and domain:

    # import re
    #email = input("What's your email?").strip()

    # if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$", email, re.IGNORECASE):
        #print("Valid")
    # else:
        #print("Invalid")

    #--> you could also force the input to all lower/all upper (.lower()/.upper())


#used regex to check for valid e-mail is very long and cryptic --> use libraries

#always use libraries when there is something well know and well defined which needs to be checked, etc., like e-mail

# f-strings can be used in the regex

# we can ask the user to type in a pattern with some functions

#clean up input/format users input (may be wrong input/wrong format)
# when using re (library), grouped things in regular expressions are handed back as return values and can be captured in new variable. If you do not want to include some grouped zhings in matches use (?:...)
    # you can access all return values stored or just some explicit ones using variable.group()
    #e.g.:
        #name = input("What's your name? ").strip()
       # matches = re.search(r"^(.+), *(.+)$", name)     -->could also detail a little more (use ranges [A-Za-z], allow dots, ...)
       # if matches:
       #     name = matches.group(2) + " " + matches.group(1)
      #  print(f"hello, {name}")

            #--> this code can be made more succinct using the walrus operator (:=), which allows to assign a value and check a boolean in one single line:
                # name = input("What's your name? ").strip()
                # if matches := re.search(r"^(.+), *(.+)$", name)
                    # name = matches.group(2) + " " + matches.group(1)
                    # print(f"hello, {name}")

#----------------------------------------------------------------------------------

# for examples look at code script of lecture

