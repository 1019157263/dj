from django.contrib import admin

# Register your models here.
from .models import Question,Choice,user
#from .models import Choice

#admin.site.register(Choice)
'''
class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question_text']
'''
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3



'''
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('标题:选择时间', {'fields': ['pub_date']}),
    ]
'''
class QuestionAdmin(admin.ModelAdmin):
    list_filter = ['pub_date']#过滤器
    search_fields = ['question_text']
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]#显示顺序
    inlines = [ChoiceInline]#编辑选择
#    list_filter = ['pub_date']

    list_display = ('question_text', 'pub_date','was_published_recently')
     #显示多个

#admin.site.register(Question, QuestionAdmin)




class userAdmin(admin.ModelAdmin):
    list_filter = ['time']#过滤器
    search_fields = ['username']
    fieldsets = [
          ('时间', {'fields': ['time']}),
        ('用户名',               {'fields': ['username']}),
        ('密码', {'fields': ['pwd']}),
    ]#显示顺序和标题
    list_display = ( 'username','time',)
  #  lines = [ChoiceInline]
     #显示多个
    
    
    
    
    
    
    
    
    
 


admin.site.register(Question,QuestionAdmin)
admin.site.register(Choice)
admin.site.register(user,userAdmin)