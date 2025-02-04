from django.db import models


class Pengguna(models.Model):
    nama = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    tanggal_bergabung = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True  


class PenggunaUmum(Pengguna):
    total_data = models.IntegerField()

class Admin(Pengguna):
    level = models.CharField(max_length=50)
    akses_admin = models.BooleanField(default=True)
