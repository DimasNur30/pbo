from django.db import models

# Model dasar untuk semua pengguna
class Pengguna(models.Model):
    nama = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    tanggal_bergabung = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True  # Menandakan kelas ini tidak dapat langsung digunakan, hanya untuk diwariskan.

# Model untuk Pengguna Umum yang mewarisi dari Pengguna
class PenggunaUmum(Pengguna):
    total_data = models.IntegerField()

# Model untuk Admin yang mewarisi dari Pengguna
class Admin(Pengguna):
    level = models.CharField(max_length=50)
    akses_admin = models.BooleanField(default=True)
