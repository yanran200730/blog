from django.db import models
import datetime

# 创建表结构
class User(models.Model):
    username = models.CharField("User's name ", max_length=50)
    passwd = models.CharField("User's password ", max_length=50)
    email = models.EmailField("User's email address ", max_length=50)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username

#每日一言
class Say(models.Model):
	saying = models.CharField("Saying everday ",max_length=50)
	date = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.saying

#说说
class Feeling(models.Model):
	person = models.ForeignKey(User)
	img = models.ImageField(upload_to="img")
	feeling = models.CharField("说说 ",max_length=200)
	createTime = models.DateTimeField(auto_now=True)
	like_times = models.IntegerField(default=0)

	def __str__(self):
		return self.person.username

