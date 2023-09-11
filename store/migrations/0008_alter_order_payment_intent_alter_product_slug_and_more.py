# Generated by Django 4.2.4 on 2023-08-30 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_rename_merchant_id_order_payment_intent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='payment_intent',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(max_length=300),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(max_length=300),
        ),
    ]
