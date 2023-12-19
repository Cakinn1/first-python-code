
#def __init__ is a magic method

class Point():
    
    # so self is reference its self? basically like .this i believe
    # input1 will be equal to self.x
    # input 2 will be equal to self.y
    def __init__(self, input1, input2):
        self.x = input1
        self.y = input2

# now we are creating a new point and setting the values
p = Point(10, 20)

# p.x will be 10, p.y will be 20
print(p.x, p.y)


#not apart of course jsut me coding ignore
# class Flight():
#     def __init__(self, capicty, passangers):
#         self.cap = capicty
#         self.pas = passangers
    
        


# new_flight = Flight(100, 80)


# if new_flight.pas > new_flight.cap:
#     print('too many passangers!')
# elif new_flight.pas < new_flight.cap:
#     print('nice we have enoughb!')
    

#

class Flight():
    def __init__(self, capacity):
        #capacity set by calling flight class
        self.capacity = capacity
        #empty passenger array list
        self.passengers = []
    
    def add_passengers(self, name):
        # we are basically checking if self.open_seats === 0
        # then there are no seats.
        if not self.open_seats():
            return False
        # add someone new to passengers list
        self.passengers.append(name)
        return True
        
    def open_seats(self):
        # checking the value of capiacity - length of passengers
        # this will tell us if we have enough room for the passengers
        return self.capacity - len(self.passengers)
        
flight = Flight(3)


# create an arary/list of people
people = ['Harry', 'Ron', 'Hermione', 'Ginny']

# for each people in the array
for person in people:
    # we add a person to flight.add__passengers function at the current person
    # we make sure to store this value
    success = flight.add_passengers(person)
    # if truly value (which is determined by which value is returned in add__passenger function)
    if success: 
        # we print the current person added to the flight
        print(f'Added {person} to flight successfully.')
        # else if not successfully in other words if !success
    elif not success:
        #we print out the flght capacity and the current person who cant book
        print(f"not enought people cap is at {flight.capacity}, people who cant book: {person}")
    

        
