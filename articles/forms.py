from django import forms
from .models import article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = article
        fields = ['title','content']

    def clean(self):
        data = self.cleaned_data
        title = data.get('title')
        qs = article.objects.all().filter(title__icontains=title)
        if qs.exists():
            self.add_error("title",f"This title \"{title}\" already taken")
        return data


class ArticleFormOld(forms.Form):
    title = forms.CharField(max_length=50)
    content = forms.CharField(max_length=100)

    def clean_title(self):
        title = self.cleaned_data.get('title')
        # print("clean data",title) #here content will none because clean_title
        if title.lower() == "test":
            self.add_error("title","This article has been taken") #field error
            raise forms.ValidationError("Invalid Input!") #entire field error->field-error 
        return title

    def clean(self):        
        cleaned_data = self.cleaned_data
        print("clean",cleaned_data)
        return cleaned_data