# Generated by Django 3.1.7 on 2021-05-18 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vkeel', '0003_auto_20210518_0743'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='mobile',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='mobile',
            field=models.CharField(blank=True, max_length=10, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='area_of_law',
            field=models.CharField(blank=True, choices=[('Social Law', 'Social Law'), ('Civil Law', 'Civil Law'), ('Healthcare Law', 'Healthcare Law'), ('Cyber Crime Law', 'Cyber Crime Law'), ('Financial Law', 'Financial Law'), ('Corruption Law', 'Corruption Law'), ('Education Law', 'Education Law'), ('Property Law', 'Property Law'), ('Labour Law', 'Labour Law'), ('Criminal Law', 'Criminal Law'), ('Personal Law', 'Personal Law'), ('Environment Law', 'Environment Law')], default='1', max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='city',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
