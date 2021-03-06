# Generated by Django 2.2.12 on 2021-07-31 18:46

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('plant_base', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='leaves',
            name='shape',
        ),
        migrations.AddField(
            model_name='leaves',
            name='shapes',
            field=multiselectfield.db.fields.MultiSelectField(max_length=200, null=True, verbose_name=models.CharField(choices=[('AR', 'Arrow-Shaped'), ('CP', 'Compound'), ('DL', 'Deltoid'), ('HT', 'Heart-Shaped'), ('LA', 'Lanecolate'), ('LI', 'Linear'), ('LB', 'Lobed'), ('OB', 'Oblong'), ('OL', 'Oval'), ('TL', 'Three-leaved')], max_length=2)),
        ),
    ]
