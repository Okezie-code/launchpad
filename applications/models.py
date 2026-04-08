from django.db import models

class Application(models.Model):
    company = models.CharField(max_length = 60)
    role = models.CharField(max_length=200)
    date_applied = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[("Applied", "Applied"), ("Interviewing", "Interviewing"), ("Rejected", "Rejected"), ("Offer", "Offer")])


    def __str__(self):
        return self.company