# Generated by Django 5.0.1 on 2024-03-01 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_alter_product_flag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='flag',
            field=models.CharField(choices=[('Feature', 'feature'), ('Sale', 'sale'), ('New', 'new')], max_length=10, verbose_name='flag'),
        ),
    ]
