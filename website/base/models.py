from django.db import models

# Create your models here.



class Build(models.Model):
    #build_id = models.IntegerField(primary_key=True)
    build_user = models.CharField(primary_key=True, max_length=50)
    name = models.CharField(max_length=50)
    total_price = models.IntegerField()
    build_cpu = models.CharField(max_length=50)
    build_gpu = models.CharField(max_length=50)
    build_motherboard = models.CharField(max_length=50)
    build_psu = models.CharField(max_length=50)
    build_ram = models.CharField(max_length=50)
    build_storage1 = models.CharField(max_length=50)
    build_storage2 = models.CharField(max_length=50)
    build_case = models.CharField(max_length=50)
    build_liquidCooling = models.CharField(max_length=50)
    build_airCooling = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Recipient(models.Model):
    email = models.CharField(max_length=50)
    build_id = models.CharField(max_length=50)

class CPU(models.Model):
    model_name = models.CharField(primary_key=True, max_length=50)
    price = models.IntegerField()
    
    power_usage = models.IntegerField()
    graphics = models.CharField(max_length=100)
    chipset = models.CharField(max_length=50)
    thread_count = models.IntegerField()
    core_clock = models.CharField(max_length=20)

    def __str__(self):
        return self.model_name

class GPU(models.Model):
    model_name = models.CharField(primary_key=True, max_length=50)
    price = models.IntegerField()
    power_usage = models.IntegerField()
    architecture = models.CharField(max_length=50)
    chipset = models.CharField(max_length=50)
    vram = models.CharField(max_length=100)
    ports = models.CharField(max_length=50)
    bus_slots = models.CharField(max_length=50)
    core_count = models.IntegerField()
    core_clock = models.CharField(max_length=20)

    def __str__(self):
        return self.model_name

class MotherBoard(models.Model):
    model_name = models.CharField(primary_key=True, max_length=50)
    price = models.IntegerField()
    power_usage = models.IntegerField()
    form_factor = models.CharField(max_length=50)
    chipset = models.CharField(max_length=50)
    ports = models.CharField(max_length=50)
    storage_capability = models.CharField(max_length=50)
    pci_slots = models.CharField(max_length=50)
    memory_type = models.CharField(max_length=50)
    audio = models.CharField(max_length=50)
    bluetooth = models.CharField(max_length=50)
    lan = models.CharField(max_length=50)
    wireless = models.CharField(max_length=50)

    def __str__(self):
        return self.model_name

class PowerSupply(models.Model):
    model_name = models.CharField(primary_key=True, max_length=50)
    price = models.IntegerField()
    modularity = models.CharField(max_length=50)
    output = models.CharField(max_length=50)

    def __str__(self):
        return self.model_name

class Memory(models.Model):
    model_name = models.CharField(primary_key=True, max_length=50)
    price = models.IntegerField()
    power_usage = models.CharField(max_length=50)
    size = models.CharField(max_length=50)
    speed = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    no_sticks = models.IntegerField()
    
    def __str__(self):
        return self.model_name

class Storage(models.Model):
    model_name = models.CharField(primary_key=True, max_length=50)
    price = models.IntegerField()
    power_usage= models.CharField(max_length=50)
    storage_size = models.CharField(max_length=50)
    read_speed = models.CharField(max_length=50)
    write_speed = models.CharField(max_length=50)
    form_factor =models.CharField(max_length=50)
    
    def __str__(self):
        return self.model_name

class Case(models.Model):
    model_name = models.CharField(primary_key=True, max_length=50)
    price = models.IntegerField()
    chassis_type = models.CharField(max_length=50)
    form_factor =models.CharField(max_length=50)
    top_radiator = models.CharField(max_length=50)
    rear_radiator = models.CharField(max_length=50)
    front_radiator = models.CharField(max_length=50)

    def __str__(self):
        return self.model_name

class LiquidCooling(models.Model):
    model_name = models.CharField(primary_key=True, max_length=50)
    price = models.IntegerField()
    radiator_size = models.CharField(max_length=50)
    location = models.CharField(max_length=50)

    def __str__(self):
        return self.model_name

class AirCooling(models.Model):
    model_name = models.CharField(primary_key=True, max_length=50)
    price = models.IntegerField()
    height = models.CharField(max_length=50)
    fan_output = models.CharField(max_length=50)
    fan_speed = models.CharField(max_length=50)

    def __str__(self):
        return self.model_name