from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("stock", "0127_alter_stockitemtestresult_options"),
    ]

    operations = [
        migrations.AddField(
            model_name="stockitem",
            name="manufacturer_serial",
            field=models.CharField(
                blank=True,
                help_text="Serial number assigned by the manufacturer",
                max_length=100,
                null=True,
                verbose_name="Manufacturer Serial Number",
            ),
        ),
    ]
