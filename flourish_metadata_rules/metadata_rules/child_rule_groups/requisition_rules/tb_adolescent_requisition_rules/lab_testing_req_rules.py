from edc_metadata import NOT_REQUIRED, REQUIRED
from edc_metadata_rules import RequisitionRule, RequisitionRuleGroup, register, P
from edc_constants.constants import NO
from flourish_labs import dna_pcr_panel, stool_sample_panel, infant_pl_cytokines_panel
from flourish_labs import rectal_swab_panel
from .....predicates import ChildPredicates


app_label = 'flourish_child'
pc = ChildPredicates()



@register()
class LabReqRuleGroup(RequisitionRuleGroup):

    # for dna_pcr and stool sample if the mother is positive
    dna_pcr_panel_rule = RequisitionRule(
        predicate=pc.func_diagnosied_with_hiv,
        consequence=REQUIRED,
        alternative=NOT_REQUIRED,
        target_panels=[dna_pcr_panel,])

    class Meta:
        app_label = app_label
        source_model = f'{app_label}.hivtestingadol'
        requisition_model = f'{app_label}.childrequisition'
