from django.contrib import admin

from main.models import Category, Product

# Register your models here.

admin.site.register(Category)


# admin.site.register(Product)

@admin.register(Product)
class Products(admin.ModelAdmin):
    list_display = ('title', 'category',)

    def count_of_phones(self, obj):
        print(self)
        print(obj, '!!!!!!!!!!!!!!!!!!!!!!!!!')
        qt = obj.category.all()
        print(qt, '!!!!!!!!!!!!!!!!!!!!')
        return qt

    # def list_of_phones(self, obj):
    #     print(self)
    #     ls = [x for x in obj.category.all()]
    #     return ls
