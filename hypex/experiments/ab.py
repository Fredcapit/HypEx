from hypex.analyzers.ab import ABAnalyzer
from hypex.comparators import GroupDifference, GroupSizes, TTest, UTest, Chi2Test
from hypex.dataset import TargetRole, TreatmentRole
from hypex.experiments import Experiment, OnRoleExperiment
from hypex.utils import ABNTestMethodsEnum

AB_TEST = Experiment(
    executors=[
        GroupSizes(grouping_role=TreatmentRole()),
        OnRoleExperiment(
            executors=[
                GroupDifference(grouping_role=TreatmentRole()),
                TTest(grouping_role=TreatmentRole()),
                UTest(grouping_role=TreatmentRole()),
                Chi2Test(grouping_role=TreatmentRole()),
            ],
            role=TargetRole(),
        ),
        ABAnalyzer(multitest_method=ABNTestMethodsEnum.quantile),
    ]
)
