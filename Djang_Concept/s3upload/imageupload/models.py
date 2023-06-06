from django.db import models

from imageupload.s3bucket_setup import AWSSignedURL

# Create your models here.
class Image(models.Model):
    name = models.CharField(max_length=50)
    originalImage = models.ImageField(upload_to='images/', max_length=254)
    webpImage = models.ImageField(upload_to='images/', max_length=254)
    pngImage = models.ImageField(upload_to='images/', max_length=254)


    def image(self):
        return {
            "s3_obj": AWSSignedURL.get(
                key=self.webpImage.name
            ),
        }
