# Generated by Django 3.1.7 on 2021-05-18 04:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vkeel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='area_of_law',
            field=models.CharField(blank=True, choices=[('Corruption Law', 'Corruption Law'), ('Labour Law', 'Labour Law'), ('Personal Law', 'Personal Law'), ('Social Law', 'Social Law'), ('Financial Law', 'Financial Law'), ('Environment Law', 'Environment Law'), ('Healthcare Law', 'Healthcare Law'), ('Property Law', 'Property Law'), ('Cyber Crime Law', 'Cyber Crime Law'), ('Criminal Law', 'Criminal Law'), ('Education Law', 'Education Law'), ('Civil Law', 'Civil Law')], default='1', max_length=100),
        ),
        migrations.CreateModel(
            name='ActiveChat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('chat_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chat_user', to=settings.AUTH_USER_MODEL)),
                ('chat_user2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chat_user2', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
