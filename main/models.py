from django.db import models
from datetime import datetime

# Create your models here.

class Size(models.Model):
    title = models.CharField(max_length=200, blank=True)
    code = models.CharField(max_length=200, blank=True)
    level = models.IntegerField(blank=True, default=0)
    category = models.ForeignKey("Category", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.title} gram --> {self.category}'


class Category(models.Model):
    title = models.CharField(max_length=200, blank=True)
    parent = models.ForeignKey("Category", on_delete=models.CASCADE, null=True, blank=True)
    level = models.IntegerField(blank=True, default=0)
    good_count = models.IntegerField(blank=True, default=0)
    sub_category_count = models.IntegerField(blank=True, default=0)
    logo = models.ImageField(upload_to='upload', blank=True)

    def __str__(self):
        result_title = self.title
        parent_model = self.parent
        while parent_model:
            result_title = parent_model.title + " ---> " + result_title
            parent_model = parent_model.parent
        return result_title


class CategoryBrand(models.Model):
    title = models.CharField(max_length=200, blank=True)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    level = models.IntegerField(blank=True, default=0)

    def __str__(self):
        return f'{self.category.title} - {self.title}'


class Product(models.Model):
    title = models.CharField(max_length=200, blank=True)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    level = models.IntegerField(blank=True, default=0)
    old_price = models.FloatField(default=0)
    price = models.FloatField(default=0)
    discount = models.IntegerField(default=0, blank=True)
    rating = models.FloatField(default=0)
    mini_description = models.TextField(blank=True)
    size = models.ForeignKey("Size", on_delete=models.CASCADE)
    logo = models.ImageField(upload_to='upload', blank=True)
    logo2 = models.ImageField(upload_to='upload', blank=True)
    logo3 = models.ImageField(upload_to='upload', blank=True)
    logo4 = models.ImageField(upload_to='upload', blank=True)
    logo5 = models.ImageField(upload_to='upload', blank=True)
    logo6 = models.ImageField(upload_to='upload', blank=True)
    logo_ver_1 = models.ImageField(upload_to='upload', blank=True)
    logo_ver_2 = models.ImageField(upload_to='upload', blank=True)
    logo_gor_1 = models.ImageField(upload_to='upload', blank=True)
    logo_gor_2 = models.ImageField(upload_to='upload', blank=True)
    description = models.TextField(blank=True)
    is_new = models.BooleanField(default=False)
    is_main = models.BooleanField(default=False)
    is_popular = models.BooleanField(default=False)
    is_discount = models.BooleanField(default=False)
    is_gor_photo = models.BooleanField(default=False)
    is_ver_photo = models.BooleanField(default=False)
    stock = models.IntegerField(blank=True, default=0)
    brand = models.ForeignKey(CategoryBrand, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'{self.category} --> {self.title} --> {self.size.title}'


class Cart(models.Model):
    comment = models.CharField(max_length=200, blank=True)
    email = models.CharField(max_length=200, blank=True)
    last_name = models.CharField(max_length=200, blank=True)
    first_name = models.CharField(max_length=200, blank=True)
    zip_code = models.CharField(max_length=200, blank=True)
    country = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=200, blank=True)
    phone = models.CharField(max_length=200, blank=True)
    address = models.CharField(max_length=200, blank=True)
    is_accepted = models.BooleanField(default=False)
    is_payed = models.BooleanField(default=False)
    status = models.IntegerField(default=0) # 0 - created zakaz  -1 - otmenen  1 - confirmed    2 - accepted
    session_id = models.CharField(max_length=200, blank=True)
    amount = models.FloatField(default=0)
    discount = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)
    discount_int = models.IntegerField(default=0, blank=True)
    orig_price = models.FloatField(default=0)
    price = models.FloatField(default=0)
    created_at = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return f'{self.session_id} --> {self.last_name}'


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    amount = models.FloatField(default=0)
    price = models.FloatField(default=0)
    status = models.IntegerField(default=0)  # 0 - created -1 - deleted
    all_price = models.FloatField(default=0)

    def __str__(self):
        return f'{self.cart.id} -->  {self.product.title} -->  {self.amount}'


class CompareItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    session_id = models.CharField(max_length=200, blank=True)
    status = models.IntegerField(default=0)  # 0 - created -1 - deleted

    def __str__(self):
        return f'{self.session_id} --> {self.product.title}'


class WishItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    session_id = models.CharField(max_length=200, blank=True)
    status = models.IntegerField(default=0)  # 0 - created -1 - deleted

    def __str__(self):
        return f'{self.session_id} --> {self.product.title}'


class AboutUs(models.Model):
    title = models.CharField(max_length=200, blank=True)
    logo = models.ImageField(upload_to='upload', blank=True)
    description1 = models.TextField(blank=True)
    description2 = models.TextField(blank=True)
    description3 = models.TextField(blank=True)
    team_logo = models.ImageField(upload_to='upload', blank=True)
    team_name = models.CharField(max_length=200, blank=True)
    team_profession = models.CharField(max_length=200, blank=True)
    facebook = models.CharField(max_length=200, blank=True)
    whatsapp = models.CharField(max_length=200, blank=True)
    instagram = models.CharField(max_length=200, blank=True)
    address = models.CharField(max_length=200, blank=True)
    email = models.CharField(max_length=200, blank=True)
    phone = models.CharField(max_length=200, blank=True)
    short_des1 = models.TextField(blank=True)
    short_des2 = models.TextField(blank=True)
    short_des3 = models.TextField(blank=True)
    short_des4 = models.TextField(blank=True)
    sponsor_name = models.CharField(max_length=200, blank=True)
    sponsor_logo = models.ImageField(upload_to='upload', blank=True)

    def __str__(self):
        return f'{self.title} {self.sponsor_name}'


class Team(models.Model):
    team_logo = models.ImageField(upload_to='upload', blank=True)
    team_name = models.CharField(max_length=200, blank=True)
    team_profession = models.CharField(max_length=200, blank=True)
    facebook = models.CharField(max_length=200, blank=True)
    whatsapp = models.CharField(max_length=200, blank=True)
    instagram = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.team_name


class Worker(models.Model):
    team_logo = models.ImageField(upload_to='upload', blank=True)
    team_name = models.CharField(max_length=200, blank=True)
    team_profession = models.CharField(max_length=200, blank=True)
    facebook = models.CharField(max_length=200, blank=True)
    whatsapp = models.CharField(max_length=200, blank=True)
    instagram = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.team_name


class FeedBack(models.Model):
    name = models.CharField(max_length=200, blank=True)
    email = models.CharField(max_length=200, blank=True)
    website = models.CharField(max_length=200, blank=True)
    product_name = models.CharField(max_length=200, blank=True)
    comment = models.TextField(blank=True)
    facebook = models.CharField(max_length=200, blank=True)
    whatsapp = models.CharField(max_length=200, blank=True)
    instagram = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f'{self.name} --> {self.email} --> {self.product_name}'


class Comment(models.Model):
    name = models.CharField(max_length=200, blank=True)
    email = models.CharField(max_length=200, blank=True)
    date = models.DateTimeField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    text = models.TextField(blank=True)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Sponsors(models.Model):
    sponsor_name = models.CharField(max_length=200, blank=True)
    sponsor_logo = models.ImageField(upload_to='upload', blank=True)

    def __str__(self):
        return f'{self.sponsor_name}'