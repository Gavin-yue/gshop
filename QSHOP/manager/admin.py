from django.contrib import admin

# Register your models here.

from .models import Type

@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display=['id','type_name','date']
    date_hierachy='date'    #根据日期数据进行分类,实现搜索功能
