# Generated by Django 4.0.1 on 2022-03-14 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0003_post_intro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='intro',
            field=models.TextField(),
        ),
    ]
