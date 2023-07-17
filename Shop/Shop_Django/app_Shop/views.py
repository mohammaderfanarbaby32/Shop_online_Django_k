from django.shortcuts import render
from django.http import JsonResponse
from .models import Customer , Products , categories
from django.http import HttpResponse
def serch_field_Customer(request , User_Name):
    if User_Name == '*':
        words = Customer.objects.all()
        return JsonResponse(list(words.values()), safe=False)
    else :
      try:
          words = Customer.objects.filter(User_Name=User_Name) # فیلتر کردن بر اساس first_name
          word_list = []
          for word in words:
              word_dict = {'User_Name': word.User_Name, 'First_Name': word.First_Name,'Last_name':word.Last_name,'email': word.email, 'Phonee_number': word.Phonee_number,'City':word.City, 'Postal_Code': word.Postal_Code}
              word_list.append(word_dict)
          return JsonResponse(word_list, safe=False)
      except Customer.DoesNotExist:
          return Customer(status=404)

def add_field_Customer(request, First_Name, Last_name, email, Phonee_number, Address, City, Postal_Code, User_Name):
    new_word = Customer(First_Name=First_Name, Last_name=Last_name, email=email, Phonee_number=Phonee_number, Address=Address, City=City, User_Name=User_Name, Postal_Code=Postal_Code)
    new_word.save()
    return HttpResponse(''+User_Name+' added successfully!')


def Delete_field_Customer(request, User_Name):
    categories = Customer.objects.filter(User_Name=User_Name)
    count_before_delete = categories.count()
    for category in categories:
        category.delete()
    return HttpResponse(f"All {count_before_delete} categories with the name '{User_Name}' were successfully deleted.")

def Update_field_Customer(request,First_Name,Last_name,email,Phonee_number,Address,City,Postal_Code,User_Name):
    customers = Customer.objects.filter(User_Name=User_Name)
    count_before_update = customers.count()
    for customer in customers:
        customer.Last_name = Last_name
        customer.email = email
        customer.Phonee_number = Phonee_number
        customer.Address = Address
        customer.City = City
        customer.Postal_Code = Postal_Code
        customer.First_Name = First_Name
        customer.save()
    return HttpResponse(f'{count_before_update} {User_Name} updated successfully!')

#----------------------------------------------------------------------------------------------------------

def serch_field_Product(request , Product_Name):
    if Product_Name == '*':
        words = Products.objects.all()
        return JsonResponse(list(words.values()), safe=False)
    else :
      try:
          words = Products.objects.filter(Product_Name=Product_Name) # فیلتر کردن بر اساس first_name
          word_list = []
          for word in words:
              word_dict = {'product_Name': word.Product_Name, 'desciprion': word.desciption,'price':word.price,'image': word.image, 'category_id': word.category_id}
              word_list.append(word_dict)
          return JsonResponse(word_list, safe=False)
      except Customer.DoesNotExist:
          return Customer(status=404)




def add_field_Product(request, Product_Name, desciption, price, image, categories_ID_id):
    new_word = Products(Product_Name=Product_Name, desciption=desciption, price=price, image=image, categories_ID_id=categories_ID_id)
    new_word.save()
    return HttpResponse(''+Product_Name+' added successfully!')


def Delete_field_Product(request, Product_Name):
    categories = Products.objects.filter(Product_Name=Product_Name)
    count_before_delete = categories.count()
    for category in categories:
        category.delete()
    return HttpResponse(f"All {count_before_delete} categories with the name '{Product_Name}' were successfully deleted.")

def Update_field_Product(request,Product_Name,desciption,price,image,categories_ID_id):
    customers = Products.objects.filter(Product_Name=Product_Name)
    count_before_update = customers.count()
    for customer in customers:
        customer.desciption = desciption
        customer.price = price
        customer.image = image
        customer.categories_ID_id = categories_ID_id
        customer.save()
    return HttpResponse(f'{count_before_update} {Product_Name} updated successfully!')

#----------------------------------------------------------------------------------------------------------

def serch_field_categories(request , categories_ID):
    if categories_ID == '*':
        categories_ID = categories.objects.all()
        return JsonResponse(list(words.values()), safe=False)
    else :
      try:
          words = categories.objects.filter(categories_ID=categories_ID) # فیلتر کردن بر اساس first_name
          word_list = []
          for word in words:
              word_dict = {'categories_ID': word.categories_ID, 'categories_name': word.categories_name,'categories_image':word.categories_image}
              word_list.append(word_dict)
          return JsonResponse(word_list, safe=False)
      except categories.DoesNotExist:
          return categories(status=404)




def add_field_categories(request, categories_ID, categories_name, categories_image):
    new_word = categories(categories_ID=categories_ID, categories_name=categories_name, categories_image=categories_image)
    new_word.save()
    return HttpResponse(''+categories_name+' added successfully!')


def Delete_field_categories(request, categories_ID):
    Categories = categories.objects.filter(categories_ID=categories_ID)
    count_before_delete = Categories.count()
    for category in Categories:
        category.delete()
    return HttpResponse(f"All {count_before_delete} categories with the name '{categories_ID}' were successfully deleted.")

def Update_field_categories(request,categories_ID,categories_name,categories_image):
    customers = categories.objects.filter(categories_ID=categories_ID)
    count_before_update = customers.count()
    for customer in customers:
        customer.categories_name = categories_name
        customer.categories_image = categories_image
        customer.save()
    return HttpResponse(f'{count_before_update} {categories_image} updated successfully!')