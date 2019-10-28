from django.db import models
from PIL import Image

class Menu(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    rating = models.FloatField(default=0)
    votes = models.IntegerField(default=0)
    veg = models.BooleanField(default=True)

    category_choices = (
        (1, 'Starters'),
        (2, 'Main Course'),
        (3, 'Desserts'),
        (4, 'Berverages'),
        (5, 'Misc'),
    )
    category = models.IntegerField(choices=category_choices, default=5)
    image = models.ImageField(default='default.jpg', upload_to='food')

    def __str__(self):
        return f'{self.name}'

    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
