# Generated by Django 2.1.1 on 2018-09-03 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_auto_20180902_1437'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.CharField(default='未设置', max_length=200),
            preserve_default=False,
        ),
    ]
