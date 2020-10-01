from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.core import validators
from django.core.validators import RegexValidator, validate_email
from django.urls import reverse
from django.contrib.auth.models import User, PermissionsMixin, AbstractUser

from django.utils import timezone


# Create your models here.

class Grado(models.Model):
    grado = models.CharField(max_length=50)

    class Meta:
        db_table = "tr_grado"
        verbose_name = "grado"
        verbose_name_plural = "grados"

    def __str__(self):
        return self.grado


class Materia(models.Model):
    nombre = models.CharField(max_length=50)

    #cursos = models.ManyToManyField(Curso)

    class Meta:
        db_table = "tr_materia"
        verbose_name = "materia"
        verbose_name_plural = "materias"

    def __str__(self):
        return self.nombre


# Create your models here.
class Docente(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    edad = models.IntegerField(default=10)
    email = models.EmailField(default="@itsgg.edu.ec")
    sexo = models.CharField(max_length=1)
    estado = models.IntegerField(default=1)
    user = models.CharField(max_length=15)
    user_mod = models.CharField(max_length=15)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "tr_docente"
        verbose_name = "docente"
        verbose_name_plural = "docentes"

    def __str__(self):
        return self.apellido + ' ' + self.nombre


class Estudiante(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    edad = models.IntegerField(default=10)
    email = models.EmailField(default="@itsgg.edu.ec")
    sexo = models.CharField(max_length=1)
    estado = models.IntegerField(default=1)  # 1 es activo y 2 es eliminado
    user = models.CharField(max_length=20)
    user_mod = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "tr_estudiante"
        verbose_name = "estudiante"
        verbose_name_plural = "estudiantes"

    def __str__(self):
        return self.apellido


class Consulta(models.Model):
    grado = models.ForeignKey(Grado, on_delete=models.CASCADE)
    docente = models.ForeignKey(Docente, on_delete=models.CASCADE)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)

    class Meta:
        db_table = "tr_consulta"
        verbose_name = "consulta"
        verbose_name_plural = "consultas"
