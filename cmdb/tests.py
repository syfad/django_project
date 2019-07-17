from django.test import TestCase

# Create your tests here.


import datetime

print(datetime.datetime.utcnow())

LIST = []
for i in range(100):
    LIST.append(i)

print(LIST[1:10])




import pymysql
from utils import pagination

current_page = (1)
current_page = int(current_page)
val = (10)
val = int(val)

db = pymysql.connect("192.168.100.198", "django", "123456", "django")
# cursor = db.cursor()
cursor = db.cursor(pymysql.cursors.DictCursor)
cursor.execute("SELECT COUNT(*) FROM user")
data_count = cursor.fetchone()

count = data_count['COUNT(*)']

page_obj = pagination.Page(current_page, count, val)


print(page_obj.start, page_obj.end, page_obj.total_count)

cursor.close()
db.close()