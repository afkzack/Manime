from django.db import models
from django.utils.timezone import datetime

class Episode(models.Model):
	name = models.CharField(max_length=100, null=True, blank=True)
	ep_num = models.DecimalField(null=True, blank=True, max_digits=5, decimal_places=1)

	def __str__(self):
		return self.name + " | Episode - " + str(self.ep_num)

class Watch(models.Model):
	link = models.URLField(null=True, blank=True)
	episode = models.ForeignKey(Episode, default=None, on_delete=models.CASCADE)

	def __str__(self):
		return self.episode.name+ " | Episode - "+ str(self.episode.ep_num)

class Genre(models.Model):
	name = models.CharField(max_length=100, null=True, blank=True)

	def __str__(self):
		return self.name

class Status(models.Model):
	name = models.CharField(max_length=100, null=True, blank=True)

	def __str__(self):
		return self.name

class Studio(models.Model):
	name = models.CharField(max_length=100, null=True, blank=True)

	def __str__(self):
		return self.name

class Anime(models.Model):
	name = models.CharField(max_length=200, null=True, blank=True)
	photo = models.ImageField(null=True, blank=True, upload_to='images/')
	eps = models.ManyToManyField(Episode, blank=True)
	cover = models.ImageField(blank=True, null=True, upload_to='images/')
	pub_date = models.DateTimeField('date published')
	genre = models.ManyToManyField(Genre, blank=True)
	status = models.ForeignKey(Status, default=None, on_delete=models.CASCADE)
	studio = models.ForeignKey(Studio, default=None, on_delete=models.CASCADE)
	summary = models.TextField(null=True, blank=True)

	def was_published_today(self):
		#now = datetime.now()
		#dt_string = now.strftime("%Y")
		#return self.pub_date.date() == dt_string
		return self.pub_date.date() == datetime.date.today()
		self.save()

	def __str__(self):
		return self.name
