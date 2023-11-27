# Generated by Django 4.2.7 on 2023-11-27 05:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("chat", "0002_room"),
    ]

    operations = [
        migrations.AddField(
            model_name="messages",
            name="room",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="chat.room",
            ),
        ),
        migrations.AlterField(
            model_name="room",
            name="room_name",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
