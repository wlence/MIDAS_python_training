from user import User

u = User("Bob", "bob~example.com", True, 2)
print(u.display_info())

users = [
    u,
    User("Charlie", "charlie@example.com", False, 3),
    User("David", "dave:@example.com", True, 4),
    User("Eve", "eevee@gmail.com", False, 5)
]

for user in users:
    print(user.name)
    
print(users[-1].email)
print([user.active for user in users[2:]])

print(u)
print(users)

