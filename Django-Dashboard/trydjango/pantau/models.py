from django.db import models

# Create your models here.
class MonitoringData(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    suhu = models.CharField(max_length=10)
    kelembaban = models.CharField(max_length=10)
    co2 = models.CharField(max_length=20)
    gas_lpg = models.CharField(max_length=20)
    gas_alkohol = models.CharField(max_length=20)
    cahaya = models.CharField(max_length=20)
    jumlah_orang = models.IntegerField()
    kebisingan = models.CharField(max_length=10)
    tegangan = models.CharField(max_length=20)
    arus = models.CharField(max_length=20)
    daya = models.CharField(max_length=20)