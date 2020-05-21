# Generated by Django 2.2.2 on 2019-07-06 14:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forum', '0004_auto_20190701_2109'),
    ]

    operations = [
        migrations.CreateModel(
            name='Userlike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('reply', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.Reply')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
