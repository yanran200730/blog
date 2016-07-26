from django.db import models
from django.utils import timezone
import json

# 创建表结构

class PersonManager(models.Manager):
	"""docstring for Person"""
	def get_by_natural_key(self, username):
		return self.get(username=username)
		

class User(models.Model):
	objects = PersonManager()
	username = models.CharField("User's name ", max_length=50)
	passwd = models.CharField("User's password ", max_length=50)
	email = models.EmailField("User's email address ", max_length=50)
	date = models.DateTimeField(default=timezone.now)

	def natural_key(self):
		return (self.username)
			
	def __str__(self):
		return self.username



#每日一言
class Say(models.Model):
	saying = models.CharField("Saying everday ",max_length=50)
	date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.saying

#说说
class Feeling(models.Model):
	person = models.ForeignKey(User)
	img = models.ImageField(upload_to="img")
	feeling = models.CharField("说说 ",max_length=200)
	createTime = models.DateTimeField(default=timezone.now)
	like_times = models.IntegerField(default=0)

	def __str__(self):
		return self.person.username

#文字
class Article(models.Model):
	author = models.ForeignKey(User)
	img = models.ImageField(upload_to="img")
	createTime = models.DateTimeField(default=timezone.now)
	article = models.TextField('文章')
	tag = models.CharField("标签",max_length=10)
	title = models.CharField("标题",max_length=20)
	view_count = models.IntegerField("浏览次数",default=0)
	praise_count = models.IntegerField("点赞次数",default=0) 

	def __str__(self):
		return self.author.username

	# def toJSON(self):
	# 	fields = []
	# 	dicts = {}
	# 	for field in self._meta.fields:
	# 		fields.append(field.name)
	# 	url = getattr(getattr(self,'img'),"url")
	# 	img = url.replace("media","static")
	# 	username = getattr(getattr(self,'author'),'username')
	# 	time = getattr(self,'createTime').strftime('%Y-%m-%d %H:%M:%S')
	# 	for attr in fields:
	# 		if attr != 'img' and attr !='author' and attr !='createTime':
	# 			dicts[attr] = getattr(self,attr)
	# 	dicts['img'] = img	
	# 	dicts["username"] = username
	# 	dicts["time"] = time
	# 	return json.dumps(dicts)

class Coding(models.Model):
	author = models.ForeignKey(User)
	article = models.TextField('文章')
	img = models.ImageField(upload_to="img",null=True,blank=True)
	createTime = models.DateTimeField(default=timezone.now)
	tag = models.CharField("标签",max_length=20)
	title = models.CharField("标题",max_length=50)
	view_count = models.IntegerField("浏览次数",default=0)
	praise_count = models.IntegerField("点赞次数",default=0)

	def __str__(self):
		return self.author.username


