# Generated by Django 4.2.3 on 2023-07-31 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0004_alter_project_members'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='phone',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Номер телефона'),
        ),
    ]
