#ask user for their name
name = input("Enter your full name: ")

#reformat name in pascal casing using title() and replace() function
name_casing = name.lower()
name_with_underscore = name_casing.replace(" ", "_") #replacing spaces with nothing

#print
print(name_with_underscore)

