from django.db import models
import datetime

# Create your models here.

#category of products
class Category(models.Model):
  name=models.CharField(max_length=50)

  def __str__(self):
    return self.name
  
  class Meta:
    verbose_name_plural='categories'

#Customers
class Customer(models.Model):
  first_name= models.CharField(max_length=50)
  last_name=models.CharField(max_length=50)
  phone=models.CharField(max_length=14)
  email=models.EmailField(max_length=50)
  password=models.CharField(max_length=50)

  def __str__(self):
    return f'{self.first_name}{self.last_name}'



#all product
class Product(models.Model):
  name=models.CharField(max_length=50)
  price=models.DecimalField(default=0,decimal_places=2,max_digits=8)
  category=models.ForeignKey(Category, on_delete=models.CASCADE,default=1)
  description=models.CharField(max_length=250,default='',null=True)
  image=models.ImageField(upload_to='products/')

  def __str__(self):
    return self.name

#customer oders
class Order(models.Model):
  product=models.ForeignKey(Product,on_delete=models.CASCADE)
  customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
  quantity=models.IntegerField(default=1)
  address=models.CharField(max_length=100,default='',null=True)
  phone=models.CharField(max_length=14,default='',blank='')
  date=models.DateField(default=datetime.datetime.today)
  status=models.BooleanField(default=False)

  def __str__(self):
    return self.product