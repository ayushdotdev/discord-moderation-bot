from main import config_cursor,config
config_cursor.execute("""
ALTER TABLE config
ADD COLOUMN invitelog_channel INTEGER DEAFULT NULL
""")
config.commit()

config_cursor.execute("""
SELECT * FROM config
""")
rows = config_cursor.fetchall()

for row in rows:
  print(row)