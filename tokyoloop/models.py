from django.db import models

# Create your models here.
class Sample(models.Model):
    sample_name = models.CharField(max_length=30)
    cover_art = models.ImageField(upload_to ='uploads/')


def __str__(self):
    return str(self.Sample)

class ClubImage(models.Model):
    image = models.ImageField(upload_to='tokyoloop/images/', blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    update_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.image)
