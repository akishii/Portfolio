from django.db import models

# Create your models here.
class Racedata(models.Model):
    
    #Racedataテーブルに各フィールドを作成
    year_id = models.IntegerField()
    race_id = models.IntegerField()
    arr_no = models.IntegerField()
    horse_no = models.IntegerField()
    horsename = models.CharField(max_length=20)
    age = models.CharField(max_length=10)
    weight = models.FloatField()
    jockey = models.CharField(max_length=10)
    trainer = models.CharField(max_length=10)
    time = models.CharField(max_length=10)
    lasttime = models.FloatField()
    odds = models.IntegerField()

    #各レコードの値を返す処理
    def __str__(self):
        return (str(self.arr_no), str(self.horse_no),
                self.horsename, self.age, str(self.weight),
                self.jockey, self.trainer, self.time,
                str(self.lasttime), str(self.odds))