# Generated by Django 3.0.5 on 2020-04-17 07:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MessageTo',
            fields=[
                ('message_id', models.AutoField(primary_key=True, serialize=False)),
                ('content', models.TextField()),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('user_id_from', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userfromto', to=settings.AUTH_USER_MODEL)),
                ('user_id_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userto', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('message_id', models.AutoField(primary_key=True, serialize=False)),
                ('content', models.TextField()),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('user_id_from', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userfrom', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]