# Generated by Django 4.2.3 on 2023-07-16 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_Shop', '0004_remove_customer_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='Phonee_number',
            field=models.TextField(default=1, max_length=12),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customer',
            name='Customer_ID',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
