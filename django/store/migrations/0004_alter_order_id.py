# Generated by Django 4.0.6 on 2022-07-14 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
