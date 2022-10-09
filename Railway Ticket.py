class Railway :
    train_Name = 'Howrah-Chakradharpur'
    # list of all seats.
    seat = [x for x in range (1,1001)]
    
    def __init__ (self, name, b_station, d_station) :
        self.name = name            # Passenger Name
        self.b_station = b_station  # Boarding Station Name
        self.d_station = d_station  # Destination Station Name
        self.seat_no = 0

    def info(self):
        print (f'Passenger Name - {self.name}.')
        print (f'Boarding Station  - {self.b_station}.')
        print (f'Destination Station - {self.d_station}.')
        print (f'Train Name - {self.train_Name}.')
    
    def book_seat(self):           # This is a Seat Booking Function
        if len(Railway.seat) >= 1 :
            self.seat_no = Railway.seat[0]
            del Railway.seat[0]
            print (f'Your Seat No. is {self.seat_no}.')
            print ()
        else :
            print ('Sorry! All seats are booked.')
        
    
    def book_ticket (self):  # This is Ticket Booking Function
        self.info()
        self.book_seat()
       
    def cancel_ticket(self):
        Railway.seat.append (self.seat_no)
        Railway.seat = sorted (Railway.seat)
        print ('Your Ticket has been cancelled.')
        print (f'Seat No. {self.seat_no} is now available to book.')
        
p1 = Railway('Bishal Kar', 'Kolkata', 'Bankura')
p2 = Railway('Rahul Halder', 'Purulia', 'Bankura')
p1.book_ticket()
p2.book_ticket()

p2.cancel_ticket()

 
