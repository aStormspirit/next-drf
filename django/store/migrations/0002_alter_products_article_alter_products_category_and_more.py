# Generated by Django 4.0.6 on 2022-07-12 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='article',
            field=models.IntegerField(verbose_name='article'),
        ),
        migrations.AlterField(
            model_name='products',
            name='category',
            field=models.CharField(max_length=64, verbose_name='category'),
        ),
        migrations.AlterField(
            model_name='products',
            name='description',
            field=models.TextField(verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='products',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False, verbose_name='id'),
        ),
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.URLField(max_length=300, verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='products',
            name='name',
            field=models.CharField(max_length=64, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='products',
            name='price',
            field=models.IntegerField(verbose_name='price'),
        ),
    ]
