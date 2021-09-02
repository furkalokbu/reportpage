# Generated by Django 3.2.6 on 2021-09-02 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('speed', '0007_alter_userdata_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='speeduserdata',
            options={'verbose_name': 'speed'},
        ),
        migrations.AlterModelOptions(
            name='userdata',
            options={'ordering': ('updated_at',), 'verbose_name': 'data user'},
        ),
        migrations.AlterField(
            model_name='userdata',
            name='date',
            field=models.DateField(verbose_name='date'),
        ),
    ]