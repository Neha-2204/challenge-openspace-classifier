def read_names_from_txt(filepath:str)->list:
    '''Opening the text file and reading its lines
    and turning the file in a list and returning a 
    list'''
    with open(filepath) as file:
        names_list = file.readlines()
        names_list = [x.strip() for x in names_list]
        return names_list
        

       
