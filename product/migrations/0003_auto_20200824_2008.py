# Generated by Django 3.0.6 on 2020-08-24 20:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0002_auto_20200811_1548'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='like_users',
            field=models.ManyToManyField(related_name='like_product', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='review',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review', to='product.Product'),
        ),
    ]