from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import(
        AbstractBaseUser,
        PermissionsMixin,
        BaseUserManager
    )
    
class MyUserManager(BaseUserManager):
    """ClientManager."""

    def create_user(
        self,
        email: str,
        password: str
    ) -> 'MyCustomUser':

        if not email:
            raise ValidationError('Email required')

        custom_user: 'MyCustomUser' = self.model(
            email=self.normalize_email(email),
            password=password
        )
        custom_user.set_password(password)
        custom_user.save(using=self._db)
        return custom_user

    def create_superuser(
        self,
        email: str,
        password: str
    ) -> 'MyCustomUser':

        custom_user: 'MyCustomUser' = self.model(
            email=self.normalize_email(email),
            password=password
        )
        custom_user.is_superuser = True
        custom_user.is_active = True
        custom_user.is_staff = True
        custom_user.set_password(password)
        custom_user.save(using=self._db)
        return custom_user


class MyCustomUser(AbstractBaseUser, PermissionsMixin):
    """My Custom User Model"""

    username = models.CharField(
        verbose_name='имя',
        max_length=120
    )

    email = models.EmailField(
        verbose_name='почта',
        unique=True,
        max_length=200
    )
    
    phone_number = models.CharField(
        verbose_name='номер телефона',
        max_length=10
    )

    is_staff = models.BooleanField(
        default=False
    )

    objects = MyUserManager()

    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'

    class Meta:
        ordering = ['-id']
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'