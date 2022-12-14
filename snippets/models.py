from unittest.util import _MAX_LENGTH
from django.contrib.auth.models import AbstractUser as BaseUser
from django.db import models

# Create your models here.
class User(BaseUser):
    # could add customer user attributes here
    pass

class Snippet(models.Model):
    code = models.TextField()
    description = models.CharField(max_length=512)
    language = models.ForeignKey('Language', 
    on_delete=models.CASCADE, related_name="snippets", blank=True, null=True)
    # related name should be the plural of the model that is in. This is a 02M relationship.
    # A snippet has one user and the user has many snippets.
    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="snippets")
    users = models.ManyToManyField('User', related_name='snippets')
    author = models.ForeignKey('User', on_delete=models.CASCADE, related_name="user_snippet")
    parent = models.ForeignKey('Snippet', on_delete=models.SET_NULL, related_name="fork",
        blank=True, null=True)
    
    
    def __str__(self):
        return f'{self.description} in {self.language} created by {self.author}'
    
    def is_user_favorite(self, user):
        for favorite in self.favorites.all():
            if favorite.snippet == self:
                return True
            
    
class Language(models.Model):
    name = models.CharField(max_length=255)
    version = models.FloatField(blank=True, null=True)
    
    def __str__(self):
        return f'{self.name} {self.version}'
    
    
class Favorite(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="favorites")
    snippet = models.ForeignKey("Snippet", on_delete=models.CASCADE, related_name="favorites")
    create_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.user}: {self.snippet}'