# Write a program to create a class Train which has methods to book ticket , get train status(no of seats available) and get fare information for the same

class Train:
    no_of_seats = 100
    fare_per_seat = 200

    def __init__(self,passengerName,tikcet_quantity):
        self.passengerName = passengerName
        self.ticket_quantity = tikcet_quantity
        self.book_ticket()

    def book_ticket(self):
        if self.ticket_quantity < self.no_of_seats:
            print(f"{self.ticket_quantity} Seats available")
            total_fare = self.get_fare()
            print(f"Total fare of {self.ticket_quantity} is {total_fare}")
            confirm = input("Do you wish to book tikcet? enter y or n :")
            if confirm.lower() == 'y':
                print("Ticket booked successfully")
                self.no_of_seats = self.no_of_seats - self.ticket_quantity
        else:
            print(f"{self.no_of_seats} avaiable only")
            
    def get_fare(self):
        return self.ticket_quantity * self.fare_per_seat

    def get_status(self):
        return self.no_of_seats


name = input("Enter the passenger name:")
quantity = int(input("Enter no of tickets:"))

test = Train(name,quantity)
