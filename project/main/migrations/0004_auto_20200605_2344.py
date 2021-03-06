# Generated by Django 3.0.6 on 2020-06-05 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_blooduser'),
    ]

    operations = [
        migrations.CreateModel(
            name='stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=200)),
                ('A_positive', models.BooleanField(default=True)),
                ('A_negative', models.BooleanField(default=True)),
                ('B_positive', models.BooleanField(default=True)),
                ('B_negative', models.BooleanField(default=True)),
                ('O_positive', models.BooleanField(default=True)),
                ('O_negative', models.BooleanField(default=True)),
                ('AB_positive', models.BooleanField(default=True)),
                ('AB_negative', models.BooleanField(default=True)),
            ],
        ),
        migrations.DeleteModel(
            name='tutorial',
        ),
    ]
