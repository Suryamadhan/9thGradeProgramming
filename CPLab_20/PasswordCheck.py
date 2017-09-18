"""
Lab 20.3        Password Check
---------
This is the object class for the Password Check lab.
Unlike most of the other programs we've done, this one
does most of the work in the object class. As you begin
to complete this, you will see why.
"""

class PasswordCheck:
    """Constructor....."""
    def __init__(self):
        self.password = "password"

    """
    check() method: We don't need to pull in parameters.
    Think of a password....
    while loop: runs as long as the variable [password] is
    not equal to your password.
        Create a user input for [password]
        if [password] is not you password....
            print "INVALID--> Please Try Again"
        otherwise..
            print "VALID" and... a message to your user that
            she or he has successfully hacked your password.
    """
    def check(self):
        guesspassword= input('What is the password? ')
        while guesspassword != self.password:
            guesspassword = input ("INVALID--> Please Try Again")
        else:
            print ("You have succefully hacked")

