# Generated by Django 4.0.5 on 2022-07-02 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coffeebeans', '0003_coffeebean_kind_coffeebean_origin_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coffeebean',
            name='kind',
            field=models.CharField(max_length=15, null=True),
        ),
    ]