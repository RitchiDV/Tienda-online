# Generated by Django 4.0.4 on 2022-05-20 03:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0002_categoriap_producto_delete_shop'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='producto',
            options={'verbose_name': 'producto', 'verbose_name_plural': 'productos'},
        ),
        migrations.AddField(
            model_name='producto',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='producto',
            name='updated',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
