

class NewApplication(object):

    """Represent NewApplication model submitted by the front-end.

        Attributes:
            process_name (str): The name of the process e.g resident_permit, visa.
            applicant (ApplicationUser): The customer who applying for the given process.
    """
    def __init__(self, process_name, applicant_identifier, status, dob=None, work_place=None):
        self.proces_name = process_name
        self.applicant_identifier = applicant_identifier
        self.status = status
        self.dob = dob
        self.work_place = work_place
