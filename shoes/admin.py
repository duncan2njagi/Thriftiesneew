from django.contrib import admin
from . models import Shoe, About, Service, Contact


class ShoeAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'color', 'shoe_size', 'stock')


class AboutAdmin(admin.ModelAdmin):
    list_display = ('who', 'what', 'where', 'why')


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('automation', 'responses')


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'address', 'telephone')


admin.site.register(Service, ServiceAdmin)
admin.site.register(About, AboutAdmin)
admin.site.register(Shoe, ShoeAdmin)