from datetime import datetime
from customer import Customer

def select_customers(customers, request):
    query_characters = " >,<,=,=!" 
    category = None
    given = None
    request = request[7:]
    for i in range(len(request)):
        if request[i] in query_characters:
            category = request[:i]
            query_characters = request[i]
            given = request[1 + i:]
            break
    if query_characters == "=":
        query_characters = "==" 

    category_dic = {"first name": customers.first, "second name": customers.last, "id": customers.id, "phone": customers.phone, "data": customers.data, "dept": customers.dept}
    suitable_customers = []
    for customer in customers:
        pass

