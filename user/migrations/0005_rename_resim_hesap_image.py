# Generated by Django 4.1.3 on 2023-02-20 09:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_hesap'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hesap',
            old_name='resim',
            new_name='image',
        ),
    ]