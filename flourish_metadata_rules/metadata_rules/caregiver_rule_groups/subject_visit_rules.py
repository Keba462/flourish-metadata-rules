from edc_metadata import NOT_REQUIRED, REQUIRED
from edc_metadata_rules import CrfRule, CrfRuleGroup, register
from ...predicates import CaregiverPredicates

app_label = 'flourish_caregiver'
pc = CaregiverPredicates()


@register()
class MaternalVisitRuleGroup(CrfRuleGroup):

    preg_prior = CrfRule(
        predicate=pc.func_preg_no_prior_participation,
        consequence=REQUIRED,
        alternative=NOT_REQUIRED,
        target_models=[f'{app_label}.foodsecurityquestionnaire',
                       f'{app_label}.ultrasound',
                       f'{app_label}.caregiveredinburghdeprscreening',
                       f'{app_label}.tbhistorypreg',
                       f'{app_label}.tbscreenpreg',
                       f'{app_label}.tbpresencehouseholdmembers'])

    biological_with_hiv = CrfRule(
        predicate=pc.func_bio_mothers_hiv,
        consequence=REQUIRED,
        alternative=NOT_REQUIRED,
        target_models=[f'{app_label}.hivviralloadandcd4', ])

    biological_mother = CrfRule(
        predicate=pc.func_bio_mother,
        consequence=REQUIRED,
        alternative=NOT_REQUIRED,
        target_models=[f'{app_label}.obstericalhistory',
                       f'{app_label}.caregiverclinicalmeasurements',
                       f'{app_label}.medicalhistory', ])

    # specimen_storage = CrfRule(
        # predicate=pc.func_specimen_storage_consent,
        # consequence=REQUIRED,
        # alternative=NOT_REQUIRED,
        # target_models=[f'{app_label}.bloodspecimenstorage', ])

    hiv_no_prior = CrfRule(
        predicate=pc.func_pregnant_hiv,
        consequence=REQUIRED,
        alternative=NOT_REQUIRED,
        target_models=[f'{app_label}.arvsprepregnancy',
                       f'{app_label}.maternalarvduringpreg',
                       f'{app_label}.maternalhivinterimhx', ])

    non_preg = CrfRule(
        predicate=pc.func_non_pregnant_caregivers,
        consequence=REQUIRED,
        alternative=NOT_REQUIRED,
        target_models=[f'{app_label}.caregiverphqdeprscreening'])

    LWHIV_10_15 = CrfRule(
        predicate=pc.func_LWHIV_aged_10_15,
        consequence=REQUIRED,
        alternative=NOT_REQUIRED,
        target_models=[f'{app_label}.hivdisclosurestatusa'])

    class Meta:
        app_label = app_label
        source_model = f'{app_label}.maternalvisit'
