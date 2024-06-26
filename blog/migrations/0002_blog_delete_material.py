# Generated by Django 5.0.4 on 2024-04-27 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Заголовок')),
                ('body', models.TextField(verbose_name='Содержание')),
            ],
            options={
                'verbose_name': 'Блог>',
                'verbose_name_plural': 'Блоги',
                'ordering': ('id',),
            },
        ),
        migrations.DeleteModel(
            name='Material',
        ),
    ]
