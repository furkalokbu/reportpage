# Generated by Django 3.2.6 on 2021-09-02 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('speed', '0009_alter_userdata_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='date',
            field=models.DateField(verbose_name='date'),
        ),
    ]