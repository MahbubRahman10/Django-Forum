# Generated by Django 2.2.2 on 2019-07-04 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_userprofile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='about',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='firstname',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(null=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='lastname',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='tags',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='title',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
