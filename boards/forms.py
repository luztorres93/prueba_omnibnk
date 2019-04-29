from django import forms
from boards.models import movie

class MovieForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea(), max_length=4000)

    class Meta:
        model = movie
        fields = ['name',
                  'description',
                  'score',
                  'category',
                  'image']
        labels = {'name' : 'Title',
                  'description': 'Description',
                  'score': 'Score',
                  'category' :'Category',
                  'image' :'image'}
        
        widgets = {'name' : forms.TextInput(attrs={'class':'form-control'}),
                  'description':forms.Textarea(attrs={'class':'form-control', 'rows': '5', 'id' :'textareaDesc'}),
                  'score':forms.NumberInput(attrs={'class':'form-control', 'min' :1, 'max':10}),
                   'image' : forms.FileInput(attrs={'class':'form-control'}),
                  'category' :forms.Select(attrs={'class':'form-control'})}
        
    def get_absolute_url(self):
        return ('home', [self.slug, ])
    

class searchForm(forms.ModelForm):
    
    text_search = forms.CharField(label='Search:', max_length=100)