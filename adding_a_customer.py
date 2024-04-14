from syntax_check import Tests


def new_customer(customers, new_customer):
    good_customer = True
    new_customer = new_customer[4:]
    values_list = new_customer.split(", ") 

    new_customer_dic = {}
    for val in values_list:
        key, value = val.split("=")
        new_customer_dic[key] = value

    new_id = Tests.check_id(new_customer_dic["id"])
    if not new_id:
        good_customer = False
        new_id = f"Invalid ID: {new_customer_dic["id"]}"
    exists = False
    if len(customers) > 0:
        for customer in customers:
            if customer.id == id:
                exists = True
                if new_customer_dic["first name"] != customer._first:
                    good_customer = False
                    new_first = f"Error, the ID is already associated with: {customer._first}"
                if new_customer_dic["second name"] != customer._last:
                    good_customer = False
                    new_last =  f"Error, the ID is already associated with: {customer._last}"
    if not exists:
        new_first = Tests.check_names(new_customer_dic["first name"])
        if not new_first:
            good_customer = False
            new_first = f"Invalid first name: {new_customer_dic["first name"]}"
        new_last = Tests.check_names(new_customer_dic["second name"])
        if not new_last:
            good_customer = False
            new_last = f"Invalid last name: {new_customer_dic["first name"]}"

    new_phone = Tests.check_phone(new_customer_dic["phone"])
    if not new_phone:
        good_customer = False
        new_phone = f"Invalid phone number: {new_customer_dic["phone"]}"

    new_debt = Tests.check_debt(new_customer_dic["dept"])
    if not new_debt:
        good_customer = False
        new_debt = f"Incorrect debt amount{new_customer_dic["dept"]}"

    new_date = Tests.check_date(new_customer_dic["date"])
    if not new_date:
        good_customer = False
        new_date = f"Invalid date{new_customer_dic["date"]}"
    else:
        new_date = new_customer_dic["date"]

    return  new_first, new_last, new_id, new_phone, new_debt, new_date, good_customer

c = []
if __name__ == "__main__":
    new_customer(c, "set first name=Moshe, second name=Berdichevsky, id=302916440, phone=0544123456, date=3/4/2022, dept=-200")
