# Generated by Django 4.1.3 on 2023-02-20 08:44

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_profile_image_alter_profile_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='slug',
            field=models.SlugField(blank=True, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='id',
            field=models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
