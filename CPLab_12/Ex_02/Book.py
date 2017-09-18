class Book:
    def __init__(self, n, txt):
        self.name = n
        self.text = txt

    def getName(self):
        return self.name
    def getText(self):
        return self.text

    def __str__(self):
        return "Name: " +  self.getName() + "\n" + "Text: " + self.getText()

    """
    Accessor: return name
    """


    """ __str__(): return Title and text
    """
