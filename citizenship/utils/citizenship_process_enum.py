from enum import Enum


class CitizenshipProcessEnum(Enum):

    RENUNCIATION = "CITIZENSHIP_RENUNCIATION"
    DUAL_RENUNCIATION = "DUAL_CITIZENSHIP_RENUNCIATION"
    INTENTION_FOREIGN_SPOUSE = "NATURALIZATION_INTENTION_FOREIGN_SPOUSE"
    MATURITY_PERIOD_WAIVER = "MATURITY_PERIOD_WAIVER"
    PRESIDENT_POWER_10A = "PRESIDENT_POWER_REGISTER_CITIZENS_10A"
    PRESIDENT_POWER_10B = "PRESIDENT_POWER_REGISTER_CITIZENS_10B"
    ADOPTED_CHILD_REGISTRATION = "REGISTRATION_OF_ADOPTED_CHILD_OVER_3YEARS"
    UNDER_20_CITIZENSHIP = "CITIZENSHIP_FOR_UNDER_20"
    FOREIGN_SPOUSE_NATURALIZATION = "NATURALIZATION_BY_FOREIGN_SPOUSE"
    NATURALIZATION = "NATURALIZATION"
    CITIZENSHIP_RESUMPTION = "RESUMPTION_OF_CITIZENSHIP"
    DOUBT_CITIZENSHIP_CERTIFICATE = "CERTIFICATE_OF_CITIZENSHIP_INCASE_DOUBT"
    CITIZENSHIP_DEPRIVATION = "DEPRIVATION_OF_CITIZENSHIP"
    SETTLEMENT = "SETTLEMENT"
