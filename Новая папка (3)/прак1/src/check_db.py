import sqlite3
conn = sqlite3.connect('app.db')
cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = cursor.fetchall()
print("Таблицы в базе:", tables)
cursor.execute("PRAGMA table_info(tasks)")
for col in cursor.fetchall():
    print(f"  колонка: {col[1]:<7} тип: {col[2]:<8} NOT NULL: {bool(col[3])}  по умолчанию: {col[4]}")
conn.close()
