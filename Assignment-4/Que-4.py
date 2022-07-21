class Vehicle:

    def __init__(self):
        self.__maxprice = 900000

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price

c = Vehicle()
c.sell()

c.__maxprice = 1500000
c.sell()
c.setMaxPrice(1500000)
c.sell()