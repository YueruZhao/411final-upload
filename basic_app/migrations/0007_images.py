# Generated by Django 2.1.7 on 2019-03-28 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0006_editid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='background_image')),
            ],
        ),
    ]
