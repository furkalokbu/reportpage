# Generated by Django 3.2.6 on 2021-09-02 05:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('speed', '0005_speeduserdata'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='speeduserdata',
            options={'ordering': ('user',), 'verbose_name': 'speed'},
        ),
    ]