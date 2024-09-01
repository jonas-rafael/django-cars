from django.contrib import admin
from cars.models import Car, Brand

class CarAdmin(admin.ModelAdmin):
    list_display = ('model','brand','factory_year','model_year', 'value')#criando cadatro de carro para o painel admin
    search_fields = ('model',)#habilitando busca


class BrandAdmin(admin.ModelAdmin):
    list_display=('name',)
    search_fields=('name',)


admin.site.register(Car, CarAdmin)# registrando no painel que o modelo car vai usar car admin
admin.site.register(Brand, BrandAdmin)