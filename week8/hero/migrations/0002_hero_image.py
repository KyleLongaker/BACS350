# Generated by Django 3.2.7 on 2021-11-03 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hero', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hero',
            name='image',
            field=models.CharField(default='image', max_length=200),
            preserve_default=False,
        ),
    ]
