from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.


class UserAccountManager(BaseUserManager):

    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email,
                         password):
        user = self.create_user(
            email=self.normalize_email(email),
            password = password

        )
        #user.set_password(password)
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user
class User(AbstractBaseUser):
    email = models.EmailField(max_length=200,unique=True)
    USERNAME_FIELD = 'email'
    # 'username', 'first_name', 'last_name', 'gender'
    REQUIRED_FIELDS = ['password']
    objects = UserAccountManager()