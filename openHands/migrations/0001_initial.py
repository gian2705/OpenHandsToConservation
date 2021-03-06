# Generated by Django 2.1 on 2018-08-14 08:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=64, null=True, verbose_name='Name')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('user_contribution', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('content', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('uploaded_media', models.FileField(default='mediafiles/Ubuntu.jpg', upload_to='', verbose_name='Image or Video')),
                ('image_caption', models.TextField(verbose_name='Image or Video caption')),
                ('posted_by', models.ForeignKey(auto_created=True, default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'News Post',
                'verbose_name_plural': 'News Posts',
            },
        ),
    ]
