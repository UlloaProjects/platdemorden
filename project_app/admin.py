from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from project_app.models import User,Product,ProductDemand
# Register your models here.

admin.site.register(User, UserAdmin)
admin.site.register(Product)
admin.site.register(ProductDemand)
