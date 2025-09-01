from main import config_cursor
config_cursor.execute("""
SELECT * FROM config
""")
rows = config_cursor.fetchall()

for row in rows:
  print(row)