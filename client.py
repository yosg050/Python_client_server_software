

def printed(list_cus):
    list_cus.sort(key=lambda customer: customer.debt)
    for customer in list_cus:
        print(customer)