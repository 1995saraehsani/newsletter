# Generated by Django 3.1.14 on 2022-05-29 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newspage', '0005_auto_20220529_0258'),
    ]

    operations = [
        migrations.AddField(
            model_name='authorpoliticpage',
            name='title',
            field=models.CharField(default=' ', max_length=250),
            preserve_default=False,
        ),
    ]
