class Seat:
    def __init__(self,free = True,occupant=""):
        '''Here, we have initialized the seat as free.
        If some occupant is provided, is will be marked
        as occupied
        :param free- Will show if the seat is free
        :param occupant-Will show the person assigned'''
        self.free = free
        self.occupant = str(occupant)
        if self.occupant != "": # condition to check if someone is assigned to the seat
           
            self.free = False #If true, setting it as not free

    def set_occupant(self,name):
        '''This will assign the occupant, a seat,if free,
        else it will return that the seat is already occupied
        :param name-It is the person who is going to be assigned'''
        if self.free:
            self.occupant = name
            self.free = False   # Once name is assigned, seat is being set as not free
            print("The seat is taken by",name) #Printing the name of the occupant
        else:
            print("The seat is already taken by", self.occupant)

        
        
    def remove_occupant(self):
        '''This function will remove the occupant and will
        display the removed occupant.If the seat was already free
        it will return None
        last person is returned, if removed'''
        if not self.free:
            last_person= self.occupant
            self.occupant = "" # Makes the occupant empty
            self.free= True    # Marks the seat as free
            return last_person # Returns the person name who was removed
        return None

        
        
class Table:
    def __init__(self,capacity:int):
        self.capacity = capacity
        self.seats = [Seat(True,"") for _ in range(capacity)]
       

    def has_free_spot(self):
        '''This function will return true if there
         is atleast 1 seat available,else will 
         return false'''
         
        for seat in self.seats:  # Checks whether a seat is available by running the loop
         if seat.free:
          return True
        return False
 
       
     
    def assign_seat(self,name):
      '''This function is going to assign a person to a free seat
      and the seat will be occupied, it will print
      that no place is available'''
      for seat in self.seats:
          if seat.free:
           seat.set_occupant(name) #If the seat is free, call the function and assign the seat
           return True
          
      print("No place available")
      return False
      
       
    def left_capacity(self):
       '''This function calculates the number of seats
       available on a table.It will increase the count if the seat 
        is free '''
       count = 0               # Setting the count to 0
       for seat in self.seats: 
         if seat.free:         # Checking the condition if a seat is free
            count +=1          #If free, its increasing the count
       return count
    
