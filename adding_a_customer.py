from customer import Customer
from syntax_check import Tests
from copy import deepcopy

def add_id():
    new_id = input("Enter an ID number: ")
    if Tests.check_id(new_id):
        return new_id
    print("Invalid ID")
    return add_id()
    

def add_name(fir_las):
    name = input(f"Enter a {fir_las} name: ")
    name = Tests.check_names(name)
    if name:
        return name
    print("Invalid name")
    return add_name(fir_las)    

def first_and_last(id, customers):
    first = None
    last = None
    if len(customers) > 0:
        for customer in customers:
            if customer.id == id:
                first = deepcopy(customer._first)
                last = deepcopy(customer._last)
                print(first,last)
    if first is None:
        first = add_name("first")
    if last is None:
        last = add_name("last")
    return first, last

def add_phone():
    new_phone = input("Enter a phone number: ")
    if Tests.check_phone(new_phone):
        return new_phone
    print("Invalid phone number")
    return add_phone()

def add_debt():
    new_debt = input("Enter a debt amount: ")
    if Tests.check_debt(new_debt):
        return new_debt
    print("Incorrect debt amount")
    return add_debt()

def add_data():
    new_data = input("Enter a date: ")
    Tests.check_data(new_data)
    if new_data:
        return new_data
    print("Invalid date")
    return add_data()
 

def new_customer(customers):
        id = add_id()
        first, last = first_and_last(id, customers)
        phone = add_phone()
        debt = add_debt()
        data = add_data()
        # customer =  Customer(first, last, id, phone, debt, data)
        customer = [first, last, id, phone, debt, data]
        return customer

c = []
if __name__ == "__main__":
    new_customer(c)