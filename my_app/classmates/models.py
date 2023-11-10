from django.db import models

class Classmate(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    age = models.IntegerField()
    address = models.CharField(max_length=255)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    picture = models.ImageField(upload_to='classmate_pics/', blank=True, null=True)

    def __str__(self):
        return self.firstname

    def get_absolute_url(self):
        return reverse('classmate_edit', kwargs={'pk': self.pk})

