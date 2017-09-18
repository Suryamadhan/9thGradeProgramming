"""
==================================================
Lab_24.1        Roman Numeral Converter
---------
Object class for the Roman Numeral Converter lab
===================================================
"""
class RomanNumeral:
    def __init__(self, rom="", num=0):
        self.number = num
        self.roman = rom
        self.result = ""
        self.numbers = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        self.letters = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

        if self.number == 0:
            self.setRoman()
        else:
            self.setNumber()

    def setNumber(self):
        num = self.number
        for i in range(0,len(self.numbers)):
            while num >= self.numbers[i]:
                self.roman += self.letters[i]
                num -= self.numbers[i]
        self.result = "The Roman numeral for " + str(self.number) + " is " + self.roman

    def setRoman(self):
        rom = self.roman
        for i in range(0,len(self.letters)):
            while rom.find(self.letters[i]) == 0:
                self.number += self.numbers[i]
                rom = rom[len(self.letters[i]):]
        self.result = "The Decimal number for " + self.roman + " is " + str(self.number)





    def __str__(self):
        return self.result




"""
    =============== Constructor =======================
    <input parameters - rom = "" and num = 0
        Variable [number] = num
        Variable [roman] = rom
        Variable [result] = ""
        Array NUMBERS = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        Array LETTERS = ["M","CM","D","CD","C","XC", "L","XL","X","IX","V","IV","I"]

        <if statement based on inputs>
        if [number] remains 0
            run setRoman()
        otherwise...
            run setNumber()
    ============================================================
    """
"""
    ====================== setNumber() ============================
        New variable [num] = [number]
        for loop: from 0 to the length of NUMBERS
            while loop: runs as long as [num] >= NUMBERS @ i
                add LETTERS @ i to [roman]
                subtract NUMBERS @ i from [num]
        Set result to....
        "The Roman numeral for [number] is [roman]
    ================================================================
    """

"""
    ========================== setRoman() ==========================================
        New variable [rom] = [roman]
        for loop: from 0 to the length of LETTERS
            while loop: runs as long as LETTERS @ i is found at index 0
            in [rom]. Hint: use the find() function for Strings <<<<Google Search>>>
                add NUMBERS @ i to [number]
                set [rom] = slice of [rom] from length of LETTERS @ i to end of [rom]
        set [result] to.....
        "The Decimal number for [roman] is [number]
    ================================================================================
    """


"""
    ======================== str() function ===============================
    return result
    =======================================================================
    """
