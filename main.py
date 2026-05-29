from utils.openspace import Openspace
from utils.table import Table
import utils
from utils.read_file import read_names_from_txt

def main():

    input_filepath = ".\\new_colleagues.txt"
    output_filename = "output.txt"

    # Creates a list that contains all the colleagues names
    names_list = read_names_from_txt(input_filepath)

    # create an OpenSpace()
    tables_input = input("Enter the number of table")
    tables = int(tables_input)
    tables_cap = input("Please enter the number of capacity on each table")
    table_num=int(tables_cap)
    open_space = Openspace(tables,table_num)
    
    

    # assign a colleague randomly to a table
    open_space.organize(names_list)

    # save the seat assigments to a new file
    open_space.store(output_filename)

    # display assignments in the terminal
    open_space.display()

if __name__ == "__main__":
    main()
