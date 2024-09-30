
import os

list_shopping = []
list_quantity = []
while true:
    os.system('cls' if os.name == 'nt' else 'clear')
    print('''Choose the option you want:
1) view list
2) add object and quantity
3) modify quantity
4) remove object
5) end of list ''')
    
    
    option_choice = input("write the option number:")
    
    match option_choice:
    
        case '1': 
            for i in range(len(list_shopping)):
                print(list_shopping[i] + " " + str(list_quantity[i]) )
                input("press enter to continue...")

        case '2': 
            object_to_add = input('What do you want to add to the list?:')
            quantity_object = input("quantity object:")
            list_shopping.append(object_to_add) 
            list_quantity.append(quantity_object)

        case '3' : 
            for i in range(len(list_shopping)):
                print(list_shopping[i] + " " + str(list_quantity[i]) )
            object_to_modify = input('which item do you want to change the quantity of?:')
            new_quantity = input('what is the new quantity?:')
            index = list_shopping.index(object_to_modify)
            list_quantity[index] = new_quantity

        case '4' :
            print(list_shopping)
            object_to_remove = input('what do you want to remove to the list?:')
            index = list_shopping.index(object_to_remove)
            list_shopping.remove(object_to_remove)
            list_quantity.pop(index)

        case '5' : 
            os.system('cls' if os.name == 'nt' else 'clear')
            last_change = input("are you sure you're done?\n(write yes or no):")
            if last_change == "no":
                end = 0
            else:
                print('your list is end ')
                for e in range(len(list_shopping)):
                    print(list_shopping[e] + " " + str(list_quantity[e]) )
                break