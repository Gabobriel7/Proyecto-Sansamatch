# Generated by Django 5.1.2 on 2024-11-03 23:46

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('matches', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='grupo',
            name='usuarios',
            field=models.ManyToManyField(related_name='grupos', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='like',
            name='usuario_destino',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes_recibidos', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='like',
            name='usuario_origen',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes_dados', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='match',
            name='usuario1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='match_usuario1', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='match',
            name='usuario2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='match_usuario2', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='like',
            unique_together={('usuario_origen', 'usuario_destino')},
        ),
    ]
