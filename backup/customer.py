class Customer:
    def __init__(self, first, last, id, phone, debt, data):
        self._first = first
        self._last = last
        self._id = id
        self._phone = phone
        self._debt = int(debt)
        self._data = data

    @property
    def id(self):
        return self._id

    @property
    def debt(self):
        return self._debt
    
    # @property
    # def first(self):
    #     return self._first

    # @property
    # def last(self):
    #     return self._last
    
    def add_debt(self, debt):
        if type(debt) is not int:
            print("Eerror: debt is not int!")
            return
        self._debt += debt

    def __str__(self):
        return f"name: {self._first} {self._last} id: {self._id}"
    
        
