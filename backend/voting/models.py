from django.db import models


class Ballot(models.Model):
    STATUS_CHOICES = [("open", "Open"), ("closed", "Closed")]

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    options = models.JSONField()  # e.g. ["Option A", "Option B"]
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="open")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Vote(models.Model):
    ballot = models.ForeignKey(Ballot, on_delete=models.CASCADE, related_name="votes")
    option = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    # No user field — anonymous voting

    def __str__(self):
        return f"Vote for '{self.option}' on ballot {self.ballot_id}"
