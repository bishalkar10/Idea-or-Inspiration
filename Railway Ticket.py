class Railway :
    train_Name = 'Howrah-Chakradharpur'
    # list of all seats. this list is sorted so we can append canceled tickets seat no. 
    seat = sorted([x for x in range (1,1001)])
    
    def __init__ (self, name, b_station, d_station) :
        self.name = name            # Passenger Name
        self.b_station = b_station  # Boarding Station Name
        self.d_station = d_station  # Destination Station Name
        
    def info(self):
        print (f'Passenger Name - {self.name}.')
        print (f'Boarding Station  - {self.b_station}.')
        print (f'Destination Station - {self.d_station}.')
        print (f'Train Name - {self.train_Name}.')
    
    def book_seat(self):           # This is a Seat Booking Function
        if len(self.seat) >= 1 :
            seat_no = self.seat[0]  # I am unable to access this 'Seat_no variable from anywhere else.'
            del self.seat[0]
            print (f'Your Seat No. is {seat_no}.')
            print ()
        else :
            print ('Sorry! All seats are booked.')
        
    
    def book_ticket (self):  # This is Ticket Booking Function
        self.info()
        self.book_seat()
       
    def cancel_ticket(self):      # I am trying to Implement Ticket Canceling Function
        self.seat.append (self.seat_no)

p1 = Railway('Bishal Kar', 'Kolkata', 'Bankura')
p2 = Railway('Rahul Halder', 'Purulia', 'Bankura')
p1.book_ticket()
p2.book_ticket()

# I am trying to implement ticket Canceling Function.But not not able to implement it.
# p2.cancel_ticket()

# print (Railway.seat)
       