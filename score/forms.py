from django import forms

class ScoreQueryForm(forms.Form):
    """成績查詢表單"""
    admit_number = forms.CharField(
        label='准考證號碼',
        max_length=10,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '請輸入准考證號碼'})
    )
    id_last_4_digits = forms.CharField(
        label='身份證末四碼',
        max_length=4,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '請輸入身份證末四碼'})
    )