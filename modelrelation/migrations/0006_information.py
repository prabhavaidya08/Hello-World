# Generated by Django 3.0.8 on 2020-07-15 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelrelation', '0005_userdetail_country'),
    ]

    operations = [
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
                ('info', models.CharField(max_length=100)),
                ('bio', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
