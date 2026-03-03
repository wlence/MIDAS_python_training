response = input("Enter a number: ")

#Defensive programming: anticipate and handle potential errors in user input
#Write code to check the input
if not response.isnumeric():
    print("That's not a number!")
    exit()

n = int(response)

for i in range(n):
    print(f"Number: {i}")

