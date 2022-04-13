# Generated by Django 4.0.2 on 2022-04-12 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_build_alter_user_build_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
        migrations.RemoveField(
            model_name='build',
            name='build_id',
        ),
        migrations.AddField(
            model_name='build',
            name='build_user',
            field=models.CharField(default='test_user', max_length=50, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
