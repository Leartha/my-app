from django.db import models

class User(models.Model):
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=255)

    class Meta:
        db_table = 'users'
        managed = False


class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'categories'
        managed = False


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image_url = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, db_column='category_id')

    class Meta:
        db_table = 'products'
        managed = False

class CartItem(models.Model):
    user_id = models.IntegerField()
    product_id = models.IntegerField()
    quantity = models.IntegerField()

    class Meta:
        db_table = 'cart_items'
        managed = False


class Order(models.Model):
    user_id = models.IntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField()

    class Meta:
        db_table = 'orders'
        managed = False


class OrderItem(models.Model):
    order_id = models.IntegerField()
    product_id = models.IntegerField()
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'order_items'
        managed = False