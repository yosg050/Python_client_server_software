from datetime import datetime

# def equal_to(x, y):
#     return x == y

# def not_equal_to(x, y):
#     return x != y

# def greater_than(x, y):
#     return x > y

# def less_than(x, y):
#     return x < y

# def select_customers(customers, request):
#     query_characters = " >,<,=,!="
#     category = None
#     given = None
#     request = request[7:]
#     for i in range(len(request)):
#         if request[i] in query_characters:
#             category = request[:i]
#             print(category)
#             query_character = request[1 + i]
#             print(query_character)
#             given = float(request[2 + i:])
#             print(given)
#             break

#     category_dict = {"first_name": lambda customer: customer.first, "last_name": lambda customer: customer.last, "id": lambda customer: customer.id, "phone": lambda customer: customer.phone, "data": lambda customer: customer.data, "dept": lambda customer: customer.dept}
#     comparison = {"=": equal_to, "!=": not_equal_to, ">": greater_than, "<": less_than}

#     if category in category_dict and query_character in comparison:
#         test_func = comparison[query_character]
#         suitable_customers = [customer for customer in customers if test_func(category_dict[category](customer), given)]
#         return suitable_customers
#     else:
#         return []
    

# c = []
# if __name__ == "__main__":
#     select_customers(c,"select debt < 20.5")


def equal_to(customer1, customer2):
    if customer1 == customer2:
        return True
    return False

def not_worth(customer1, customer2):
    if customer1 != customer2:
        return True
    return False

def bigger_than(customer1, customer2):
    if customer1 != customer2:
        return True
    return False

def smaller_than(customer1, customer2):
    if customer1 != customer2:
        return True
    return False

def select_customers(customers, request):
    query_characters = " >,<,=,=!" 
    category = None
    given = None
    request = request[7:]
    for i in range(len(request)):
        if request[i] in query_characters:
            category = request[:i]
            query_characters = request[1 + i]
            given = request[2 + i:]
            break

    category_dic = {"first name": customers.first, "second name": customers.last, "id": customers.id, "phone": customers.phone, "data": customers.data, "dept": customers.dept}
    comparison = {"=": equal_to(), "!=":not_worth(), ">":bigger_than(), "<": smaller_than()}
    test = comparison[query_characters]()
    suitable_customers = []
    for customer in customers:
        test(customer, request)
        if test:
            suitable_customers.append(customer)

    return select_customers


c = []
if __name__ == "__main__":
    select_customers(c,"select debt < 20.5")
