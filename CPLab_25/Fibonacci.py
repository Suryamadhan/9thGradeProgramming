"""===============================================================
Lab_24.1        Fibonacci Sequence
---------
This will be the object class for the Fibonacci Sequence lab
================================================================"""

class Fibonacci:
    """Constructor..."""
    def __init__(self, size):
        self.list = []
        self.setFibo(size)

    def setFibo(self, size):
        if size == 1:
            self.list.append(1)
        elif size == 2:
            self.list.append(1)
            self.list.append(1)
        else:
            self.list.append(1)
            self.list.append(1)

            for i in range(2, size):
                self.list.append(self.list[i-1]+self.list[i-2])

    """============== setFibo(self, size) ==================
    if size is equal to 1
        add the number 1 to list @ 0
    if size is equal to 2
        add the number 1 to list @ 0
        add the number 1 to list @ 1
    otherwise...
        add the number 1 to list @ 0
        add the number 1 to list @ 1

        for loop from 2 to size...
            add the sum of the previous 2 numbers to
            the end of list
    ================================================"""
    def getFibo(self, num):
        if int(num) - 1 < int(len(self.list)):
            return str(self.list[int(num) -1])
        else:
            return "-1"

    """============== getFibo(self, num) ============================
    if num-1 is less than the length of list...
        return list @ num - 1
    otherwise return - 1
    ============================================"""

    """ __str__() function"""
    def __str__(self):
        output = ""
        for i in range(1, len(self.list)):
            output += str(i) + " - " + str(self.list[i]) + "\n"
        return output

