# Generated by Django 2.0.3 on 2018-03-19 11:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0006_auto_20180319_0004'),
    ]

    operations = [
        migrations.AddField(
            model_name='carmodel',
            name='Model',
            field=models.CharField(default=django.utils.timezone.now, max_length=45),
            preserve_default=False,
        ),
    ]
