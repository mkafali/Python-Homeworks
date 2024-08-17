#Taking order program for restaurant
order_list = [] #order's list
def prepareInfo(choice,list,code): 
    if code != "0": # code=="0" is initial code in main() function
        code = list[int(choice)-1][-1]
    else:
        code = str(choice)
    order_list.append(list[int(choice)-1][1]) #append informations which will be printed after completing order  
    return code #code: related code for other process

def getUserInput(file):
    file = file.rstrip(".txt")
    file = file.rstrip("s")
    choice = int(input("Please select the " + file + " : "))
    return str(choice) #choice: user's choice
    
def printMenu(file_name, code):
    list = []
    file = open(file_name,"r")
    file_str = file.readlines()
    num = 0
    for i in file_str:
        regulated_i = i.split(";")
        regulated_i[0] = regulated_i[0].lstrip("#") #remove "#" char
        if code == regulated_i[0] or code == "0": # code=="0" is initial code in main() function
            print(str(str(num+1) + "." + regulated_i[1].strip()))    
            num += 1
            for q in range(len(regulated_i)):
                regulated_i[q] = regulated_i[q].rstrip() #arrangement informations for list
            list.append(regulated_i)
    file.close()
    return list #list: list of order informations according to each user input

def main():
    print("--------------------\nWelcome to the Store\n--------------------")
    order = True
    sum = 0
    while order:
        order = True
        code = "0" #it is only for beginning
        files = ["categories.txt","products.txt","portions.txt"]
        for i in files:
            #choice: user's choice, list: list of order informations according to each user input, code: related code for other process 
            liste = printMenu(i,code)
            choice = getUserInput(i)
            code = prepareInfo(choice,liste,code)
        order_list.append(str(code)+"$") #append cost
        sum += float(code) #calculating total cost
        order_list.append("\n")            
        while order != "y" and order != "n":
            order = input("Would you like to complete the order (y,n)?")
        if order == "y":
            order = False
            print("-"*140)
            for i in order_list:
                if i != "\n":
                    print((i + " "*(35-(len(i)))),end = "") #every row's lenght are 35 chars
                else:
                    print()
            print("-"*140 + f"\nTotal =      {sum}$")
            
if __name__ == "__main__":
    main()
    