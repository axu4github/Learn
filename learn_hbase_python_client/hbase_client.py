
import happybase

connection = happybase.Connection('10.0.3.41')
table = connection.table('smartv')

# table.put(b'row-key', {b'family:qual1': b'value1',
#                        b'family:qual2': b'value2'})

row = table.row(b'dy-gz-t51851828_20150115_7371575.mp3')

row_keys = []
for i in range(10000):
    row_keys.append(b'dy-gz-t54548716_20150201_8221862.mp3')

rows = table.rows(row_keys)

for row_key in row_keys:
    row = table.row(row_key)

# for key, data in table.scan(row_prefix=b'row'):
#     print(key, data)  # prints 'value1' and 'value2'

# row = table.delete(b'row-key')
