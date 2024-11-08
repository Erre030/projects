# Expense Tracker
    #### Video Demo:  https://youtu.be/lfbN_4OAWLs
    #### Description:

The program allows you to track, manipulate and manage your expenses to get an
 extensive and detailed insights on your spendings.
 Firstly, you will be asked for your name. This name will be verified and used
 afterwards to greet you and provide you with the possible options of the program
 gathered in a main menu. For each of the options, there will be a constraint on
 the values you can put in. This is also explained in more detail in the instructions
 as you move through the options.

In the __main menu__, you have the following options:

__create expense__: this option lets you create a new expense. After choosing,
 you are able to specify the amount, category, description and regularity of payment
  of the expense. If you successfully created your expense, it will be stored in
   a list and can be accessed by all other options from then on. After crafting
   an expense, your crafted expense will be printed as conformation of crafting,
   and you will be automatically redirected to the main menu.

__remove expense__: this option will list your expenses with their index numbers,
giving you the chance to remove an expense of your choice. If you chose this
option by accident, you can jump back to the main menu by giving the input „menu“.
If you successfully removed an expense, „expense removed“ will be printed, and you
will be directed back to the main menu.

__list expenses__: this option gives you the ability to list your current expenses
sorted by amount, category or regularity. If you inadvertently chose this option you
can go back to the main menu directly by typing „menu“. Otherwise, your expenses will
be listed, sorted by the parameter of your choice, and you will return to the main menu afterwards.

__sum expenses__: this option gives you the opportunity to sum all your expenses in a
given period of time (daily, weekly, monthly, yearly). The regularity of payment is
factored in according to your choice. After providing your expenses for the chosen time
period, the specific amount for the given time period is displayed, and you are redirected
 to the main menu. You can abort the option by typing in „menu“ to go back to the main menu immediately.

__visualize expenses__: this option assembles graphs, which make it easier to understand
and visually analyze your expenses. The following three graphs will be automatically created
as png-files (if you use this option repeatedly, the current files will be overwritten by the new ones):

	1. Overall amounts for each category
	2. Overall number of expenses for each category
	3. Distribution of expenses by regularity of payment

__export csv__: this option exports all of your current expenses to a csv-file,
so you can display and reuse your data using other programs and applications.
Every time you take this option, new headers will be written to the existing csv-file.
This way, you can separate your current spendings and also access previous versions of exported spendings.

__end program__: this option ends your current state of the program. If you end
your program, all expenses will be lost, so make sure you export them to a csv-file
first and/or create some graphs for specific insights.
