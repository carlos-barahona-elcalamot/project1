import mysql.connector as mariadb
import sys
import time

# Wait 5 seconds for the database server to start
print("Waiting 15 seconds for the database server to start...")
time.sleep(15)

print("---------------------------------")
print("List of tables:")
print("---------------------------------")

# Connect to MariaDB Platform
print("Connecting to database...")
try:
    conn = mariadb.connect(
        user="root",
        password="Asdqwe123",
        host="projecteexamen-examenDB-1",
        port=3306,
        database="information_schema"

    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

# Get Cursor
cur = conn.cursor()
cur.execute("select NAME, N_COLS from INNODB_SYS_TABLES")
# Print Result-set
for (NAME,N_COLS) in cur:
    print(f"{NAME}, {N_COLS}")

conn.close()
