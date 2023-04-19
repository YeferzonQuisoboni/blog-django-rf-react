# Generated by Django 4.0.6 on 2023-04-19 03:48

import apps.blog.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_uuid', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(unique=True)),
                ('thumbnail', models.ImageField(upload_to=apps.blog.models.blog_directory_path)),
                ('video', models.FileField(blank=True, null=True, upload_to=apps.blog.models.blog_directory_path)),
                ('description', models.TextField()),
                ('excerpt', models.CharField(max_length=100)),
                ('published', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', max_length=10)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='category.category')),
            ],
            options={
                'ordering': ('-published',),
            },
        ),
    ]
