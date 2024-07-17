from workresidentpermit.classes import DataHelper
from workresidentpermit.classes.production import FetchRequiredDataForProduction


class PrepareCaseSummaryHelper(DataHelper):

    def __init__(self, configuration_file_name: str, document_number: str):
        self.configuration_file_name = configuration_file_name
        self.document_number = document_number

    def transform_data(self):
        """Returns assessment case summary data.
        """
        fetch_data = FetchRequiredDataForProduction(configuration_file_name=self.configuration_file_name,
                                                    document_number=self.document_number)
        data = fetch_data.get_data()

        for data_set in data:
            model_object = data_set.get("model_obj")
            for field in data_set.get("fields"):
                self.add_field(field_name=field, field_value=self.set_field_value(model_object, field))
        return self.data