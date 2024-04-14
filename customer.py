class Customer:
    def __init__(self, first, last, id, phone, debt, date):
        self._first = first
        self._last = last
        self._id = id
        self._phone = phone
        self._debt = float(debt)
        self._date = date

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
    def date(self):
        return self._date

    @property
    def phone(self):
        return self._phone

    def add_debt(self, debt, new_date, phone_comparison):
        if type(debt) is not int:
            print("Error: debt is not int!")
            return
        self._debt += debt
        if type(new_date) is str:
            return
        if type(self._date) is str or self._date < new_date:
            self._date = new_date
            if self._phone != phone_comparison:
                self._phone = phone_comparison

    def __str__(self):
        nams = str(self._first) + " " + str(self._last)
        return f"name: {nams:<15} id: {self._id:<15} phone: {self._phone:<14} debt: {self._debt:<5} date: {self._date}"
