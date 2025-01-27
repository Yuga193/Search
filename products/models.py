# search_project/products/models.py

from django.db import models

class Product(models.Model):
    COLOR_CHOICES = [
        ('', '白'),
        (1, '赤'),
        (2, '青'),
        (3, '黄'),
        (4, '緑'),
        (5, '紫'),
        (6, 'オレンジ'),
        (7, 'ピンク'),
    ]
    # ... existing code ...
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)
    background_color = models.IntegerField(choices=COLOR_CHOICES, blank=True, null=True)
    stock = models.IntegerField(default=0)  # stockフィールドを追加

    def __str__(self):
        return self.name
    
    def get_background_color_code(self):
        color_map = {
            1: '#ff0000',
            2: '#0000ff',
            3: '#ffff00',
            4: '#008000',
            5: '#800080',
            6: '#ffa500',
            7: '#ffc0cb',
        }
        return color_map.get(self.background_color, '#ffffff')