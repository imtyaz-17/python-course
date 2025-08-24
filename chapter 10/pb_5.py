class Train:
    def __init__ (self, train_no, start, destination):
        self.train_no = train_no
        self.start = start
        self.destination = destination

    def book_ticket (self, passenger_name):
        print("Ticket booked successfully for", passenger_name, "from", self.start, "to", self.destination, "in train number", self.train_no)
    def getStatus (self):
        print("Train number", self.train_no, "is running on time from", self.start, "to", self.destination)
    def getFare (self):
        print("The fare for the journey from", self.start, "to", self.destination, "in train number", self.train_no, "is $50")

obj = Train(12345, "New York", "Washington D.C.")
obj.book_ticket("Alice")
obj.getStatus()
obj.getFare()

