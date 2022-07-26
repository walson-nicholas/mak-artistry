# Generated by Django 3.2.5 on 2021-09-11 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_auto_20210911_1402'),
    ]

    operations = [
        migrations.AddField(
            model_name='illustration',
            name='display_ImgLeft',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='illustration',
            name='display_ImgRear',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='illustration',
            name='display_ImgRight',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='illustration',
            name='display_ImgTop',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='journal',
            name='display_ImgLeft',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='journal',
            name='display_ImgRear',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='journal',
            name='display_ImgRight',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='journal',
            name='display_ImgTop',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='package',
            name='display_ImgLeft',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='package',
            name='display_ImgRear',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='package',
            name='display_ImgRight',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='package',
            name='display_ImgTop',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
