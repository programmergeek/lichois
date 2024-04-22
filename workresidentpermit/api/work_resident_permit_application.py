

class WorkResidentPermitApplication:
    """A wrapper class for work resident permit application details API model.
    """
    def __init__(self):
        self._personal_details = None
        self._address = None
        self._passport = None
        self._permit = None
        self._child = None
        self._spouse = None
        self._form_details = None
        self._application = None
        self._attachments = None

    @property
    def personal_details(self):
        return self._personal_details

    @personal_details.setter
    def personal_details(self, value):
        self._personal_details = value

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value

    @property
    def passport(self):
        return self._passport

    @passport.setter
    def passport(self, value):
        self._passport = value

    @property
    def permit(self):
        return self._permit

    @permit.setter
    def permit(self, value):
        self._permit = value

    @property
    def child(self):
        return self._child

    @child.setter
    def child(self, value):
        self._child = value

    @property
    def spouse(self):
        return self._spouse

    @spouse.setter
    def spouse(self, value):
        self._spouse = value

    @property
    def form_details(self):
        return self._form_details

    @form_details.setter
    def form_details(self, value):
        self._form_details = value

    @property
    def application(self):
        return self._application

    @application.setter
    def application(self, value):
        self._application = value

    @property
    def attachments(self):
        return self._attachments

    @attachments.setter
    def attachments(self, value):
        self._attachments = value
