# Generated by Django 4.2.4 on 2024-03-31 00:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0012_alter_listing_wishlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='product',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='bids', to='auctions.listing'),
        ),
    ]
