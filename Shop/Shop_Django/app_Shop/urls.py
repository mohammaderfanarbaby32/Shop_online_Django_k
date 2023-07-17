from django.urls import path
from . import views

urlpatterns = [
    path('serch_field_Customer/<str:User_Name>/', views.serch_field_Customer, name='serch_field_Customer'),
    path('add_field_Customer/<str:User_Name>/<str:First_Name>/<str:Last_name>/<str:email>/<str:Phonee_number>/<str:Address>/<str:City>/<str:Postal_Code>/', views.add_field_Customer, name='add_field_Customer'),
    path('Delete_field_Customer/<str:User_Name>/', views.Delete_field_Customer, name='Delete_field_Customer'),
    path('Update_field_Customer/<str:User_Name>/<str:First_Name>/<str:Last_name>/<str:email>/<str:Phonee_number>/<str:Address>/<str:City>/<str:Postal_Code>/', views.Update_field_Customer, name='Update_field_Customer'),
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    path('serch_field_Product/<str:Product_Name>/', views.serch_field_Product, name='serch_field_Product'),
    path('add_field_Product/<str:Product_Name>/<str:desciption>/<str:price>/<str:image>/<str:categories_ID_id>/', views.add_field_Product, name='add_field_Product'),
    path('Delete_field_Product/<str:Product_Name>/', views.Delete_field_Product, name='Delete_field_Product'),
    path('Update_field_Product/<str:product_name>/<str:description>/<str:price>/<str:image>/<str:categories_ID_id>/', views.Update_field_Product, name='Update_field_Product'),
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    path('serch_field_categories/<str:categories_ID>/', views.serch_field_categories, name='serch_field_categories'),
    path('add_field_categories/<str:categories_ID>/<str:categories_name>/<str:categories_image>/', views.add_field_categories, name='add_field_categories'),
    path('Delete_field_categories/<str:categories_ID>/', views.Delete_field_categories, name='Delete_field_categories'),
    path('Update_field_categories/<str:categories_ID>/<str:categories_name>/<str:categories_image>/', views.Update_field_categories, name='Update_field_categories'),
]