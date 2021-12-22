from django.db import models

# Create your models here.
class Board(models.Model):
    title       = models.CharField(max_length=200)
    contents    = models.TextField()
    writer      = models.ForeignKey('account.Member', on_delete=models.CASCADE)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table            = 'boards'
        verbose_name        = 'board'
        verbose_name_plural = 'boards'