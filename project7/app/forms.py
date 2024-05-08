from django import forms 
from app.models import *

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = '__all__'
        
class  WebsiteForm(forms.ModelForm):
    class Meta:
        model = Website
        fields = '__all__'
        
class AccessForm(forms.ModelForm):
    class Meta:
        model = Access
        fields = '__all__'
     
        