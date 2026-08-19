# Computational Thinking Exercise
## [Smart School Canteen Queue]
**Name:** Christine Joyce
**Section:** 9-Magnesium
**Last Name:** Astillero
**Date:** 8/19/2026
---

## Step 1: Identify the Big Problem
### Main Problem
The system is very time consuming and is prone to human errors because most of the operations are done manually without technical help.
---
## Step 2: Identify the Sub-Problems
1. There is no system to quickly calculate the total price and change.
2. There is no convenient way to check the status of the available foods.
3. The menu options are not already displayed in order for the students to decide ahead of time.
---
## Step 3: Apply Computational Thinking Skills
| Sub-Problem | CT Skill | Proposed Solution |
|---|---|---|
| Calculating Manually| Algorithm Design | create a program in which it will ask for the price of the selected food and the given payment, and it will calculate the total price and the change. |
| Status of Foods | Algorithm Design | create a program where it will ask the name of the dish, and how many servings it can provide. And every time someone purchases a dish, it will ask for its dish name and it will subtract the purchased amount from the dish's recent number of serving. and if the serving is reduced to 0, it will notify the user.  |
| Menu Options| Abstractions | Ask for the menu options and the price and display it without additional information. |
---
## Step 4: Algorithmic Solution
### Selected Sub-Problem
Calculating Manually
### Pseudocode
``` Python
START

no_of_dishes = int(input("what is the number of dishes/foods that you wish to sell?"))
prices = []
name_of_dish = []

for i in range(no_of_dishes):
 name = str(input(f"Enter the name of dish number {i + 1}: "))
 name_of_dish.append(name)
 price = int(input(f"Enter the price per serving of dish number {i + 1}: "))
 prices.append(price)

for i in range(no_of_dishes):
 print(f"Dish no.{i + 1}: {name_of_dish[i]} / Price: {prices[i]}")

no_of_dishes_to_buy = int(input("How many of the listed food options will you buy?"))

prices_of_chosen_food = []

def calculate_num():
 for i in range(no_of_dishes_to_buy):
  corres_num = int(input("Enter the corresponding number of the dish that you want to purchase: "))
  if corres_num <= len(prices):
   quantity = int(input("How many servings of the chosen dish do you want to purchase?"))
   total = prices[corres_num - 1] * quantity
   prices_of_chosen_food.append(total)
   print(" ")
   
  else:
   print("The corresponding number you chose is not available/is not a part of the shown options, please try again!")

def display_total():
 print(f"The total amount is {sum(prices_of_chosen_food)} pesos")
 amount_received = int(input("How much will you pay?"))
 print(f"Your change is {amount_received - (sum(prices_of_chosen_food))} pesos")
 print(" ")
 print("Thank you for your time! Please come again!")

def main():
 calculate_num()
 if (len(prices_of_chosen_food)) == 0:
  print("Your total is zero, please try again.")
 else:
  display_total()

main()

END
```
---
