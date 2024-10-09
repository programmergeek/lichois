from enum import Enum


class CitizenshipStagesEnum(Enum):

    VERIFICATION = "VERIFICATION"
    ASSESSMENT = "ASSESSMENT"
    REVIEW = "REVIEW"
    VETTING = "VETTING"
    RECOMMENDATION = "RECOMMENDATION"
    MINISTER_DECISION = "MINISTER_DECISION"
    MINISTER_ACCEPTANCE = "MINISTER_ACCEPTANCE"
    FOREIGN_RENUNCIATION = "FOREIGN_RENUNCIATION"
    PS_RECOMMENDATION = "PS_RECOMMENDATION"
    PRES_PS_RECOMMENDATION = "PRES_PS_RECOMMENDATION"
    PRESIDENT_DECISION = "PRESIDENT_DECISION"
