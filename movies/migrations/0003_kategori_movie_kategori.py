# Generated by Django 4.2.3 on 2023-10-29 18:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_alter_movie_resim'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kategori',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isim', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='movie',
            name='kategori',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='movies.kategori'),
        ),
    ]
