# Generated by Django 3.1.4 on 2020-12-28 08:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Fbooks', '0002_auto_20201217_1109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='fbooks',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='information', to='Fbooks.fbooks'),
        ),
    ]
