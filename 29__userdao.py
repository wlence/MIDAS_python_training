#Data Access Object (DAO) for User
import sqlite3
from user import User

class UserDAO():
    def __init__(self, filename="userdb.db"):
        self.filename = filename
        self.conn = sqlite3.connect(filename)
    
    def close_connection(self):
        self.conn.close()
    
    def add_user(self, user):
        sql = "INSERT INTO users (name, email, active) VALUES (?, ?, ?)"
        self.conn.execute(sql, (user.name, user.email, int(user.active)))
        self.conn.commit()
    
    def get_user_by_email(self, email):
        sql = "SELECT * FROM users WHERE email = ?"
        cur = self.conn.execute(sql, (email,))
        rec = cur.fetchone()
        if rec:
            id, name, email, active = rec
            return User(name, email, bool(active), id)
        return None
    
    def get_all_users(self):
        users = []
        sql = "SELECT * FROM users"

        cur = self.conn.execute(sql)

        for rec in cur:
            id, name, email, active = rec
            users.append(User(name, email, bool(active), id))
            
        return users
    
    def delete_user(self, id):
        sql = "DELETE FROM users WHERE id = ?"
        self.conn.execute(sql, (id,))
        self.conn.commit()
    
    def update_user(self, id, name=None, email=None, active=None):
        sql = "UPDATE users SET "
        params = []
        if name is not None:
            sql += "name = ?, "
            params.append(name)
        if email is not None:
            sql += "email = ?, "
            params.append(email)
        if active is not None:
            sql += "active = ?, "
            params.append(int(active))
        
        # Remove the last comma and space
        sql = sql[:-2]
        sql += " WHERE id = ?"
        params.append(id)

        self.conn.execute(sql, tuple(params))
        self.conn.commit()
    
dao = UserDAO()

users = dao.get_all_users()
#print(users)

#Delete a user by ID
dao.delete_user(27)

#Update a user by ID
user_to_update = users[-1]
user_to_update.active = not user_to_update.active

dao.update_user(user_to_update.id, active=user_to_update.active)


user = dao.get_user_by_email("fred@gmail.com")
if user:
    print(user.display_info())

dao.add_user(User("Willian", "wlenert@cadence.com", True))

users = dao.get_all_users()
for user in users:
    print(user.display_info())

dao.delete_user(users[-1].id)

dao.close_connection()