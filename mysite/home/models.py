from django.db import models
from django.contrib.auth.models import User
'''
class DataUpload(models.Model):
    jenis_upload = (
        ('buku', 'Kecil'),
        ('jurnal', 'Medium'),
    )

    
    judul = models.CharField(max_length = 100,default=None)
    jenis_upload =  models.CharField(max_length = 100,choices=jenis_upload,default=None, null=True)
    tahun_terbit =  models.IntegerField(default=2017)

    def __str__(self): 
        return self.judul 
      
class Images(models.Model):
    post = models.ForeignKey(DataUpload, default=None, on_delete=models.CASCADE, related_name= 'images')
    image = models.ImageField(upload_to = 'gambar/', blank=True, null = True)
    def __str__(self):
        return self.post.judul + " Image"

'''