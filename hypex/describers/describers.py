import numpy as np
from typing import Iterable

from hypex.experiment.experiment import Executor
from hypex.dataset.dataset import Dataset, ExperimentData


class Describer(Executor):
    def __init__(self, target_field: FieldKey, full_name: str = None, key: Any = 0):
        self.target_field = target_field
        super().__init__(full_name, key)

    def _set_value(self, data: ExperimentData, value: Dataset) -> ExperimentData:
        return data.set_value("analysis_tables", self._id, self.full_name, value)


class Unique(Describer):
    def _convert_to_dataset(self, data: Iterable) -> Dataset:
        return Dataset().from_dict(data)

    def execute(self, data: ExperimentData) -> ExperimentData:
        result_dataset = self._convert_to_dataset(
            [{self.full_name: np.unique(data.data[self.target_field])}]
        )
        return self._set_value(data, result_dataset)
