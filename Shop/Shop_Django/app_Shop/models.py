from django.db import models

class Admin(models.Model):
    User_Name = models.TextField(max_length=50)
    Password = models.TextField(max_length=20)
class Customer(models.Model):
    Customer_ID = models.AutoField(primary_key=True)
    First_Name = models.TextField(max_length=20)  
    Last_name = models.TextField(max_length=20)
    email = models.TextField(max_length=40)
    Phonee_number = models.TextField(max_length=12)
    Address = models.TextField(max_length=35)
    City = models.TextField(max_length=10)
    Postal_Code = models.TextField(max_length=20)
    User_Name = models.TextField(max_length=30)

class categories(models.Model):
    categories_ID = models.AutoField(primary_key=True)
    categories_name = models.TextField(max_length=20)  
    categories_image = models.TextField(max_length=30)

class Products(models.Model):
    Product_ID = models.AutoField(primary_key=True)
    Product_Name = models.TextField(max_length=20)  
    desciption = models.TextField(max_length=12)
    price = models.TextField(max_length=35)
    image = models.TextField(max_length=10)
    categories_ID = models.ForeignKey(categories,max_length=30,on_delete=models.CASCADE)

class Order(models.Model):
    Order_ID = models.AutoField(primary_key=True)
    Customer_ID = models.ForeignKey(Customer,max_length=20,on_delete=models.CASCADE)  
    Order_date = models.TextField(max_length=12)

class Order_detail(models.Model):
    Product_ID = models.ForeignKey(Products,max_length=30,on_delete=models.CASCADE)
    Customer_ID = models.ForeignKey(Customer,max_length=30,on_delete=models.CASCADE)  
    item_price = models.TextField(max_length=12)
    categories_ID = models.TextField(categories,max_length=30)
    quantity = models.TextField(max_length=20)  
    item_price = models.TextField(max_length=12)
    Order_ID = models.ForeignKey(Order,max_length=30,on_delete=models.CASCADE)
    

      

# Create your models here.
