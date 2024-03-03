import sys
import os
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
                    counter += int(id[i])*2
                else:
                    counter += (int(id[i])*2) - 9
            else:
                if (counter + int(id[8]))% 10 != 0:
                    return False
        return True

    def check_names(name):
        if not name.isalpha():
           return False
        name = str(name).capitalize()
        return name
    
    def check_phone(phone):
        if phone[0] != "0" or len(phone) != 10 or not phone.isdigit():
            return False
        return True 

    def check_debt(debt):
        test = debt
        if test[0] == "-":
            test = test[1:]
        if not test.replace(".","",1).isdigit():
            return False
        return True

    def check_data_manual(data):#לא בשימוש
        data = data.split("/")
        day ,month, year = int(data[0]),int(data[1]),int(data[2])
        if month > 12 or 1 > month:
            return False  
        elif  (month == 4) or (month == 6) or (month == 9) or (month == 11):
            if 0 > day or day > 31:
                return False 
        elif (month == 2):
            if ((year %4 == 0) and (year %100 != 0)) or (year %400 == 0):
                if 0 > day or day > 30:
                    return False
            else:
                if 0 > day or day > 29:
                    return False
        if year < 1000:
            if year > 50:
                year += 1900
            else:
                year += 2000

    def check_data(data):
        try:
            data = datetime.strptime(data.strip(), "%d/%m/%Y").date()
        except ValueError:
            return False
        return data

#הכנסה אוטומתית של שם פרטי ומשפחה לפי תז
def first_and_last(id):
    csv_file = sys.argv[1]
    if not os.path.exists(csv_file):
        while open(csv_file, "w"):
            return 
    customers = []
    with open(csv_file, "r", encoding='utf-8') as fd:
        for line in fd.readlines():
            fields = line.strip().split(",")
            id = fields[2]
            for customer in customers:
                if customer.id == id:
                    first = fields[0]
                    last = fields[1]
    return

