class Order:
    def __init__(self, name, price, isDelivered):
        self.name = name
        self.price = price 
        self.isDelivered = isDelivered

    def isExpensive(self):
        print(self.price >= 1999)
    
    def status(self):
        print(f"{self.name}, Status : ${self.isDelivered}")


order = Order("Iphone", 2000, True)
order.isDelivered()
order.status()