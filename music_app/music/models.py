from django.db import models

#class Artist(models.Model):
    #name = models.CharField(max_length=100)
    #latest_release = models.CharField(max_length=100)
    #top5 = models.CharField(max_length=250)   
    #recommended = models.CharField(max_length=250)
    #def __str__(self):
     #   return 'Artist: ' + self.name + '\nLatest Release: ' + self.latest_release

'''class Album(models.Model):
    album_id = models.AutoField(primary_key=True)
    album_title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    year = models.IntegerField()
    def __str__(self):
        return 'Album: ' + self.album_title + '\nYear: ' + str(self.year)'''

#class Song(models.Model):
    #album = models.ForeignKey(Album,on_delete=models.CASCADE)
    #genre = models.CharField(max_length=50)

