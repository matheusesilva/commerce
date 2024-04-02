# Generated by Django 4.2.4 on 2024-03-30 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0009_alter_listing_max_bid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='price',
            new_name='initial_price',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='endDate',
        ),
        migrations.AddField(
            model_name='listing',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='listing',
            name='max_bid',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
    ]
