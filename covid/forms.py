from django.forms import ModelForm, Textarea
from covid.models import Questions

class QuestionForm(ModelForm):
    class Meta:
        model = Questions
        fields = ['ques']
        widgets = {
            'ques': Textarea(attrs={'cols': 40, 'rows': 6}),
        }