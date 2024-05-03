from django.db import models
from accounts.models import User
# Create your models here.

class UserSnapSetting(models.Model):
    client_id = models.CharField(max_length=700)
    redirect_uri = models.CharField(max_length=700)
    account_id = models.CharField(max_length=700)
    user_id = models.OneToOneField(User,on_delete=models.CASCADE)
    class Meta:
        verbose_name = "UserSnapSetting"
        verbose_name_plural = "UserSnapSettings"
    def __str__(self):
        return "Account Id: " + str(self.account_id)

class UserSnapToken(models.Model):
    code = models.CharField(max_length=700)
    access_token = models.CharField(max_length=900)
    refresh_token = models.CharField(max_length=900)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated_at = models.DateTimeField(auto_now=True)
    user_id = models.OneToOneField(User,on_delete=models.CASCADE)

