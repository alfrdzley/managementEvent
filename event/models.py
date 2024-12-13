from django.db import models


# TODO: Event memiliki atribut berikut:
# 		•	title (string, maksimal 100 karakter, tidak boleh kosong)
# 		•	description (teks panjang, opsional)
# 		•	date (tanggal dan waktu event, tidak boleh di masa lalu)
# 		•	location (string, maksimal 150 karakter, tidak boleh kosong)
# 		•	capacity (integer, menunjukkan jumlah peserta maksimal)

class Event(models.Model):
	title = models.CharField(max_length=100)
	description = models.TextField()