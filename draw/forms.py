from django import forms
from .models import Draw


DRAW_CHOICES = [
    ('팀엑스', '팀엑스'),
    ('공장', '공장'),
    ('뮤', '뮤'),
    ('소프', '소프'),
    ('아키', '아키'),
    ('작공', '작공'),
    ('비작', '비작')
]


class DrawForm(forms.ModelForm):
    class Meta:
        model = Draw
        fields = ['first', 'second', 'third']
        widgets = {
            'first': forms.RadioSelect(attrs={'class': 'form-check-inline text-white'}, choices=DRAW_CHOICES),
            'second': forms.RadioSelect(attrs={'class': 'form-check-inline text-white'}, choices=DRAW_CHOICES),
            'third': forms.RadioSelect(attrs={'class': 'form-check-inline text-white'}, choices=DRAW_CHOICES),
        }
        labels = {
            'first': '1지망',
            'second': '2지망',
            'third': '3지망',
        }
