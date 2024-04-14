from datetime import datetime

class Tests:
    def check_id(id):
        if len(id) > 9:
            return False
        id = str(id).zfill(9)
        counter = 0
        if not id.isdigit():
            return False
        for i in range(len(id)):
            if i % 2 == 0 and i < 8:
                counter += int(id[i])
            elif i % 2 == 1:
                if int(id[i]) < 5:
                    counter += int(id[i]) * 2
                else:
                    counter += (int(id[i]) * 2) - 9
            else:
                if (counter + int(id[8])) % 10 != 0:
                    return False
        return id

    def check_names(name):
        if not name.isalpha():
            return False
        name = str(name).capitalize()
        return name

    def check_phone(phone):
        if phone[0] != "0" or len(phone) != 10 or not phone.isdigit():
            return False
        return phone

    def check_debt(debt):
        test = debt
        if test[0] == "-":
            test = test[1:]
        if not test.replace(".", "", 1).isdigit():
            return False
        return debt

    def check_date(date):
        try:
            date = datetime.strptime(date.strip(), "%d/%m/%Y").date()
        except ValueError:
            return False
        return date
