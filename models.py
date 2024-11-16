class Client:
    def __init__(self, name , gender, phone, address):
        self.name = name
        self.gender = gender 
        self.phone = phone
        self.address = address

    def serialize(self):
        return {
            'name':self.name,
            'gender':self.gender,
            'phone' : self.phone,
            'address': self.address,

        }
        