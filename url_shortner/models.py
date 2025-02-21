from django.db import models
import random
import string

def generate_short_code():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

class ShortURL(models.Model):
    long_url = models.URLField(null=False, blank=False)  
    short_code = models.CharField(max_length=10, unique=True, default=generate_short_code)  
    created_at = models.DateTimeField(auto_now_add=True)  
    click_count = models.IntegerField(default=0)  
    is_active = models.BooleanField(default=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.short_code} -> {self.long_url}"