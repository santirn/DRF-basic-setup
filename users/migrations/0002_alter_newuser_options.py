# Generated by Django 4.0.4 on 2022-04-29 09:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='newuser',
            options={'verbose_name': 'User', 'verbose_name_plural': 'Users'},
        ),
    ]