from django import forms

class AddSubForm(forms.Form):
    as_min = forms.IntegerField(label = "Min", required=True, widget=forms.TextInput(attrs={'placeholder': 'Min.','class':'num_input'}))
    as_max = forms.IntegerField(label = "Max", required=True, widget=forms.TextInput(attrs={'placeholder': 'Max.', 'class':'num_input'}))

class MultDivForm1(forms.Form):
    md_min1 = forms.IntegerField(label = "Min", required=True, widget=forms.TextInput(attrs={'placeholder': 'Min.','class':'num_input'}))
    md_max1 = forms.IntegerField(label = "Max", required=True, widget=forms.TextInput(attrs={'placeholder': 'Max.', 'class':'num_input'}))

class MultDivForm2(forms.Form):
    md_min2 = forms.IntegerField(label = "Min", required=True, widget=forms.TextInput(attrs={'placeholder': 'Min.','class':'num_input'}))
    md_max2 = forms.IntegerField(label = "Max", required=True, widget=forms.TextInput(attrs={'placeholder': 'Max.', 'class':'num_input'}))

possible_durations = [('30','30 Seconds'), ('60','60 Seconds'),
           ('120', '120 Seconds'), ('300', '300 Seconds'),
           ('600','600 Seconds')]
class Duration(forms.Form):
    duration = forms.CharField(label='Duration:', widget=forms.Select(choices=possible_durations))
    