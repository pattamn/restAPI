import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'libProject.settings')

import django
django.setup()

from library.models import Libraries,Library_Activities,Users,Books,Library_Books
from faker import Faker
from datetime import datetime,timedelta 


fake = Faker()
for i in range(20):
    book = Books()
    la = Library_Activities()
    lb = Library_Books()

    name = fake.name()
    
    book.title = name +' Book'
    book.author_name= name
    book.isbn_num= fake.isbn10()
    book.genre=  ''
    book.description=  'Author is  %s'%(fake.name)
    book.save()
    if i%5==0:
        lib = Libraries()
        user = Users()

        lib.name = name
        lib.city = fake.city()
        lib.state = fake.state()
        lib.postal_code = fake.zipcode()
        lib.save()

        user.first_name = name
        user.last_name = name
        user.password = 'psw'
        user.email = 'test%s@test.com'%(i)
        user.username = name
        user.save()
    
    
    la.activity_type = 'in'
    la.user_id = user
    la.check_in_at =  datetime.now() +timedelta(hours=1)
    la.save()
  
    lb.library_id = lib
    lb.book_id = book
    lb.last_library_activity_id = la
    
    lb.save()

    