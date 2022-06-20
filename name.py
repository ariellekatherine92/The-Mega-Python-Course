name = input("Enter your name: ")
surname = input("Enter your surname: ")
message = "Hello %s %s!" % (name, surname)
message = f"Hello {name} {surname}"
print(message)

name = "John"
surname = "Smith"
 
message = "Your name is {}. Your surname is {}".format(name, surname)
print(message)

#using the .formant variable form