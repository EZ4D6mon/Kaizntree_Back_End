# Generated by Django 4.1.9 on 2024-02-13 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_item_created_at_alter_category_id_alter_item_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='sku',
            field=models.CharField(max_length=50),
        ),
    ]