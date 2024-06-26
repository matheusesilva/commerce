# Generated by Django 4.2.4 on 2024-03-27 19:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_bid_category_comment_delete_bids_delete_comments_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bid',
            name='product',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='auctions.listing'),
        ),
        migrations.AddField(
            model_name='comment',
            name='product',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='auctions.listing'),
        ),
    ]
