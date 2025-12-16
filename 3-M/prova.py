import os
inventory ={}
variable = 0

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    variable = 0


    print('''Choose the option you want: 
1. view inventory.
2. Add the product, its price and its quantity.
3. Remove products.
4. total product.
5. total merchandise value.
6. Escape''')
    
    choise = int(input("write the option number:"))

    if choise < 7 and choise > 0:    
        match choise:
            case 1:
                print(inventory)
                input("press enter to continue...")

            case 2:
                    modify_product = input("Enter the product: ")
                    modify_prices = int(input("Enter the price: "))
                    modify_quantity = int(input('Enter the quantity: '))            
                    
                    inventory['product ' + str(variable)] = modify_product
                    inventory['price ' + str(variable)] = modify_prices
                    inventory['quantity '+ str(variable)] = modify_quantity

                    variable += 1
                    input("press enter to continue...")

            case 3:
                number_product = input("Enter the number of product for remove: ")
                if number_product <= variable:
                    del thisdict["product " + str(number_product) ]
                    del thisdict["price " + str(number_product) ]
                    del thisdict["quantity " + str(number_product) ]
                    
                else:
                    print('ERROR!!! the selected product does not exist')
                    input("press enter to continue...")

            case 4:
                    
                total_product = 0
                for i in range(variable):
                    
                    total_product += inventory['quantity '+str(i)]
                print(f'total product {total_product}')
                input("press enter to continue...")

            case 5: 
                total_value = 0
                for o in range(variable):
                    
                    total_value += (inventory['price '+str(o)]* inventory['quantity '+str(o)])
                print(f'total value {total_value}')
                input("press enter to continue...")

            case 6:
                
                break
    else:
        print('ATTENTION! the option selected does not exist')
        input("press enter to continue...")