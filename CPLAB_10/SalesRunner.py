from AlbumSales import*

def main():
    name = input("Please enter the name of the artist: ")
    album = input("Please enter the name of the album: ")
    units = int(input("Please enter the number of the units sold: "))

    Surya = AlbumSales(name, album, units)
    Surya.categorize()
    Surya = Surya.__str__()
    print(Surya)
main()