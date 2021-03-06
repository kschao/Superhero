from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Superhero', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='superhero',
            name='alter_ego_name',
            field=models.CharField(default=5, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='superhero',
            name='catchphrase',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='superhero',
            name='prim_ability',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='superhero',
            name='second_ability',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='superhero',
            name='superheros_names',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]