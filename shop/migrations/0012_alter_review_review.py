# Generated by Django 4.2.1 on 2023-06-03 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_review_user_alter_order_customer_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='review',
            field=models.CharField(max_length=1024),
        ),
    ]
