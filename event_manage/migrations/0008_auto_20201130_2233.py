# Generated by Django 3.1.2 on 2020-11-30 20:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('novav1', '0024_auto_20201130_2233'),
        ('event_manage', '0007_auto_20201124_1440'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='Presence',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='events',
            name='session_area',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='novav1.pricing'),
        ),
        migrations.AddField(
            model_name='events',
            name='session_clinic',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='novav1.clinc'),
        ),
        migrations.AddField(
            model_name='events',
            name='session_doctor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='novav1.doctorin'),
        ),
        migrations.AddField(
            model_name='events',
            name='session_end',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='events',
            name='session_used_balls',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='events',
            name='start_session',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]