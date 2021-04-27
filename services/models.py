from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator


class Services(models.Model):
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def no_of_ratings(self):
        ratings = Review.objects.filter(service=self)
        return len(ratings)

    def avg_rating(self):
        sum = 0
        ratings = Review.objects.filter(service=self)
        for rating in ratings:
            sum += rating.stars

        if len(ratings) > 0:
            avg = sum / len(ratings)
            return round(avg, 1)
        else:
            return 0

    def __str__(self):
        return self.name


class Review(models.Model):
    """Model to define the fields required to review a product"""
    stars = models.PositiveSmallIntegerField(validators=[MaxValueValidator(5)],
                                             null=False, default=0)
    title = models.CharField(max_length=100)
    review_text = models.TextField()
    date_reviewed = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ForeignKey(Services, on_delete=models.CASCADE)

    def __str__(self):
        return self.review_text
