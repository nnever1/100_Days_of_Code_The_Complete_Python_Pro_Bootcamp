import  random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password=[]
password_str=''
ran_letters=random.sample(letters,nr_letters)
ran_symbols=random.sample(symbols,nr_symbols)
ran_numbers=random.sample(numbers,nr_numbers)

for symbol in ran_symbols:
    password.append(symbol)
for letter in ran_letters:
    password.append(letter)
for number in ran_numbers:
    password.append(number)
random.shuffle(password)
for item in password:
    password_str += item
password_str.join(password)
print(password)
print(password_str)
