#Libraries
import csv
from datetime import datetime
from pizza import *
from sauces import *
def main():
    #Read the menu from menu.txt
    with open("menu.txt","r") as f:
        print(f.read())
    #Get pizza choice from user.
    pizza_choice = input("\nEnter your pizza choice : ")
    #Create pizzas to reach the pizza objects.
    pizzas = {"1" : Classic(),"2" : Margherita(),"3" : TurkPizza(),"4" : PlainPizza()}
    #Get sauce choice from user.
    sauce_choice = input("\nEnter your sauce choice : ")
    #Combine pizza and sauce.
    order = None
    if sauce_choice == "11":
        order = Olives(pizzas[pizza_choice])
    elif sauce_choice == "12":
        order = Mushrooms(pizzas[pizza_choice])
    elif sauce_choice == "13":
        order = GoatCheese(pizzas[pizza_choice])
    elif sauce_choice == "14":
        order = Meat(pizzas[pizza_choice])
    elif sauce_choice == "15":
        order = Onions(pizzas[pizza_choice])
    elif sauce_choice == "16":
        order = Corn(pizzas[pizza_choice])
    else:
        print("You entered wrong number.")
        exit()
    #Print the pizza and cost of user.
    order_description = order.component.get_description() + ' with ' + order.get_description()
    order_cost = order.component.get_cost() + order.get_cost()
    print(f"\nYour order is : {order_description}")
    print(f"Total cost is : {order_cost}")
    #Get the user name,id number,credit card number and password.
    user_name = input("\nEnter your name and surname please : ")
    id_number = input("\nEnter your id number(11 character) : ")
    credit_card_number = input("\nEnter your credit card number (16 character) : ")
    #Check 16 character credit card number.
    if len(credit_card_number) == 16 and credit_card_number.isdigit():
        pass
    else:
        print("Please enter valid credit card number next time!")
        exit()
    #Get user credit card password.
    credit_card_password = input("\nEnter your credit card password (4 character) : ")
    #Check 4 character credit card password.
    if len(credit_card_password) == 4 and credit_card_password.isdigit():
        pass
    else:
        print("Please enter valid credit password next time!")
        exit()
    #Time of order.
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    #Save information to database.
    with open("Orders_database.csv","a") as f:
        writer = csv.writer(f)
        #write the data
        writer.writerow([user_name,id_number,credit_card_number,order_description,dt_string,credit_card_password])

main()