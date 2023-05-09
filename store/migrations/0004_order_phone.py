from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_order_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='phone',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
    ]
