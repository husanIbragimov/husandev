# Generated by Django 4.2.3 on 2025-03-12 07:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='main_images/')),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='aboutme',
            name='address',
            field=models.CharField(blank=True, max_length=225, null=True),
        ),
        migrations.AddField(
            model_name='aboutme',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='aboutme',
            name='birthday',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='aboutme',
            name='degree',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='aboutme',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='aboutme',
            name='interest',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='aboutme',
            name='phone_number',
            field=models.CharField(blank=True, max_length=17, null=True),
        ),
        migrations.AlterField(
            model_name='blogimages',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='blog_images/'),
        ),
        migrations.AlterField(
            model_name='meimages',
            name='blog',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='my_images', to='blog.aboutme'),
        ),
        migrations.AlterField(
            model_name='meimages',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='about/'),
        ),
        migrations.AlterField(
            model_name='resume',
            name='resume',
            field=models.FileField(null=True, upload_to='resume/'),
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.CharField(blank=True, max_length=127, null=True)),
                ('percent', models.IntegerField(default=100)),
                ('blog', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='skills', to='blog.aboutme')),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('experience', models.CharField(blank=True, max_length=50, null=True)),
                ('position', models.CharField(blank=True, max_length=31, null=True)),
                ('period', models.CharField(blank=True, max_length=47, null=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('blog', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='experiences', to='blog.aboutme')),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('education', models.CharField(blank=True, max_length=50, null=True)),
                ('degree', models.CharField(blank=True, max_length=15, null=True)),
                ('period', models.CharField(max_length=15)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('blog', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='educations', to='blog.aboutme')),
            ],
        ),
    ]
