from django import forms
from .models import Draw


DRAW_CHOICES = [
    ('팀엑스', '팀엑스'),
    ('공간과장소', '공간과장소'),
    ('뮤', '뮤'),
    ('소프', '소프'),
    ('아키', '아키'),
    ('작은공간', '작은공간'),
    ('비작업실', '비작업실')
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
