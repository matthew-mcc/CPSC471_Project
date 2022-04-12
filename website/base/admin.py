from django.contrib import admin

# Register your models here.
from .models import CPU, GPU, Memory, MotherBoard, Case, AirCooling, LiquidCooling, PowerSupply, Storage, User, Build

admin.site.register(CPU)
admin.site.register(GPU)
admin.site.register(Memory)
admin.site.register(MotherBoard)
admin.site.register(Case)
admin.site.register(AirCooling)
admin.site.register(LiquidCooling)
admin.site.register(PowerSupply)
admin.site.register(Storage)
admin.site.register(Build)
admin.site.register(User)