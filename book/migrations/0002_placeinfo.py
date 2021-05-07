# Generated by Django 3.2 on 2021-04-29 05:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlaceInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_title', models.CharField(max_length=20)),
                ('k', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='book.placeinfo')),
            ],
        ),
    ]
