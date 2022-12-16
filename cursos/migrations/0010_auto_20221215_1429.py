# Generated by Django 3.2.16 on 2022-12-15 17:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0009_alter_turma_instrutor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aluno',
            name='rg',
        ),
        migrations.RemoveField(
            model_name='candidato',
            name='rg',
        ),
        migrations.RemoveField(
            model_name='responsavel',
            name='r_rg',
        ),
        migrations.AlterField(
            model_name='responsavel',
            name='r_aluno',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cursos.candidato'),
        ),
    ]