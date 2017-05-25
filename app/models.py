from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    rank_position = models.IntegerField(blank=False, null=False)

    class Meta:
        ordering = ['-rank_position']

    def __str__(self):
        return "%s" % (self.name)