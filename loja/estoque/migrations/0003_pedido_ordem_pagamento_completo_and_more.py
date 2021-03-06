# Generated by Django 4.0.3 on 2022-03-16 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0002_admin'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido_ordem',
            name='pagamento_completo',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='pedido_ordem',
            name='pagamento_metodo',
            field=models.CharField(choices=[('Dinheiro Na Entrega', 'Dinheiro Na Entrega'), ('Khalti', 'Khalti')], default='Dinheiro Na Entrega', max_length=20),
        ),
    ]
