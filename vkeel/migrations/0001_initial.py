# Generated by Django 3.1.7 on 2021-05-07 13:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid
import vkeel.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_advocate', models.BooleanField(default=False)),
                ('is_user', models.BooleanField(default=False)),
                ('image', models.ImageField(blank=True, default='user.png', null=True, upload_to='userimage/')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('name', models.CharField(blank=True, max_length=30, verbose_name='name')),
                ('city', models.CharField(blank=True, max_length=30)),
                ('mobile', models.CharField(blank=True, max_length=10, null=True, unique=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatars/')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            managers=[
                ('objects', vkeel.manager.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.IntegerField(default=0)),
                ('query', models.TextField(max_length=500)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dob', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('gender', models.CharField(blank=True, default='', max_length=20)),
                ('state', models.CharField(blank=True, default='', max_length=30)),
                ('pincode', models.CharField(blank=True, default='', max_length=10)),
                ('address', models.TextField(blank=True, default='', max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='userprofile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reviewer', models.CharField(default='', max_length=100)),
                ('rate', models.IntegerField(default=0, null=True)),
                ('post', models.TextField(default='', max_length=500)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default='', max_length=200)),
                ('question_description', models.TextField(blank=True, default='', max_length=1000)),
                ('area_of_law', models.CharField(blank=True, choices=[('Healthcare Law', 'Healthcare Law'), ('Corruption Law', 'Corruption Law'), ('Environment Law', 'Environment Law'), ('Property Law', 'Property Law'), ('Education Law', 'Education Law'), ('Labour Law', 'Labour Law'), ('Criminal Law', 'Criminal Law'), ('Cyber Crime Law', 'Cyber Crime Law'), ('Personal Law', 'Personal Law'), ('Social Law', 'Social Law'), ('Financial Law', 'Financial Law'), ('Civil Law', 'Civil Law')], default='1', max_length=100)),
                ('date_posted', models.DateTimeField(null=True)),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='InstantAdvice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=20)),
                ('ammount', models.IntegerField(blank=True, default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('mobile', models.IntegerField(default=0)),
                ('advocate', models.EmailField(max_length=254)),
                ('transaction_id', models.UUIDField(db_index=True, default=uuid.uuid4, unique=True)),
                ('user', models.ForeignKey(blank=True, max_length=200, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Follower',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('follower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follower', to=settings.AUTH_USER_MODEL)),
                ('following', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='following', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EducationModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(default='', max_length=50)),
                ('college_name', models.CharField(default='', max_length=50)),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='educationalprofile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CaseProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('case_title', models.CharField(default='', max_length=150)),
                ('case_year', models.DateField(null=True)),
                ('case_law', models.CharField(choices=[('1', '---------'), ('2', 'a'), ('3', 'b'), ('4', 'c'), ('5', 'd'), ('6', 'e'), ('7', 'f'), ('8', 'g')], default='', max_length=50)),
                ('case_description', models.TextField(default='', max_length=1000)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='caseprofile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reply', models.TextField(max_length=2000, null=True)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vkeel.question')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AdvocateProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dob', models.CharField(blank=True, default='', max_length=50)),
                ('gender', models.CharField(blank=True, default='', max_length=20, null=True)),
                ('state', models.CharField(blank=True, default='', max_length=30)),
                ('pincode', models.CharField(blank=True, default='', max_length=10)),
                ('address', models.TextField(blank=True, default='', max_length=100, null=True)),
                ('language_spoken', models.CharField(blank=True, default='', max_length=200)),
                ('enrollment_number', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('practicing_since', models.CharField(blank=True, default='', max_length=100)),
                ('bio', models.TextField(blank=True, default='', max_length=1000, null=True)),
                ('service_cities', models.JSONField(blank=True, default=list, null=True)),
                ('area_of_law', models.JSONField(blank=True, default=list, null=True)),
                ('visiting_courts', models.JSONField(blank=True, default=list, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
