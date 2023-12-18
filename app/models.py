from django.db import models



class Car(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='car_images/')  # Using ImageField for images

    def __str__(self):
        return self.name


class UserText(models.Model):
    text_content = models.TextField()

    def __str__(self):
        return self.text_content