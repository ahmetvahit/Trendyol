# Generated by Django 4.0.1 on 2022-08-06 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='city_names',
            field=models.CharField(max_length=70, null=True),
        ),
        migrations.AddField(
            model_name='products',
            name='seller_scores',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='products',
            name='sellers_name',
            field=models.CharField(max_length=70, null=True),
        ),
    ]