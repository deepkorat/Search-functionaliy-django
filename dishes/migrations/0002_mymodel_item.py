# Generated by Django 4.2.1 on 2023-06-29 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dishes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mymodel',
            name='item',
            field=models.TextField(default='{}'),
        ),
    ]
