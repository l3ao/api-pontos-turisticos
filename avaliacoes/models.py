from django.contrib.auth.models import User
from django.db import models


class Comentario(models.Model):
    usuario = models.ForeignKey(User)
    comentario = models.TextField()
    data = models.DateTimeField(auto_now=True)
    aprovado = models.BooleanField(default=True)
    
    def _str__(self):
        return self.usuario.first_name
    