# Generated by Django 2.2.5 on 2022-07-20 10:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True, verbose_name='书籍')),
                ('pub_date', models.DateField(null=True, verbose_name='发布日期')),
                ('read_count', models.IntegerField(default=0, verbose_name='阅读人数')),
                ('comment_count', models.IntegerField(default=0, verbose_name='评论条数')),
                ('is_delete', models.BooleanField(default=False, verbose_name='已被删除')),
            ],
            options={
                'verbose_name': '书籍管理',
                'db_table': 'bookinfo',
            },
        ),
        migrations.CreateModel(
            name='PersonInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True, verbose_name='姓名')),
                ('gender', models.SmallIntegerField(choices=[(0, 'unknown'), (1, 'male'), (2, 'female')], default=0, verbose_name='性别')),
                ('description', models.CharField(max_length=100, null=True, verbose_name='描述')),
                ('is_delete', models.BooleanField(default=False, verbose_name='已被删除')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.BookInfo', verbose_name='书籍')),
            ],
            options={
                'verbose_name': '人物信息',
                'db_table': 'personinfo',
            },
        ),
    ]
