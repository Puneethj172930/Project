# Generated by Django 3.0.6 on 2020-06-06 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20200605_2344'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blooduser',
            old_name='name',
            new_name='first_name',
        ),
        migrations.AddField(
            model_name='blooduser',
            name='last_name',
            field=models.CharField(default='reddy', max_length=200),
        ),
        migrations.AddField(
            model_name='stock',
            name='phone',
            field=models.IntegerField(default=1234),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blooduser',
            name='phone',
            field=models.IntegerField(default='1234'),
        ),
    ]
