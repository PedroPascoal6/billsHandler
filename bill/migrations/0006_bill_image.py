# Generated by Django 2.1.3 on 2019-02-19 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bill', '0005_auto_20190113_2243'),
    ]

    operations = [
        migrations.AddField(
            model_name='bill',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='bills/images/'),
        ),
    ]
