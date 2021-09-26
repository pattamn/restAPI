from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

class Libraries(models.Model):
    library_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    postal_code = models.CharField(max_length=6)

    def __str__(self):
        return self.name 
class Users(User):
    def __str__(self):
        return self.first_name +" "+ self.last_name

class Books(models.Model):
    book_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=40)
    author_name= models.CharField(max_length=40)
    isbn_num= models.CharField(max_length=40)
    genre= models.CharField(max_length=40)
    description= models.CharField(max_length=100)

class Library_Activities(models.Model):
    library_activity_id = models.AutoField(primary_key=True)
    activity_type = models.TextChoices('in','out')
    library_book_id = models.ManyToManyField('Library_Books', blank=True)
    user_id = models.ForeignKey(Users, related_name='user_id',on_delete=models.CASCADE)
    check_in_at = models.DateTimeField(null=True, default=None)
    check_out_at = models.DateTimeField(null=True)


class Library_Books(models.Model):
    library_book_id = models.AutoField(primary_key=True)
    library_id =models.ForeignKey(Libraries,on_delete=models.CASCADE)
    book_id =models.ForeignKey(Books,related_name='books', on_delete=models.CASCADE)
    last_library_activity_id= models.ForeignKey(Library_Activities,null=True,related_name='library_activiites',blank=True, on_delete=models.CASCADE)

