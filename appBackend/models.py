from djongo import models
from django.utils import timezone
# from markdownx.models import MarkdownxField


# Create your models here.

class Room(models.Model):
  user_id = models.ManyToManyField('users.CustomUser')
  name = models.CharField('ルーム名', max_length=100)
  objects = models.DjongoManager()

  def __str__(self):
    return self.name

class Talk(models.Model):
  user_id = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
  room_id = models.ForeignKey(Room, on_delete=models.CASCADE)
  content = models.CharField(max_length=500, default=None)
  created_at = models.DateTimeField(default=timezone.now)

  def __str__(self):
    return (f'{self.created_at}')