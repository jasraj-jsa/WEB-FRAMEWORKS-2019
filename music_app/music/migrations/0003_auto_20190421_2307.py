# Generated by Django 2.1.7 on 2019-04-21 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_auto_20190421_2302'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('latest_release', models.CharField(max_length=100)),
                ('top5', models.CharField(max_length=250)),
                ('recommended', models.CharField(max_length=250)),
            ],
        ),
        migrations.DeleteModel(
            name='Artists',
        ),
    ]
