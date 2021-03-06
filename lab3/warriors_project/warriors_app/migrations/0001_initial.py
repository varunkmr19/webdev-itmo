# Generated by Django 3.1.5 on 2021-01-10 13:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='Name')),
                ('description', models.TextField(verbose_name='Description')),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='Name')),
            ],
        ),
        migrations.CreateModel(
            name='SkillOfWarrior',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.IntegerField(verbose_name='Skill development level')),
                ('skill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='warriors_app.skill', verbose_name='Skill')),
            ],
        ),
        migrations.CreateModel(
            name='Warrior',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('race', models.CharField(choices=[('s', 'student'), ('d', 'developer'), ('t', 'teamlead')], max_length=1, verbose_name='Race')),
                ('name', models.CharField(max_length=120, verbose_name='Name')),
                ('level', models.IntegerField(default=0, verbose_name='Level')),
                ('profession', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='warriors_app.profession', verbose_name='Profession')),
                ('skill', models.ManyToManyField(related_name='warrior_skills', through='warriors_app.SkillOfWarrior', to='warriors_app.Skill', verbose_name='Skills')),
            ],
        ),
        migrations.AddField(
            model_name='skillofwarrior',
            name='warrior',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='warriors_app.warrior', verbose_name='Warrior'),
        ),
    ]
