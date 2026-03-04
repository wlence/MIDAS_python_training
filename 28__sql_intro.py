#Structured Query Language (SQL) is a powerful language used for managing and manipulating relational databases. It allows users to create, read, update, and delete data in a structured format. SQL is widely used in various applications, from web development to data analysis, making it an essential skill for anyone working with databases.
import sqlite3

filename = "userdb.db"

# Connect to the database
conn = sqlite3.connect(filename)

# Read data from the database
sql = "SELECT * FROM users"
cursor = conn.execute(sql)

print(f"ID\t{"Name":16}\t{"Email":16}\t{"Status"}")
# Iterate through the results and print each record
# Records are returned as tuples, where each tuple represents a row in the database
for rec in cursor:
    id, name, email, active = rec
    print(f"{id}\t{name:16}\t{email:16}\t{'Active' if active else 'Inactive'}")

# CRUD operations
# Create a new record
sql = "INSERT INTO users (name, email, active) VALUES (?, ?, ?)"
new_user = ("Frank", "frank@example.com", 1)
conn.execute(sql, new_user)
conn.commit()

# Update a record
sql = "UPDATE users SET active = ? WHERE name = ?"
conn.execute(sql, (0, "Frank"))
conn.commit()

# Retrieve the new record
#sql = "SELECT * FROM users WHERE name = ?"
#cursor = conn.execute(sql, ("Frank",))

# Delete a record
sql = "DELETE FROM users WHERE name = ?"
conn.execute(sql, ("Frank",))
conn.commit()

for rec in cursor:
    id, name, email, active = rec
    print(f"{id}\t{name:16}\t{email:16}\t{'Active' if active else 'Inactive'}")

# Close the connection
conn.close()