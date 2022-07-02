from django.contrib import admin

from .models import Coffeebean, CoffeeKind, Origin, RoastLevel, Method

class CoffeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price')
    list_display_links = ('id', 'name', 'price')


admin.site.register(Coffeebean, CoffeeAdmin)
admin.site.register(CoffeeKind)
admin.site.register(RoastLevel)
admin.site.register(Origin)
admin.site.register(Method)
