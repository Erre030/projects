
#description: transform a date given in specific format to "spoken" numbers.

from datetime import date
import sys
import re
import inflect      #to transform numerical out put into "spoken" output --> 430 = four hundred thirty

def main():
    phrase = age_minutes(input("Date of Birth: "))

    print(phrase)

















def age_minutes(s):
    if not re.search(r"^\d{1,4}-\d{1,2}-\d{1,2}$", s):
        sys.exit("Invalid date")


    given_date = date.fromisoformat(s)  #formats input yyyy-mm-dd correctly and produces object of date class (class encompassed in datetime library) using methods of date class

    date_today = date.today()       #create object of date class with date of today

    date_difference = date_today - given_date       #automatically creates new object of class timedelta (rule for creation of class and class itself encompassed in datetime library), which encompasses period alive since birth

    minutes_difference = date_difference.total_seconds() / 60       #get minute difference

    eng = inflect.engine()              #make instance of engine class to use its methods(contents) / methods inside of engine class inside the module inflect (module = .py file with code, library = encompasses one or multiple modules)
    phrase = eng.number_to_words(int(minutes_difference))           #phrase number to spoken words

    phrase = phrase.capitalize()
    result = re.sub(r'\band \b', "", phrase)      # removes all "and" and their whitespaces in output

    return (f"{result} minutes")


if __name__ == "__main__":
    main()
