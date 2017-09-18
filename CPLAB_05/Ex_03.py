__author__ = 'Surya'
bigMac = 2.53
lgFry = 1.97
medCoke = 0.99
subtotal = bigMac + lgFry + medCoke
tax = 0.075 * subtotal
total = tax + subtotal

def product():
    total = tax + subtotal
print("BigMac:      "+str(bigMac))
print("lgFry:       "+str(lgFry))
print("medCoke:     "+str(medCoke))
print("subtotal:    "+str(subtotal))
print("tax:   " +"%10.2f"%tax)
print("total: " +"%10.2f"% total)
