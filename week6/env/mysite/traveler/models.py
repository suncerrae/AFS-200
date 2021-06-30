# # from django.db import models

# # # Create your models here.
# from django.db import models


# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')


# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)

#     from django.db import models


# Create your models here.
class Destination(models.Model):

    location = models.CharField(max_length=50)
    price = models.IntegerField()
    los = models.IntegerField()
    discription = models.TextField()
    img = models.ImageField(upload_to='pics')

class Welcome(models.Model):

    h2 = models.CharField(max_length=50)
    h1 = models.CharField(max_length=50)
    p = models.TextField()
    a1 = models.CharField(max_length=50)
    a2 = models.CharField(max_length=50)

class Reviews(models.Model):
    i = models.CharField( max_length=50)
    p = models.TextField()
    img = models.ImageField( upload_to='pics')
    h5 = models.CharField( max_length=50)
    span =models.CharField( max_length=50)

class Css(models.Model):
    slick = models.FileField(upload_to='css')