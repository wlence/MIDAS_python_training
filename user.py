#Object-Oriented Programming

#Camel case for naming classes
class User():
    def __init__(self, name="", email="", active=False, id=None):
        self.name = name
        self.email = email
        self.active = active
        self.id = id

    def __str__(self):
        # Function to return a string representation of the object when we print it
        return f'User: {self.name} \nID: {self.id} \nEmail: {self.email} \nActive: {self.active}'

    def __repr__(self):
        # Function to return a string representation of the object when we print a list of objects
        return f'User(name={self.name}, email={self.email}, active={self.active}, id={self.id})'
    
    def display_info(self):
        return f'User: {self.name} \nID: {self.id} \nEmail: {self.email} \nActive: {self.active}'
    
if __name__ == "__main__":
    u1 = User("Alice", "alice@example.com", True, 1)
    print(u1.display_info())