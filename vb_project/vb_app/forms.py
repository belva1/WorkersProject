from django import forms
from django.core.exceptions import ValidationError

from .models import Worker


class WorkerForm(forms.ModelForm):
    class Meta:
        model = Worker  # in the form will display all fields from this model
        fields = ('fullname', 'mobile', 'work_code', 'position')
        labels = {
            'fullname': 'Full Name',
            'work_code': 'Work Code',
        }

    # to customize the text that appears in the Select dropdown list for a ForeignKey or ChoiceField field on a form.
    def __init__(self, *args, **kwargs):
        super(WorkerForm, self).__init__(*args, **kwargs)
        self.fields['position'].empty_label = 'Select'

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if name and any(char.isdigit() for char in name):
            raise ValidationError('Name should not contain digits.')

        return name

    def clean_second_name(self):
        second_name = self.cleaned_data.get('second_name')
        if second_name and any(char.isdigit() for char in second_name):
            raise ValidationError('Second name should not contain digits.')

        return second_name




