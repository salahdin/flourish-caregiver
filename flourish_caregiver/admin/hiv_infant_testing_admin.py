from django.contrib import admin
from edc_model_admin import audit_fieldset_tuple

from ..admin_site import flourish_caregiver_admin
from ..forms import HIVInfantTestingForm
from ..models import HIVInfantTesting
from .modeladmin_mixins import CrfModelAdminMixin


@admin.register(HIVInfantTesting, site=flourish_caregiver_admin)
class HIVInfantTestingAdmin(CrfModelAdminMixin, admin.ModelAdmin):

    form = HIVInfantTestingForm

    fieldsets = (
        (None, {
            "fields": (
                'maternal_visit',
                'report_datetime',
                'child_tested_for_hiv',
                'child_test_date',
                'child_test_date_estimated',
                'results_received',
                'recall_result_date',
                'receive_date',
                'result_date_estimated',
                'hiv_test_result',
                'reason_child_not_tested',
                'reason_child_not_tested_other',
                'preferred_clinic_for_testing',
                'additional_comments',
            ),
        }),
        audit_fieldset_tuple,
    )

    radio_fields = {
        'child_tested_for_hiv': admin.VERTICAL,
        'child_test_date_estimated': admin.VERTICAL,
        'results_received': admin.VERTICAL,
        'recall_result_date': admin.VERTICAL,
        'result_date_estimated': admin.VERTICAL,
        'hiv_test_result': admin.VERTICAL,
        'reason_child_not_tested': admin.VERTICAL,
        'preferred_clinic_for_testing': admin.VERTICAL,
    }

    search_fields = ('subject_identifier',)
