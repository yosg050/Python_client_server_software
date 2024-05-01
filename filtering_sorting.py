from datetime import datetime


category_dic = {
    "first name": "first name",
    "second name": "second name",
    "id": "id",
    "phone": "phone",
    "debt": "debt",
    "date": "date",
}


def select_customers(customers, request):
    print_list = []
    request = request[7:]
    query_characters = ">,<,=,=!"
    query_character = None
    category = None
    given = None
    for i in range(len(request)):
        if request[i] in query_characters:
            category = (request[:i]).strip()
            query_character = (request[i]).strip()
            given = (request[1 + i :]).strip()
            break

    if query_character:
        if category == "date":
            try:
                given = datetime.strptime(given.strip(), "%d/%m/%Y").date()
            except ValueError:
                return False

            if query_character == ">":
                for i in customers:
                    if type(i.date) == str:
                        continue
                    if given > i.date:
                        print_list.append(i)

            if query_character == "<":
                for i in customers:
                    if type(i.date) == str:
                        continue
                    if given < i.date:
                        print_list.append(i)

            if query_character == "=":
                for i in customers:
                    if type(i.date) == str:
                        continue
                    if given == i.date:
                        print_list.append(i)

            if query_character == "=!":
                for i in customers:
                    if type(i.date) == str:
                        continue
                    if given != i.date:
                        print_list.append(i)

        if category == "debt":
            given = float(given)

            if query_character == ">":
                for i in customers:
                    if type(i.date) == str:
                        continue
                    if given > i.debt:
                        print_list.append(i)

            if query_character == "<":
                for i in customers:
                    if type(i.date) == str:
                        continue
                    if given < i.debt:
                        print_list.append(i)

            if query_character == "=":
                for i in customers:
                    if type(i.date) == str:
                        continue
                    if given == i.debt:
                        print_list.append(i)

            if query_character == "=!":
                for i in customers:
                    if type(i.date) == str:
                        continue
                    if given != i.debt:
                        print_list.append(i)

        if category == "first name":

            if query_character == ">":
                for i in customers:
                    if given > i.first:
                        print_list.append(i)

            if query_character == "<":
                for i in customers:
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
    return print_list

