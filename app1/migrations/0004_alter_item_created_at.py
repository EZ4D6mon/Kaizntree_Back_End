# Generated by Django 4.1.9 on 2024-02-13 03:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_alter_item_sku'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
