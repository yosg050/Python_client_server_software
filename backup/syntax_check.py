# class Syntax_check:
def check_id(id):
    if len(id) != 9:
        return False, "3"
    counter = 0
    # for i in id:
    #     if not i.isdigit():
    #         return False, "4"
    for i in range(len(id)):
        if not id[i].isdigit():
            return False
        if i % 2 == 0 and i < 8:
            counter += int(id[i])
        elif i % 2 == 1:
            if int(id[i]) < 5:
                counter += int(id[i])*2
            else:
                counter += (int(id[i])*2) - 9
        else:
            if (counter + int(id[8]))% 10 != 0:
                return False, "5"
    return True
    
v = ("240327601")
s = check_id(v)
print(s)

