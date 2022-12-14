# Generated by Django 4.0.4 on 2022-09-09 12:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_cart_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_logo', models.ImageField(blank=True, upload_to='upload')),
                ('team_name', models.CharField(blank=True, max_length=200)),
                ('team_profession', models.CharField(blank=True, max_length=200)),
                ('facebook', models.CharField(blank=True, max_length=200)),
                ('whatsapp', models.CharField(blank=True, max_length=200)),
                ('instagram', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='cart',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 9, 18, 38, 47, 936128)),
        ),
    ]
