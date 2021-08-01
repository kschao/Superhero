from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Superhero', '0002_auto_20210603_1454'),
    ]

    operations = [
        migrations.AddField(
            model_name='superhero',
            name='superhero_picture',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='superhero',
            name='catchphrase',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='superhero',
            name='prim_ability',
            field=models.CharField(max_length=75),
        ),
        migrations.AlterField(
            model_name='superhero',
            name='second_ability',
            field=models.CharField(max_length=75),
        ),
    ]