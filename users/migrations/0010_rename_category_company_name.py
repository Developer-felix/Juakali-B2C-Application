# Generated by Django 3.2.8 on 2022-06-15 15:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20220615_0835'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='category',
            new_name='name',
        ),
    ]
