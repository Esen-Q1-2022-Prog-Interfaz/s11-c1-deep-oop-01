from client import Client, Product

# balbino 2 años  100 por año

Client.yearCost = 100
Client.addYearCost()

clientdb = []

"""
clientdb.append(Client("balbino", 23, "bal@test.com", 2).display())
clientdb.append(Client("rodrigo", 24, "rod@test.com", 1).display())
clientdb.append(Client("gaby", 25, "gaby@test.com", 3).display())
clientdb.append(Client("carlos", 28, "carlos@test.com", 5).display())
"""

clientdb.append(Client("balbino", 23, "bal@test.com", 2))
clientdb.append(Client("rodrigo", 24, "rod@test.com", 1))
clientdb.append(Client("gaby", 25, "gaby@test.com", 3))
clientdb.append(Client("carlos", 28, "carlos@test.com", 5))

print(clientdb)

for client in clientdb:
    client.display()
    print(client.getRetirement())
