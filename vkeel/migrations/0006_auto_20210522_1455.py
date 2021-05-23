# Generated by Django 3.1.7 on 2021-05-22 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vkeel', '0005_auto_20210518_0923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='area_of_law',
            field=models.CharField(blank=True, choices=[('Criminal Law', 'Criminal Law'), ('Cyber Crime Law', 'Cyber Crime Law'), ('Personal Law', 'Personal Law'), ('Corruption Law', 'Corruption Law'), ('Property Law', 'Property Law'), ('Labour Law', 'Labour Law'), ('Social Law', 'Social Law'), ('Healthcare Law', 'Healthcare Law'), ('Civil Law', 'Civil Law'), ('Environment Law', 'Environment Law'), ('Education Law', 'Education Law'), ('Financial Law', 'Financial Law')], default='1', max_length=100),
        ),
    ]
