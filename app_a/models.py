from django.contrib.auth.models import AbstractUser


class Abstract_User_A(AbstractUser):
    class Meta:
        abstract = True


class User_A(Abstract_User_A):
    pass
