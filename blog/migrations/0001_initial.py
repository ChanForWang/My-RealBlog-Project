# Generated by Django 3.0.8 on 2020-07-30 21:50

import DjangoUeditor.models
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
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='博客分类')),
                ('index', models.IntegerField(default=999, verbose_name='分类')),
            ],
            options={
                'verbose_name': '博客分类',
                'verbose_name_plural': '博客分类',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='文章标签')),
            ],
            options={
                'verbose_name': '文章标签',
                'verbose_name_plural': '文章标签',
            },
        ),
        migrations.CreateModel(
            name='Tui',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='推荐位')),
            ],
            options={
                'verbose_name': '推荐位',
                'verbose_name_plural': '推荐位',
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70, verbose_name='标题')),
                ('excerpt', models.TextField(blank=True, max_length=200, verbose_name='摘要')),
                ('img', models.ImageField(blank=True, null=True, upload_to='article_img/%Y/%m/%d/', verbose_name='文章图片   ')),
                ('content', DjangoUeditor.models.UEditorField(blank=True, verbose_name='内容')),
                ('views', models.PositiveIntegerField(default=0, verbose_name='阅读量')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='发布时间')),
                ('modified_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('auther', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='作者')),
                ('category', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to='blog.Category', verbose_name='分类')),
                ('tags', models.ManyToManyField(blank=True, to='blog.Tag', verbose_name='标签')),
                ('tui', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='blog.Tui', verbose_name='推荐位')),
            ],
            options={
                'verbose_name': '文章',
                'verbose_name_plural': '文章',
            },
        ),
    ]