class Customer:
    def __init__(self, first, last, id, phone, debt, data):
        self._first = first
        self._last = last
        self._id = id
        self._phone = phone
        self._debt = float(debt)
        self._data = data

    @property
    def id(self):
        return self._id

    @property
    def debt(self):
        return self._debt

    @property
    def first(self):
        return self._first

    @property
    def last(self):
        return self._last

    @property
    def data(self):
        return self._data

    @property
    def phone(self):
        return self._phone

    def add_debt(self, debt, new_data, phone_comparison):
        if type(debt) is not int:
            print("Error: debt is not int!")
            return
        self._debt += debt
        if type(new_data) is str:
            return
        if type(self._data) is str or self._data < new_data:
            self._data = new_data
            if self._phone != phone_comparison:
                self._phone = phone_comparison

    def __str__(self):
        nams = str(self._first) + " " + str(self._last)
        return f"name: {nams:<15} id: {self._id:<15} phone: {self._phone:<14} debt: {self._debt:<5} data: {self._data}"
