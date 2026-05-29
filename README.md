# Challenge-Openspace-Classifier
## Project 1

## 🏢 Description

Your company moved to a new office at Brussels . Its an openspace with available tables and seats.(Lets assume its 6 and 4) As many of you are new colleagues, you come up with the idea of changing seats everyday and get to know each other better by working side by side with your new colleagues. 

This script runs everyday to re-assign everybody to a new seat.
## 📦 Repo structure

```
.
├── src/
│   ├── openspace.py
│   ├── table.py
│   └── read_file.py
├── .gitignore
├── main.py
├── new_colleagues.txt
├── output.txt
└── README.md
```
## 🛎️ Usage

1. Clone the repository to your local machine.

2 .To run the script, you can execute the `main.py` file from your command line:

```
   python main.py

3. The script reads your input file, and organizes your colleagues to random seat assignments. The resulting seating plan is displayed in your console and also saved to an "output.txt" file in your root directory. 
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

    # display assignments
    open_space.display()

if __name__ == "__main__":
    main()
```
## ⏱️ Timeline

This project took two days for completion.

## 📌 Personal Situation
This project was done as part of the AI Boocamp at BeCode.org. 

Connect with me on [LinkedIn](www.linkedin.com/in/neha-khandelwal-1a54291b7)
      


    
