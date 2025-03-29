#ask user for their name
name = input("Enter your full name: ")

#reformat name in pascal casing using title() and replace() function
name_casing = name.title()
name_with_no_space = name_casing.replace(" ", "") #replacing spaces with nothing

#print
print(name_with_no_space)

