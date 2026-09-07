import uuid

from django.db import models


class Product(models.Model):
    ## Still a placeholder
    CATEGORY_CHOICES = [
        ("transfer", "Transfer"),
        ("update", "Update"),
        ("exclusive", "Exclusive"),
        ("match", "Match"),
        ("rumor", "Rumor"),
        ("analysis", "Analysis"),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField(default=0)
    description = models.TextField()
    thumbnail = models.URLField(blank=True, null=True)
    category = models.CharField(
        max_length=20, choices=CATEGORY_CHOICES, default="update"
    )
    is_featured = models.BooleanField(default=False)
    rating = models.PositiveIntegerField(default=0, max_length=5)
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

    @property
    def is_item_hot(self):
        return self.views > 20

    def increment_views(self):
        self.views += 1
        self.save()
