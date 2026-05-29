from random import shuffle
from utils.table import Table,Seat
class Openspace():
    def __init__(self,tables:int,table_num:int):
        self.num_of_tables = tables
        self.tables=[Table(table_num) for _ in range(tables)]

    def organize(self,names):
        '''This function will perform the shuffling of the people 
        and randomly assign them across the table,
        if there is no free space, the person will be unassigned'''
        name_list= names.copy()
        shuffle(name_list)
        for name in name_list:
            assigned=False
            for table in self.tables:
                if table.has_free_spot():
                   table.assign_seat(name)
                   assigned=True
                   break
            if not assigned:
                print(name,"could not be assigned a table") 

    def display(self):
        '''This function will display seating for all the tables
           and will let you know if the seat is free or
           is it assigned to someone.If its assigned to someone, 
           it will display the name of the person'''
        for i , table in enumerate(self.tables, start = 1):
            print(f"Table{i}:")
            for seat in table.seats:
                if seat.free:
                    print(" - Free")
                else:
                    print(f"- {seat.occupant}")

    def store(self,filename:str):
        '''This function will write the arrangement
        in a .txt file showing all the tables and the seats
        and would display in the file if the seat is free
        or assigned(name will display)'''
        with open(filename, 'w')as f:
            for i, table in enumerate(self.tables, start=1):
                f.write(f"Table{i}:\n")
                for seat in table.seats:
                    if seat.free:
                        f.write(" - Free\n")
                    else:
                        f.write(f" - {seat.occupant}\n")
