#This is my third homework. I programmed simple database management system without using sql or any database server.
#I create new syntax that determined by my instructor and use files as a database. Also, I create some query functions. 
#You can do basic database operations with my program.
import os

def create_file(query):
    #query--> "create": ["create","file","Identifier","with","Identifiers"]
    name = query[2] + ".txt" 
    try:
        f = open(name,"x") #does file exist
    except: #if file exists
        f = open(name,"w") #recreate file again
        f.write("id" + " "*4)
        for i in query[-1]:
            f.write(i + " "*4)
        f.write("\n")
        print("There was already such a file. It is removed and then created again.")
    else: #if file does not exist
        f.write("id" + " "*4) #id automatically added
        for i in query[-1]:
            f.write(i + " "*4)
        f.write("\n")
        print("Corresponding file was successfully created.")
    finally:
        f.close()


def delete_file(query):
    #query--> "delete": ["delete","file","Identifier"]
    file = query[-1] + ".txt"
    file_names = os.listdir()
    if file in file_names:
        os.remove(file)
        print("Corresponding file was successfully deleted.")
    else:
        print("There is no such file.")
    
    
def display_files(query):
    #query--> "display": ["display","files"]
    file_names = os.listdir()
    file_names.remove("databasemanagement.py")
    print(f"Number of files: {len(file_names)}")
    count = 1
    for file in file_names:
        f = open(file)
        attributes = f.readline()
        attributes = attributes.split("    ") #get attributes names
        del(attributes[-1])
        str_attributes = ""
        for i in attributes:
            str_attributes += f"{i}," #add attributes into string
        str_attributes = str_attributes[:-1]
        name = file[:-4] #delete extension
        print(f"{count}) {name}: {str_attributes}")
        f.close()
        count += 1


def add_line(query):
    #query--> "add": ["add","Identifiers","into","Identifier"]
    file_names = os.listdir()
    file = query[-1] + ".txt"
    if file in file_names:
        f = open(file,"r+")
        attributes = f.readlines()
        if len(attributes) == 1:
            id_number = 1 #id number automatically given
        else:
            id_number = int(attributes[-1][0]) + 1 #calculate id of new line
        attributes = attributes[0].split("    ")
        del(attributes[-1])
        print(attributes)
        if len(attributes)-1 == len(query[1]):
            f.write(f"{id_number}    ")
            for i in query[1]:
                f.write(i + "    ")
            f.write("\n")
            print(f"New line was successfully added to students with id = {id_number}.")
  
        else:
            print("Numbers of attributes do not match.")
        f.close()
    else:
        print("There is no such file.")
        



def remove_lines(query):
    #query--> "remove": ["remove","lines","from","Identifier","where","Identifier","Operator","Identifier"]
    file = query[3] +".txt"
    file_names = os.listdir()
    if file in file_names:
        f = open(file,"r+")
        list_of_lines = f.readlines()
        f.close()
        lines = [] #it takes lines as a seperated list
        for i in list_of_lines:
            each_line = i.split("    ")
            del(each_line[-1])
            lines.append(each_line)

        if query[5] in lines[0]:
            index = lines[0].index(query[5])
            del_lines = [lines[0]] #lines will be deleted for operator ==
            not_del_lines = [lines[0]] #lines will be deleted for operator !=
            
            for line in lines[1:]:
                if line[index] != query[-1]:
                    not_del_lines.append(line)
                else:
                    del_lines.append(line)
            if query[-2] == "==":
                f = open(file,"w")
                for line in not_del_lines: #rewrite lines
                    for word in line:
                        f.write(word + "    ") 
                    f.write("\n")
                f.close()
                print(f"{len(lines)-len(not_del_lines)} lines were successfully removed.")
            
            else: 
                f = open(file,"w")
                for line in del_lines: #rewrite lines
                    for word in line:
                        f.write(word + "    ") 
                    f.write("\n")
                f.close()
                print(f"{len(lines)-len(del_lines)} lines were successfully removed.")

        else:
            print("Your query contains an unknown attribute.")

    else:
        print("There is no such file.")


def modify_lines(query):
    #query--> "modify": ["modify","Identifier","in","Identifier","as","Identifier","where","Identifier","Operator","Identifier"
    file = query[3] +".txt"
    file_names = os.listdir()
    if file in file_names:
        f = open(file,"r+")
        attributes = f.readline()
        attributes = attributes.split("    ")
        del(attributes[-1])
        change_attribute = query[1] #attribute that we change
        control_attribute = query[-3] #attribute that we control
        if change_attribute != "id":
            if change_attribute in attributes and control_attribute in attributes:
                change_index = attributes.index(change_attribute)
                control_index = attributes.index(control_attribute)
                f.seek(0)
                lines = f.readlines()
                f.close()
                line_index = 0
                counter = 0
                for line in lines:
                    each_line = line.split("    ")
                    del(each_line[-1])
                    lines[line_index] = each_line #seperate word of lines with ","
                    line_index += 1
                line_index = 1
                if query[-2] == "==":
                    for line in lines[1:]:
                        if line[control_index] == query[-1]:
                            counter += 1
                            lines[line_index][change_index] = query[-5] #change attribute
                        line_index += 1

                else:
                    for line in lines[1:]:
                        if line[control_index] != query[-1]:
                            counter += 1
                            lines[line_index][change_index] = query[-5] #change attribute
                        line_index += 1


                f = open(file,"w")
                for line in lines: #rewrite lines
                    for word in line:
                        f.write(word + "    ")
                    f.write("\n")
                f.close()

                
                print(f"{counter} lines were successfully modified.")

            else:
                print("Your query contains an unknown attribute.")
        else:
            print("Id values cannot be changed.")
        
    else:
        print("There is no such file.")


def fetch_lines(query):
    #query--> "fetch": ["fetch","Identifiers","from","Identifier","where","Identifier","Operator","Identifier"]}
    def calculate_lenght(list_of_lists): #calculate each columns lenght
        lenghts = []
        index_number = len(list_of_lists[0])
        for index in range(index_number):
            max = len(list_of_lists[0][index])
            for i in list_of_lists[1:]:
                if len(i[index]) > max:
                    max = len(i[index])
            lenghts.append(max + 3) #lenght of each column
        full_len = 0
        for i in lenghts:
            full_len += i
        lenghts.append(full_len + 1) #amount of "_"
        return lenghts

    file = query[3] +".txt"
    file_names = os.listdir()
    if file in file_names:
        f = open(file,"r+")
        attributes = f.readline()
        attributes = attributes.split("    ")
        del(attributes[-1])
        canfetch = 1
        if not query[-3] in attributes: #check identifier
            canfetch = 0
            print("Your query contains an unknown attribute.")
        for i in query[1]:
            if not i in attributes: #check identifiers
                print("Your query contains an unknown attribute.")
                canfetch = 0
        if canfetch:
            control_index = attributes.index(query[-3])
            fetch_index = []
            for i in query[1]:
                fetch_index.append(attributes.index(i)) #index of attributes that we fetch
            f.seek(0)
            lines = f.readlines()
            f.close()
            line_index = 0
            for line in lines:
                each_line = line.split("    ")
                del(each_line[-1])
                lines[line_index] = each_line #seperate word of lines with ","
                line_index += 1
            print_them = [query[1]]
            if query[-2] == "==":
                for line in lines[1:]:
                    print_lines = [] #lines that we fetch
                    if line[control_index] == query[-1]:
                        for i in fetch_index:
                            print_lines.append(line[i])
                        print_them.append(print_lines) #append lines as a list
           
            else:
                for line in lines[1:]:
                    print_lines = [] #lines that we fetch
                    if line[control_index] != query[-1]:
                        for i in fetch_index:
                            print_lines.append(line[i])
                        print_them.append(print_lines) #append lines as a list

            each_block = calculate_lenght(print_them) #calculate lenght of each column
            print("-"*each_block[-1])
            print_them_index = True
            for i in print_them: #print table
                index = 0
                for word in i:
                    print_word = f"| {word}"
                    print(print_word + " "*(each_block[index]-len(print_word)),end = "")
                    index += 1
                print("|")
                if print_them_index:
                    print("-"*each_block[-1]) #it is the top line of the table
                    print_them_index = False 
                
            print("-"*each_block[-1]) #it is the bottom line of the table
            
    else:
        print("There is no such file.")
    

def examine(input):
    #syntax rules for each process:
    queries = {"create": ["create","file","Identifier","with","Identifiers"],
               "delete": ["delete","file","Identifier"],
               "display": ["display","files"],
               "add": ["add","Identifiers","into","Identifier"],
               "remove": ["remove","lines","from","Identifier","where","Identifier","Operator","Identifier"],
               "modify": ["modify","Identifier","in","Identifier","as","Identifier","where","Identifier","Operator","Identifier"],
               "fetch": ["fetch","Identifiers","from","Identifier","where","Identifier","Operator","Identifier"]}
    
    keys = {"with", "into", "from", "where", "in", "as", "where","file","files","lines"}
    syntax_list = input.split(" ")
    syntax = list() #syntax that we send it to functions
    for i in syntax_list:
        if "," in i:
            i = i.split(",")
        syntax.append(i)

    if syntax_list[0] in queries:
        isvalid = 1 #if isvalid == 1 --> call functions 
        if len(syntax_list) >= len(queries[syntax_list[0]]):
            check_query = list()
            count = 0
            for part in queries[syntax_list[0]]:
                if part in keys:
                    if syntax_list[count] != part:
                        print("invalid query") #query does not obey syntax rule
                        isvalid = 0
                        break
                
                else:
                    if syntax_list[count] not in keys:
                        if part == "Identifier" or part == "Identifiers":
                            identifier_chars = {"@","_","."}
                            identifiers_chars = {"@","_",".",","} #identifiers should contain "," if it has plural elements
                            isidintifier = 1
                            i_counter = 0
                            if part == "Identifier":
                                if type(syntax[count]) == list:
                                    print("invalid query") #identifier cannot have plural element
                                    isidintifier = 0
                            if type(syntax[count]) != list or part == "Identifiers": 
                                for i in syntax_list[count]:
                                    if i.isascii():
                                        if not i.isalpha() and not i.isdigit():
                                            if part == "Identifier":
                                                if not i in identifier_chars:
                                                    if i == "-" and i_counter == 0:
                                                        if not syntax_list[count][i_counter+1:].isdigit():
                                                            print("invalid query") #identifier only contain "-" if and only if identifier is negative number
                                                            isidintifier = 0
                                                    else:
                                                        print("invalid query") #identifier only contain English letters,numbers, "@", "_", ".", ","
                                                        isidintifier = 0
                                                        break
                                            else:
                                                if not i in identifiers_chars:
                                                    if i == "-":
                                                        index = syntax_list[count].index(i)
                                                        if index != len(syntax_list[count])-1:
                                                            if syntax_list[count][index-1] == "," or index == 0:
                                                                index_of_i = 0
                                                                for i in syntax_list[count][index + 1:]:
                                                                    if index_of_i == 0 and i == ",":
                                                                        print("invalid query") #identifiers cannot contain "-" individually
                                                                        isvalid = 0
                                                                        break
                                                                    if i == ",":
                                                                        break
                                                                    else:
                                                                        if not i.isdigit():
                                                                            print("invalid query") #identifiers' elements can contain - if and only if element is negative number
                                                                            isvalid = 0
                                                                            break
                                                                    index_of_i += 1
                                                                
                                                            else:
                                                                print("invalid query") #identifiers' elements cannot contain if it is not negative number
                                                                isvalid = 0
                                                                break
                                                        else:
                                                            print("invalid query") #identifiers cannot contain "-" individually
                                                            isvalid = 0
                                                            break
                                                    else:
                                                        print("invalid query") #identifiers only contain English letters,numbers, "@", "_", ".",","
                                                        isidintifier = 0
                                                        break

                                    else:
                                        print("invalid query") #identifier must be ascii
                                        isidintifier = 0
                                    
                                    i_counter += 1

                            if isidintifier == 0:
                                isvalid = 0

                        elif part == "Operator": #operator can be only "==" or "!="
                            if syntax_list[count] != "==" and syntax_list[count] != "!=":
                                isvalid = 0
                                print("invalid query")
                                break
                                   
                    else:
                        print("invalid query") #value names cannot be keys
                        isvalid = 0    
                        break         

                count += 1

        else:
            print("invalid query") #It may couse index errors
            isvalid = 0

        if isvalid:
            if syntax_list[0] == "create":
                if not "id" in syntax[-1]:
                    create_file(syntax)
                else:
                    print("You cannot create a file with attribute 'id'") #I check it there because it does not necessary to execute create_file function to check this
            elif syntax_list[0] == "delete":
                delete_file(syntax)
            elif syntax_list[0] == "display":
                display_files(syntax)
            elif syntax_list[0] == "add":
                add_line(syntax)
            elif syntax_list[0] == "remove":
                remove_lines(syntax)
            elif syntax_list[0] == "modify":
                modify_lines(syntax)
            elif syntax_list[0] == "fetch":
                fetch_lines(syntax)

    else:
        print("invalid query") #query does not exist

def main():
    while True:
        user_input = input("What is your query?\n")
        if user_input == "x":
            break
        else:
            examine(user_input)

if __name__ == "__main__":
    main()

