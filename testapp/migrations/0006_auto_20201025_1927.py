# Generated by Django 3.1.2 on 2020-10-25 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0005_auto_20201025_1926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='name',
            field=models.CharField(max_length=124),
        ),
    ]
