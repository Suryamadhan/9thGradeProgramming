class AlbumSales:
    def __init__(self, n= "Not Found", alb = "Not Found", uts=0):
        self.name = n
        self.album = alb
        self.units = uts
        self.category = "Not Found"

    def categorize(self):

        if self.units >= 1000000:
            self.category = "Top Seller"

        elif self.units >= 500000:
            self.category = "Good Seller"

        elif self.units >= 100000:
            self.category = "Average Seller"

        else:
            self.category = "Needs Review"

    def getName(self):
        return self.name

    def getAlbum(self):
        return self.album

    def getUnits(self):
        return self.units

    def getCat(self):
        return self.category

    def __str__(self):
        return "<<<<  ALBUM INFORMATION  >>>>" \
            "\nArtist:\t\t\t" + self.name +"\n" \
            "Album:\t\t\t" + self.album + "\n" \
            "Units Sold:\t\t" + str(self.units)+"\n" \
            "Category:\t\t" + self.category

