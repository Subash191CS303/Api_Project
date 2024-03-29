# Generated by Django 3.1.5 on 2022-01-23 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PhoneNumber', models.CharField(max_length=200)),
                ('Created', models.DateTimeField(auto_now=True)),
                ('Deleted', models.DateTimeField(auto_now=True)),
                ('Installed', models.BooleanField(blank=True, default=False, null=True)),
            ],
            options={
                'ordering': ['-Created', '-Deleted'],
            },
        ),
    ]
