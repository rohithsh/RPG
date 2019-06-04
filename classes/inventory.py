class items:
    def __init__(self, name, type, desc, value, qty):
        self.name = name
        self.type = type
        self.desc = desc
        self.value = value
        self.qty = qty

    def use_item(self, no):
        self.qty -= no
        return self.qty


