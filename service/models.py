from abc import ABCMeta, abstractmethod
from django.db import models
from django.utils import timezone
# Create your models here.

class Entity(models.Model):
    created_date = models.DateTimeField('date created')
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name
    # @abstractmethod
    # def save_to_file(self):
        # return

    # @abstractmethod
    # def load_from_file(self):
        # return
    class Meta:
        abstract = True

class App(Entity):
    pass

class Skill(Entity):
    active = models.BooleanField(default=False)
    app = models.ForeignKey(App,on_delete=models.CASCADE)

class Intent(Entity):
    handler = models.CharField(max_length=50)
    skill=models.ForeignKey(Skill,on_delete=models.CASCADE)

class Material(Entity):
    class Meta:
        abstract = True
    intent = models.ForeignKey(Intent,on_delete=models.CASCADE)
    content = models.TextField(max_length=2000)
    
class Vocab(Material):
    require = models.BooleanField(default=True)

class Regex(Material):
    pass

class Dialog(Material):
    pass
