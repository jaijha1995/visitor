# Generated by Django 4.1.1 on 2022-09-18 12:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_rename_signup_contact'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Contact',
            new_name='Signup',
        ),
    ]