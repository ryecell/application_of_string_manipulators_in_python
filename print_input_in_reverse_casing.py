print_input_in_reverse_casing.py
#ask user for their name
name = input("Enter your full name in incorrect casing: ")

#print input with capital letters format
for letter in name:
    if letter .isupper():
        letter.lower()
    else:
        letter.upper()

print(letter)
