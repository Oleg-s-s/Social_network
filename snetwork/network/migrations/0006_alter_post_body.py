# Generated by Django 4.1.1 on 2022-10-05 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0005_post_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='body',
            field=models.CharField(max_length=100),
        ),
    ]
