# Generated by Django 3.1.4 on 2020-12-17 09:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fbooks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('search', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('number', models.CharField(default='', max_length=100)),
                ('fbooks', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='Fbooks', to='Fbooks.fbooks')),
            ],
        ),
    ]
