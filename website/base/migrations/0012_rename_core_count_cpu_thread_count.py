# Generated by Django 4.0.2 on 2022-04-13 20:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_rename_speed_storage_read_speed_storage_write_speed'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cpu',
            old_name='core_count',
            new_name='thread_count',
        ),
    ]
