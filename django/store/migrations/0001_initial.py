# Generated by Django 4.0.6 on 2022-07-12 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('article', models.IntegerField()),
                ('name', models.CharField(max_length=64)),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('category', models.CharField(max_length=64)),
                ('image', models.URLField(max_length=300)),
            ],
        ),
    ]
