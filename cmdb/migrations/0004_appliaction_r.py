# Generated by Django 2.1.5 on 2019-07-03 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0003_auto_20190703_1050'),
    ]

    operations = [
        migrations.AddField(
            model_name='appliaction',
            name='r',
            field=models.ManyToManyField(to='cmdb.Host'),
        ),
    ]