from django.contrib import admin
from .models import User,Say,Feeling,Article,Coding
from pagedown.widgets import AdminPagedownWidget
from django import forms

class ArticleForm(forms.ModelForm):
    article = forms.CharField(widget=AdminPagedownWidget())

    class Meta:
        model = Coding
        fields = '__all__'

class ArticleAdmin(admin.ModelAdmin):
    form = ArticleForm

admin.site.register(User)
admin.site.register(Say)
admin.site.register(Feeling)
admin.site.register(Article)
admin.site.register(Coding,ArticleAdmin)