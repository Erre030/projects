
#definition: create a class with specific functions given in the exercise

class Jar:

    #initialize class and its instance variables
    def __init__(self, capacity=12):
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError("Use a valid capacity")
        self._capacity = capacity
        self._cookies = 0


    #returns as many cookie emojies as in the jar
    def __str__(self):
        cookie = "\U0001F36A"
        n = self._cookies
        return cookie * n

    #value error if deposit exceeds jar capacity (add cookies to jar)
    def deposit(self, n):
        if (self._cookies + n) > self._capacity:
            raise ValueError("Exceeded capacity")

        else:
            self._cookies += n


    #value error if withdraw exceeds cookie amount in jar (remove cookies from jar)
    def withdraw(self, n):
        if n > self._cookies:
            raise ValueError("Not that many cookies in jar")

        else:
            self._cookies -= n

    #return jar capacity
    @property
    def capacity(self):
        return self._capacity   #use _, so function do not get confused and produces infinite loop

    #return cookies in jar
    @property
    def size(self):
        return self._cookies    #done for similarity because of function above

