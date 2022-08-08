from edc_list_data import PreloadData
from edc_constants.constants import NONE, OTHER

list_data = {
    'flourish_caregiver.chronicconditions': [
        ('mhist_asthma', 'Asthma'),
        ('mhist_hyperten', 'Hypertension'),
        ('mhist_hyperchole', 'Hypercholesterolemia'),
        ('mhist_heart', 'Heart disease'),
        ('mhist_hepb_pos', 'Hepatitis B surface Ag positive'),
        ('mhist_hepb_carrier', 'Chronic Hepatitis B carrier'),
        ('mhist_hepc', 'Hepatitis C'),
        ('mhist_diab', 'Diabetes'),
        ('mhist_other', 'Other, Specify'),
        ('mhist_na', 'Not Applicable')
    ],
    'flourish_caregiver.wcsdxadult': [
        ('who_asympt', 'Asymptomatic'),
        ('who_lymphadeno', 'Persistent generalized lymphadeno'),
        ('who_mod_wloss', 'Unexplained moderate weight loss'),
        ('who_resptract', 'Recurrent resp tract infection'),
        ('who_herpeszost', 'Herpes zoster'),
        ('who_cheilitis', 'Angular cheilitis'),
        ('who_oral_ulcer', 'Recurrent oral ulceration'),
        ('who_papular_pruri', 'Papular pruritic eruptions'),
        ('who_dermatit', 'Seborrhoeic dermatitis'),
        ('who_fungal', 'Fungal nail infections'),
        ('who_sev_wloss', 'Unexplained* severe weight loss'),
        ('who_fev', 'Unexplained persistent fever'),
        ('who_diarr', 'Unexplained chronic diarrhoea'),
        ('who_oral_candid', 'Persistent oral candidiasis'),
        ('who_leukoplakia', 'Oral hairy leukoplakia'),
        ('who_pulm_tb', 'Pulmonary tuberculosis'),
        ('who_bactinfect', 'Severe bacterial infections'),
        ('who_stomatit', 'Stomatitis/gingivitis/periodontis'),
        ('who_anemia', 'Anaemia/neutropaenia/thrombocytopa'),
        ('who_hivwaste', 'HIV wasting syndrome'),
        ('who_pneumonia', 'Pneumocystis pneumonia'),
        ('who_bact_pneumo', 'Recurrent severe bacterial pneumo'),
        ('who_herpesinfec', 'Chronic herpes simplex infection'),
        ('who_oeso_candid', 'Oesophageal candidiasis'),
        ('who_extpulm_tb', 'Extrapulmonary tuberculosis'),
        ('who_kaposi_carc', 'Kaposi\u2019s sarcoma'),
        ('who_cytomeg', 'Cytomegalovirus infection'),
        ('who_cns', 'CNS toxoplasmosis'),
        ('who_hivenceph', 'HIV encephalopathy'),
        ('who_meningitis', 'Exp cryptococcosis/meningitis'),
        ('who_dissnon_tb', 'Diss non-TB mycobacterial infection'),
        ('who_leukoence', 'Prog multifocal leukoencephalopathy'),
        ('who_crypto', 'Chronic cryptosporidiosis'),
        ('who_isospor', 'Chronic isosporiasis'),
        ('who_mycosis', 'Disseminated mycosis'),
        ('who_septica', 'Recurrent septicaemia'),
        ('who_lymphoma', 'Lymphoma'),
        ('who_cerv_carc', 'Invasive cervical carcinoma'),
        ('who_leishman', 'Atypical disseminated leishmaniasis'),
        ('who_cardiomy', 'Sympt nephropathy/cardiomyopathy'),
        ('who_na', 'Not Applicable'),
    ],
    'flourish_caregiver.caregivermedications': [
        ('mmed_na', 'Not Applicable'),
        ('mmed_cholest', 'Cholesterol medications'),
        ('mmed_vitd', 'Vitamin D supplement'),
        ('mmed_trad_medic', 'Traditional medications'),
        ('mmed_hyper', 'Hypertensive medications'),
        ('mmed_prenatal_vit', 'Prenatal Vitamins'),
        ('mmed_diabetic', 'Diabetic medications'),
        ('mmed_asthmatic', 'Anti-asthmatic drugs'),
        ('mmed_depress', 'Antidepressant drugs'),
        ('mmed_anxiety', 'Anti-anxiety drugs'),
        ('mmed_hep', 'Anti-hepatitis medications'),
        ('mmed_heart', 'Heart disease medications'),
        ('mmed_3tc', '3TC'),
        ('mmed_truvada', 'Truvada'),
        ('mmed_efv', 'Efavirenz'),
        ('mmed_dtg', 'DTG'),
        ('mmed_atripla', 'Atripla'),
        ('mmed_comb3tc_azt', 'Combivir. (3TC,. AZT),'),
        ('mmed_nevirapine', 'Nevirapine'),
        ('mmed_aluvia', 'Aluvia'),
        ('mmed_abacavir', 'Abacavir'),
        ('mmed_tenofovir', 'Tenofovir'),
        ('mmed_tld', 'TLD (TDF,3TC, DTG)'),
        ('mmed_raltearavir', 'Raltearavir'),
        ('mmed_other', 'Other, Specify'),
        ('mmed_none', 'None'),
    ],
    'flourish_caregiver.deliverycomplications': [
        ('delivery_comp_ruptur', 'Uterine rupture'),
        ('delivery_comp_hemorr', 'Hemorrhage req. transfusion'),
        ('delivery_comp_preeclamp', 'Pre-eclampsia/eclampsia'),
        ('delivery_comp_previa', 'Placenta previa'),
        ('delivery_comp_abrupt', 'Placental abruption'),
        ('delivery_comp_chorio', 'Chorioamnioitis or sus. chorioamnionitis'),
        ('delivery_comp_fev', 'Intrapartum fever'),
        ('delivery_comp_other', 'Other'),
        ('delivery_comp_none', 'None')
    ],
    'flourish_caregiver.phonenumtype': [
        ('cell_phone', 'Cell Phone'),
        ('cell_phone_alt', 'Cell Phone (alternative)'),
        ('telephone', 'Telephone'),
        ('telephone_alt', 'Telephone (alternative)'),
        ('work_contact', 'Work contact number'),
        ('alt_person_cell', 'Alternative contact person cell phone'),
        ('alt_person_tel', 'Alternative contact person telephone'),
        ('resp_person_cell', 'Responsible person cell phone'),
        ('resp_person_tel', 'Responsible person telephone'),
        (NONE, 'None')
    ],
    'flourish_caregiver.priorarv': [
        ('prior_arv_azt', 'AZT'),
        ('prior_arv_ddi', 'DDI'),
        ('prior_arv_kaletra', 'Kaletra (or Aluvia)'),
        ('prior_arv_nevirapine', 'Nevirapine'),
        ('prior_arv_3tc', '3TC'),
        ('prior_arv_atripla', 'Atripla'),
        ('prior_arv_tenofovir', 'Tenofovir'),
        ('prior_arv_truvada', 'Truvada (Tenofovir, FTC)'),
        ('prior_arv_atz', 'ATZ'),
        ('prior_arv_d4t', 'D4T'),
        ('prior_arv_raltegravir', 'Raltegravir'),
        ('prior_arv_efv', 'Efavirenz (or Sustiva)'),
        ('prior_arv_combivir', 'Combivir (AZT, 3TC)'),
        ('prior_arv_trizivir', 'Trizivir (AZT, 3TC, Abacavir)'),
        ('prior_arv_abacavir', 'Abacavir'),
        ('prior_arv_dtg', 'DTG'),
        ('prior_arv_unknown', 'ART, unknown'),
        ('prior_arv_na', 'Not Applicable'),
        ('prior_arv_other', 'Other, specify')
    ],
    'flourish_caregiver.covidsymptoms': [
        ('c19m_iso_chestpain', 'Chest pain'),
        ('c19m_iso_chills', 'Chills'),
        ('c19m_iso_cough', 'Cough'),
        ('c19m_iso_diarr ', 'Diarrhea '),
        ('c19m_iso_fev', 'Fever > 37.5 Degree Celsius'),
        ('c19m_iso_aches', 'Muscle aches'),
        ('c19m_iso_nasal', 'Nasal Congestion'),
        ('c19m_iso_nausea', 'Nausea/vomiting'),
        ('c19m_iso_sob', 'Shortness of breath'),
        ('c19m_iso_throat', 'Sore throat'),
        ('c19m_iso_headache', 'Headache'),
        ('c19m_iso_losssmell', 'Loss of Smell'),
        ('c19m_iso_losstaste', 'Loss of Taste'),
        ('c19m_iso_nosympt', 'No Symptoms'),
    ],
    'flourish_caregiver.covidsymptomsafter14days': [
        ('c19m_14d_chestpain', 'Chest pain'),
        ('c19m_14d_chills', 'Chills'),
        ('c19m_14d_cough', 'Cough'),
        ('c19m_14d_diarr ', 'Diarrhea '),
        ('c19m_14d_fev', 'Fever > 37.5 Degree Celsius'),
        ('c19m_14d_aches', 'Muscle aches'),
        ('c19m_14d_nasal', 'Nasal Congestion'),
        ('c19m_14d_nausea  ', 'Nausea/vomiting'),
        ('c19m_14d_sob', 'Shortness of breath'),
        ('c19m_14d_throat', 'Sore throat'),
        ('c19m_14d_headache', 'Headache'),
        ('c19m_14d_losssmell', 'Loss of Smell'),
        ('c19m_14d_losstaste', 'Loss of Taste'),
        ('c19m_14d_nosympt', 'No Symptoms'),
    ],
    'flourish_caregiver.maternaldiagnoseslist': [
        ('mdiag_pneumonia', 'Pneumonia'),
        ('mdiag_chlamydia', 'Chlamydia'),
        ('mdiag_tb', 'Tuberculosis'),
        ('mdiag_depression', 'Depression'),
        ('mdiag_preeclamp', 'Pre-eclampsia'),
        ('mdiag_gonorrhea', 'Gonorrhea'),
        ('mdiag_liver', 'Liver Problems'),
        ('mdiag_hepc', 'Hepatitis C'),
        ('mdiag_syphillis', 'Syphillis'),
        ('mdiag_asthma', 'Asthma requiring steroids'),
        ('mdiag_herpes', 'Genital Herpes'),
        ('mdiag_hyperten', 'Gestational Hypertension'),
        ('mdiag_na', 'Not Applicable'),
        ('mdiag_other', 'Other, specify')
    ],
    'flourish_caregiver.caregiversocialworkreferrallist': [
        ('refer_argument', 'Arguments with partner/spouse'),
        ('refer_violence', 'Violence with partner/spouse'),
        ('refer_distrust', 'Distrust with partner/spouse'),
        ('refer_finances', 'Financial challenges'),
        ('refer_diagnosis',
         'Difficultly dealing with diagnoses of chronic illness or infectious disease'),
        ('refer_grief', 'Grief counseling (for loss of loved one)'),
        ('refer_adherence', 'Adherence counseling'),
        ('refer_other', 'Other, specify')
    ],
    'flourish_caregiver.pregnancyinfluencerslist': [
        ('the_father', 'The father of the child'),
        ('maternal_family_members', 'Members of my family '),
        ('paternal_family_members', 'Family members of the father of my child'),
        ('anc_staff', 'The ANC staff'),
        ('no_one', 'No other individual influenced my feeding choice decision'),
        (OTHER, 'Other, specify'),
    ],
    'flourish_caregiver.afterpregnancyinfluencerslist': [
        ('the_father', 'The father of the child'),
        ('maternal_family_members', 'Members of my family '),
        ('paternal_family_members', 'Family members of the father of my child'),
        ('anc_staff', 'The ANC staff'),
        ('no_one', 'No other individual influenced my feeding choice decision'),
        (OTHER, 'Other, specify'),
    ],
    'flourish_caregiver.receivedtrainingonfeedinglist': [
        ('antenatal_clinic', 'ANC'),
        ('labour_delivery_ward', 'Labour and Delivery Ward'),
        ('maternatiy_ward', 'Maternity Ward after delivery'),
        ('flourish_team', 'The FLOURISH study team'),
        (NONE, 'None'),
    ],
    'flourish_caregiver.reasonsforinfantfeedinglist': [
        ('no_time_for_breastfeeding', 'I did not have time to breastfeed'),
        ('returned_work_school', 'I had to return to school/work'),
        ('unable_to_produce_enough_milk',
         'I was not able to produce enough breastmilk to keep my infant satisfied'),
        ('infant_refused_breastmilk', 'My infant refused breastmilk'),
        ('painfull_breastfeeding', 'Breastfeeding was too painful'),
        ('cracked_bleeding_nipples', 'My nipples were cracked and/or bleeding'),
        ('did_not_like_breast_shape',
         'I did not like the way breastfeeding changed my breast shape'),
        ('wanted_to_give_infant_traditional_medicine',
         'I wanted to give traditional medicines to my infant'),
        (OTHER, 'Other, specify'),
    ],
}

preload_data = PreloadData(
    list_data=list_data)
