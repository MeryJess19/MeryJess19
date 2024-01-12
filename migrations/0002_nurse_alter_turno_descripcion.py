from django.db import migrations, models

class Migration(migrations.Migration):
    dependencies = [
        ('AppEnfermeria', '0001_initial'),
    ]

    operations = [

        migrations.CreateModel(
            name='Nurse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=100)),
                ('Apellido', models.CharField(max_length=100)),
                ('Profesion', models.CharField(max_length=100)),
                ('fecha_ingreso', models.DateField()),
            ],
        ),

        migrations.AlterField(
            model_name='turno',
            name='descripcion',
            field=models.CharField(max_length=255),
        ),

        migrations.AddField(
            model_name='turno',
            name='Nombre',
            field=models.CharField(default='', max_length=200),
            preserve_default=False, 
        ),
    ]
