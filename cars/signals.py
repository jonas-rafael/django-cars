from django.db.models.signals import pre_save, post_save, post_delete 
from django.db.models import Sum
from django.dispatch import receiver
from cars.models import Car, CarInventory



def car_inventory_update():
    cars_count = Car.objects.all().count()
    cars_value = Car.objects.aggregate(
        total_value=Sum('value')#query de soma
    )['total_value']#ajustando resposta da query
    CarInventory.objects.create(
        cars_count = cars_count,
        cars_value = cars_value   
    )

@receiver(pre_save, sender=Car)
def car_pre_save(sender, instance, **kwargs):
    if not object.bio:
        instance.bio= "bios"


@receiver(post_save, sender=Car)
def car_post_save(render, instance, **kwargs):
    car_inventory_update()

@receiver(post_delete,sender=Car)
def car_post_delete(sender, instance, **kwargs):
    car_inventory_update()    









