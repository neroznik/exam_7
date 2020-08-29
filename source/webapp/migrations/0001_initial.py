# Generated by Django 2.2 on 2020-08-29 05:50

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(max_length=2000, verbose_name='Вопрос')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Время создания')),
            ],
            options={
                'verbose_name': 'Poll',
                'verbose_name_plural': 'Polls',
            },
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option', models.TextField(max_length=2000, verbose_name='Вариант ответа')),
                ('poll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='poll', to='webapp.Poll', verbose_name='Опрос')),
            ],
        ),
    ]