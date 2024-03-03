import sys
import os
from customer import Customer

if len(sys.argv) < 2:
    print("Error missing csv file name!")
    quit()

csv_file = sys.argv[1]
if not os.path.exists(csv_file):
    while open(csv_file, "w"):
        pass

customers = []
with open(csv_file, "r", encoding='utf-8') as fd:
    for line in fd.readlines():
        fields = line.strip().split(",")
        id = fields[2]
        for customer in customers:
            if customer.id == id:
                customer.add_debt(int(fields[4]))
                break
        else:
            customer = Customer(*fields)
            customers.append(customer)

customers.sort(key=lambda customer: customer.debt)
for customer in customers:
    print(customer)

while True:
    query = ("==>")
    if query == "quit":
        print("Bye!")
        break








# customers = []
# with open(csv_file, "r") as fd:
#     for line in fd.readlines():
#         fields = line.split(",")
#         # exists = False
#         index = -1
#         id = int(fields[2])
#         for i, customer in enumerate(customers):
#             if customer.id == id:
#                 index = i
#                 break
#         if index >= 0:
#             customers[index].add_debt(int(fields[4]))
#         else:
#             customer = Customer(*fields)
#             customers.append(customer)

# customers.sort(key=lambda customer: customer.debt)
# for customer in customers:
#     print(customers)

# while True:
#     query = ("==>")
#     if query == "quit":
#         print("Bye!")
#         break
    