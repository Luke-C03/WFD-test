class House:
    def __init__(self, house_number, street, area, no_of_beds, price):

        self.house_number = house_number
        self.street = street
        self.area = area
        self.no_of_beds = no_of_beds
        self.price = price

    def house_Info(self):
        
         print("House Info: ")
         print("The House Number is: ", self.house_number)
         print("The Street is: ", self.street)
         print("The Area is: ", self.area)
         print("The Number of Beds is: ", self.no_of_beds)
         print("The price is: ", self.price)
    
    def update_house_number (self, new_house_number: str):

        self.house_number = new_house_number

    def update_street (self, new_street: str):

        self.street = new_street

    def update_area (self, new_area: str):

        self.area = new_area

    def update_no_of_beds (self, new_no_of_beds: str):

        self.no_of_beds = new_no_of_beds

    def update_price (self, new_price: str):

        self.price = new_price

class Apartment(House):

    def __init__(self, house_number, street, area, no_of_beds, price):
        super().__init__(street, area, price)

        self.floors = street
        self.garden = area
        self.driveway = price

    def extra_details(self):
        self.house_Info()

        print("Extra Details")
        print("The Street is", self.street)
        print("The Area is", self.area)
        print("The Rent is ", self.price)


h1 = House(22,'main street','Rathcoole',3,400000)
h1.house_Info()    