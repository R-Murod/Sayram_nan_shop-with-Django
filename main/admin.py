from django.contrib import admin
from main.models import *


# Register your models here.


class AdminModelSingle(admin.ModelAdmin):
    pass


admin.site.register(Size, AdminModelSingle)
admin.site.register(Category, AdminModelSingle)
admin.site.register(Product, AdminModelSingle)
admin.site.register(CategoryBrand, AdminModelSingle)
admin.site.register(Cart, AdminModelSingle)
admin.site.register(CartItem, AdminModelSingle)
admin.site.register(CompareItem, AdminModelSingle)
admin.site.register(WishItem, AdminModelSingle)
admin.site.register(AboutUs, AdminModelSingle)
admin.site.register(Team, AdminModelSingle)
admin.site.register(FeedBack, AdminModelSingle)
admin.site.register(Comment, AdminModelSingle)
admin.site.register(Sponsors, AdminModelSingle)
admin.site.register(Worker, AdminModelSingle)
