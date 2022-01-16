from django.contrib import admin
from school.models import Student, Fruit

# Register your models here.
class Students(admin.ModelAdmin):
    list_display = ('id','name','rg')
    list_display_links = ('id','name')
    search_fields = ('name',)

class Fruits(admin.ModelAdmin):
    list_display = ('id','name','number','gosto',)
    list_display_links = ('id','name',)
    search_fields = ('name',)

admin.site.register(Student,Students)
admin.site.register(Fruit,Fruits)