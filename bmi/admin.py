from django.contrib import admin
from bmi.models import Userdata, Suggestion

# Register your models here.

# admin.site.register(Product)


@admin.register(Userdata)
class ProductAdmin(admin.ModelAdmin):
    list_display=("height", "weight", "bmi","bmi_category", "user",)
    

admin.site.register(Suggestion)