import sqlite3

# 1. Подключение: если файла app.db нет — он создастся автоматически
conn = sqlite3.connect('app.db')

# 2. Курсор — через него отправляем SQL-команды
cursor = conn.cursor()

# 3. DDL: создаём таблицу задач.
#    IF NOT EXISTS — повторный запуск не вызовет ошибку (идемпотентность)
#    id     — уникальный номер, заполняется автоматически
#    title  — название задачи, обязательно (NOT NULL)
#    status — статус, по умолчанию 'new'
cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id     INTEGER PRIMARY KEY,
        title  TEXT NOT NULL,
        status TEXT DEFAULT 'new'
    )
""")

# 4. Фиксация изменений на диске
conn.commit()

# 5. Закрытие соединения (освобождаем файл базы)
conn.close()

print("База данных и таблица tasks успешно созданы.")
