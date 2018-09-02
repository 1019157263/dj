from django.db import models

# Create your models here.
class Question(models.Model):
    
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    class Meta:
        #末尾不加s
        verbose_name_plural='标签'
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
    def __str__(self):
        return self.question_text   
 
     


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0) 
    class Meta:
        #末尾不加s
        verbose_name_plural='数据'
    def __str__(self):
        return self.choice_text
        
        
class user(models.Model):
    username = models.CharField(max_length=200,primary_key=True)
    pwd = models.CharField(max_length=200)
    def __str__(self):
        return self.username