# Generated by Django 4.1 on 2022-08-19 08:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Airport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('code', models.CharField(max_length=3)),
            ],
        ),
        migrations.AlterField(
            model_name='flight',
            name='dest',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dest', to='flights.airport'),
        ),
        migrations.AlterField(
            model_name='flight',
            name='origin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='origin', to='flights.airport'),
        ),
    ]
