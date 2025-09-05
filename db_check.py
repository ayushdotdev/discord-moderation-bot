from main import config_cursor,config
config_cursor.execute("""
ALTER TABLE config
ADD COLOUM invitelog_channel INTEGER DEFAULT NULL
""")
config.commit()

config_cursor.execute("""
SELECT * FROM config
""")
rows = config_cursor.fetchall()

for row in rows:
  print(row)