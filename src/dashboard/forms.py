from django import forms


class InterviewerSelectForm(forms.Form):
    interviewer = forms.ChoiceField(
        choices=[],
        label="Enquêteur",
        widget=forms.Select(attrs={'id': 'interviewer-id'})
    )

    def __init__(self, *args, **kwargs):
        interviewer_choices = kwargs.pop('interviewer_choices', [])
        super().__init__(*args, **kwargs)
        self.fields['interviewer'].choices = interviewer_choices
