from datetime import datetime

print_list = []

category_dic = {
    "first name": "first name",
    "second name": "second name",
    "id": "id",
    "phone": "phone",
    "debt": "debt",
    "date": "date",
}


def select_customers(customers, request):
    request = request[7:]
    query_characters = ">,<,=,=!"
    query_character = None
    category = None
    given = None
    for i in range(len(request)):
        if request[i] in query_characters:
            category = (request[:i]).strip()
            print(category)
            query_character = (request[i]).strip()
            print(query_character)
            given = (request[1 + i :]).strip()
            print(given)
            break

    if query_character:
        if category == "date":
            try:
                given = datetime.strptime(given.strip(), "%d/%m/%Y").date()
                print(given)
            except ValueError:
                return False

            if query_character == ">":
                for i in customers:
                    if given > i.date:
                        print_list.append(i)

            if query_character == "<":
                for i in customers:
                    if given < i.date:
                        print_list.append(i)

            if query_character == "=":
                for i in customers:
                    if given == i.date:
                        print_list.append(i)

            if query_character == "=!":
                for i in customers:
                    if given != i.date:
                        print_list.append(i)


        if category == "debt":
            given = float(given)

            if query_character == ">":
                for i in customers:
                    if given > i.debt:
                        print_list.append(i)

            if query_character == "<":
                for i in customers:
                    print(i.date)
                    if given < i.debt:
                        print_list.append(i)

            if query_character == "=":
                for i in customers:
                    if given == i.debt:
                        print_list.append(i)

            if query_character == "=!":
                for i in customers:
                    if given != i.debt:
                        print_list.append(i)


        if category == "first name":

            if query_character == ">":
                for i in customers:
                    if given > i.first:
                        print_list.append(i)

            if query_character == "<":
                for i in customers:
                    print(i.date)
                    if given < i.first:
                        print_list.append(i)

            if query_character == "=":
                for i in customers:
                    if given == i.first:
                        print_list.append(i)

            if query_character == "=!":
                for i in customers:
                    if given != i.first:
                        print_list.append(i)


        if category == "second name":

            if query_character == ">":
                for i in customers:
                    if given > i.last:
                        print_list.append(i)

            if query_character == "<":
                for i in customers:
                    print(i.date)
                    if given < i.last:
                        print_list.append(i)

            if query_character == "=":
                for i in customers:
                    if given == i.last:
                        print_list.append(i)

            if query_character == "=!":
                for i in customers:
                    if given != i.last:
                        print_list.append(i)


        if category == "phone":

            if query_character == ">":
                for i in customers:
                    if given > i.phone:
                        print_list.append(i)

            if query_character == "<":
                for i in customers:
                    print(i.date)
                    if given < i.phone:
                        print_list.append(i)

            if query_character == "=":
                for i in customers:
                    if given == i.phone:
                        print_list.append(i)

            if query_character == "=!":
                for i in customers:
                    if given != i.phone:
                        print_list.append(i)


            if category == "id":

                if query_character == ">":
                    for i in customers:
                        if given > i.id:
                            print_list.append(i)

                if query_character == "<":
                    for i in customers:
                        print(i.date)
                        if given < i.id:
                            print_list.append(i)

                if query_character == "=":
                    for i in customers:
                        if given == i.id:
                            print_list.append(i)

                if query_character == "=!":
                    for i in customers:
                        if given != i.id:
                            print_list.append(i)
        print(print_list)

    # return select_customers


c = [
    ["yosef", "levi", "302916440", "0548443278", "123", "05/01/2017"],
    ["Yosef", "Gelle", "302916440", "0444444444", "-1999", "15/11/1999"],
    ["'Yosef'", "Fwef", "302916440", "0333333333", "-1", "01/01/2000"],
    ["Yosef", "Geller", "302916440", "0444444444", "-100", "11/11/2011"],
    ["Esti", "Geller", "203225750", "0503233222", "-222", "19/09/2021"],
    ["Svi", "Geller", "224249268", "0545454543", "-424", "11/01/2019"],
]

if __name__ == "__main__":
    x = input()
    y = input()
    z = input()
    select_customers(c, f"select {x} {y} {z}")
