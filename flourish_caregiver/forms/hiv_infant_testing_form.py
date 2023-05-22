from django import forms
# from flourish_form_validations.form_validators import HIVInfantTestingFormValidator

from ..models import HIVInfantTesting
from .form_mixins import SubjectModelFormMixin


class HIVInfantTestingForm(SubjectModelFormMixin, forms.ModelForm):
    # form_validator_cls = HIVInfantTestingFormValidator

    class Meta:
        model = HIVInfantTesting
        fields = '__all__'
