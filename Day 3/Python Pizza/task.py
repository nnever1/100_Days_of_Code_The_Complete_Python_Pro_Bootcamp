print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
final_cost = 0

if size == 'S':
    final_cost += 15
    if pepperoni == 'Y':
        final_cost += 2
    if extra_cheese == 'Y':
        final_cost += 1
elif size == 'M':
    final_cost += 20
    if pepperoni == 'Y':
        final_cost += 3
    if extra_cheese == "Y":
        final_cost += 1
elif size == 'L':
    final_cost =+ 25
    if pepperoni =='Y':
        final_cost += 3
    if extra_cheese == 'Y':
        final_cost += 1

print(f'Your final bill is: ${final_cost}.')