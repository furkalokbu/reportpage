# Generated by Django 3.2.6 on 2021-09-02 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('speed', '0008_auto_20210902_0726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='date',
            field=models.DateTimeField(verbose_name='date'),
        ),
    ]
