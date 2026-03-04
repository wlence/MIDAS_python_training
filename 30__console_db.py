
from userdao import UserDAO

dao = UserDAO()

#users = dao.get_all_users()

dao.delete_user(42)

users = dao.get_all_users()

for user in users:
    print(user)

dao.close_connection()