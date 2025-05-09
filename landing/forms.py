from django import forms


class ContactUsForm(forms.Form):
    form_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True, max_length=150)
    content = forms.CharField(required=True, max_length=450, widget=forms.Textarea)
    help_texts = {
        "form_email": 'Your e-mail address',
        "subject": 'Subject',
        "content": 'Type your message here',
    }
    classes = {
        "form_email": 'form-control',
        "subject": 'form-control',
        "content": 'form-control',
    }

    def __init__(self, data=None, files=None, auto_id='id_%s', prefix=None, initial=None,
                 label_suffix=None, empty_permitted=False, field_order=None, use_required_attribute=None,
                 renderer=None):
        super().__init__(data, files, auto_id, prefix, initial, label_suffix, empty_permitted, field_order,
                         use_required_attribute, renderer)
        for field in self.fields.items():
            field[1].widget.attrs['placeholder'] = self.help_texts[field[0]]
            field[1].widget.attrs['class'] = self.classes[field[0]]
            # field[1].widget.attrs['class'] = self.help_texts[field[0]]
