# Generated by Django 5.1.1 on 2024-10-08 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_blog_introduction'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='image_link',
            field=models.URLField(blank=True, null=True),
        ),
    ]
