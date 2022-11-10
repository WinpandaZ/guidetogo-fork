# Generated by Django 2.0.1 on 2022-11-10 06:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tour', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tour',
            name='guide',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='tour_owner', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='tour',
            name='review',
            field=models.ManyToManyField(blank=True, to='tour.Review'),
        ),
        migrations.AddField(
            model_name='review',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='review',
            name='reviewto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviewto', to='tour.Tour'),
        ),
    ]
