from django import forms

"""Write a simple form for the Plan model with two fields option_1 and option_2

Both fields must be choice fields with Yes/No options (the values are not important)

We want to present these choice fields as radio buttons on the view."""
CHOICES = [
    [0, "Yes"],
    [1, "No"]
]

class PlanForm(forms.Form):
    option_1 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    option_2 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
