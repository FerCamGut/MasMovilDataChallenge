from airflow.models.baseoperator import BaseOperator
from datetime import datetime

class TimeDiffOperator(BaseOperator):

    def __init__(
            self,
            input_date: datetime,
            **kwargs) -> None:
        super().__init__(**kwargs)
        self.input_date = input_date
		
    def execute(self,context):
        diff_date = datetime.now() - self.input_date
