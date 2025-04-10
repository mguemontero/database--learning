# created on 10.04.25

import hashlib
def md5sum(t)
	return hashlib.md5(t).hexdigest()
con = sqlite3.connect(":memory:")
con.create_funtion("md5", 1, md5sum)
for row in con.execute("SELECT md5(?)", (b"foo",)):
	print(row)

# expected result --> ('acbd18db4cc2f85cedef654fccc4a4d8',)

con.close()