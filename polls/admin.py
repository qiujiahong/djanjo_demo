from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Question, Choice


# 定义Choice的布局文件
# class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):  # 不换行
    model = Choice
    extra = 3


# 定义Question的布局文件
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    # 定义对象的嵌入
    inlines = [ChoiceInline]
    # 添加显示table行信息
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    # 添加过滤器
    list_filter = ['pub_date']
    # 为question_text 添加一个搜索框
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice)
