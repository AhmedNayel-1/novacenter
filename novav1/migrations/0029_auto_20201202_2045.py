# Generated by Django 3.1.2 on 2020-12-02 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('novav1', '0028_auto_20201202_0219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='ref_code',
            field=models.CharField(default='3YMXALLNXKDZG7JEEHHJ', max_length=20),
        ),
    ]