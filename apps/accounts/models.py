
"""
Definido ja no inicio do projeto porque trocar AUTH_USER_MODEL depois da primeira
migracao irá forçar reset do banco. Manter esse modelo aqui, mesmo simples.
"""
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    class Papel(models.TextChoices):
        PRODUTOR= "produtor", "Produtor"
        TECNICO = "tecnico", "Tecnico"
        ADMIN = "admin", "Administrador"

    email = models.EmailField("e-mail", unique=True)
    papel = models.CharField(
        max_length=20,
        choices=Papel.choices,
        default=Papel.PRODUTOR,
    )

    # Login por email e mais natural pro produtor em campo
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    class Meta:
        verbose_name = "usuario"
        verbose_name_plural = "usuarios"

    def __str__(self) -> str:
        return self.email or self.username

