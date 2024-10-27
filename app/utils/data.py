from datetime import date

statuses = [
    {
        "code": "New",
        "name": "NEW",
        "processes": "WORK_PERMIT_REPLACEMENT,WORK_PERMIT,WORK_RESIDENT_PERMIT,SPECIAL_PERMIT,CITIZENSHIP_RENUNCIATION,CITIZENSHIP_INTENTION_FOREIGN_SPOUSE",
        "valid_from": date(2023, 1, 1),
        "valid_to": None,
    },
    {
        "code": "draft",
        "name": "Draft",
        "processes": "WORK_PERMIT_REPLACEMENT,WORK_PERMIT,WORK_RESIDENT_PERMIT,SPECIAL_PERMIT,CITIZENSHIP_RENUNCIATION,CITIZENSHIP_INTENTION_FOREIGN_SPOUSE",
        "valid_from": date(2023, 1, 1),
        "valid_to": None,
    },
    {
        "code": "VERIFICATION",
        "name": "Verification",
        "processes": "WORK_PERMIT_REPLACEMENT,WORK_PERMIT,WORK_RESIDENT_PERMIT,SPECIAL_PERMIT,CITIZENSHIP_RENUNCIATION,CITIZENSHIP_INTENTION_FOREIGN_SPOUSE,NATURALIZATION_INTENTION_FOREIGN_SPOUSE,MATURITY_PERIOD_WAIVER,PRESIDENT_POWER_REGISTER_CITIZENS_10A,REGISTRATION_OF_ADOPTED_CHILD_OVER_3YEARS,PRESIDENT_POWER_REGISTER_CITIZENS_10B, CITIZENSHIP_FOR_UNDER_20,CERTIFICATE_OF_CITIZENSHIP_INCASE_DOUBT,RESUMPTION_OF_CITIZENSHIP,SETTLEMENT,NATURALIZATION,NATURALIZATION_BY_FOREIGN_SPOUSE,DUAL_CITIZENSHIP_RENUNCIATION",
        "valid_from": date(2023, 1, 1),
        "valid_to": None,
    },
    {
        "code": "GAZETTE",
        "name": "gazette",
        "processes": "NATURALIZATION,NATURALIZATION_BY_FOREIGN_SPOUSE",
        "valid_from": date(2023, 1, 1),
        "valid_to": None,
    },
    {
        "code": "vetting",
        "name": "Vetting",
        "processes": "WORK_PERMIT_REPLACEMENT,WORK_PERMIT,WORK_RESIDENT_PERMIT,SPECIAL_PERMIT,CITIZENSHIP_RENUNCIATION,CITIZENSHIP_INTENTION_FOREIGN_SPOUSE, NATURALIZATION_INTENTION_FOREIGN_SPOUSE,MATURITY_PERIOD_WAIVER,PRESIDENT_POWER_REGISTER_CITIZENS_10A,REGISTRATION_OF_ADOPTED_CHILD_OVER_3YEARS,PRESIDENT_POWER_REGISTER_CITIZENS_10B,CITIZENSHIP_FOR_UNDER_20,CERTIFICATE_OF_CITIZENSHIP_INCASE_DOUBT,RESUMPTION_OF_CITIZENSHIP,SETTLEMENT,NATURALIZATION,NATURALIZATION_BY_FOREIGN_SPOUSE,DUAL_CITIZENSHIP_RENUNCIATION",
        "valid_from": date(2023, 1, 1),
        "valid_to": None,
    },
    {
        "code": "committee_evaluation",
        "name": "COMMITTEE EVALUATION",
        "processes": "WORK_RESIDENT_PERMIT,SPECIAL_PERMIT,CITIZENSHIP_RENUNCIATION,CITIZENSHIP_INTENTION_FOREIGN_SPOUSE, NATURALIZATION_INTENTION_FOREIGN_SPOUSE,MATURITY_PERIOD_WAIVER,PRESIDENT_POWER_REGISTER_CITIZENS_10A,REGISTRATION_OF_ADOPTED_CHILD_OVER_3YEARS,PRESIDENT_POWER_REGISTER_CITIZENS_10B,CITIZENSHIP_FOR_UNDER_20,CERTIFICATE_OF_CITIZENSHIP_INCASE_DOUBT,RESUMPTION_OF_CITIZENSHIP,SETTLEMENT,NATURALIZATION,NATURALIZATION_BY_FOREIGN_SPOUSE,DUAL_CITIZENSHIP_RENUNCIATION",
        "valid_from": date(2023, 1, 1),
        "valid_to": None,
    },
    {
        "code": "rejected",
        "name": "REJECTED",
        "processes": "WORK_PERMIT_REPLACEMENT,WORK_PERMIT,WORK_RESIDENT_PERMIT,SPECIAL_PERMIT,CITIZENSHIP_RENUNCIATION,CITIZENSHIP_INTENTION_FOREIGN_SPOUSE,MATURITY_PERIOD_WAIVER,PRESIDENT_POWER_10A,REGISTRATION_OF_ADOPTED_CHILD_OVER_3YEARS,PRESIDENT_POWER_REGISTER_CITIZENS_10B,CITIZENSHIP_FOR_UNDER_20,CERTIFICATE_OF_CITIZENSHIP_INCASE_DOUBT,RESUMPTION_OF_CITIZENSHIP,SETTLEMENT,NATURALIZATION,NATURALIZATION_BY_FOREIGN_SPOUSE,DUAL_CITIZENSHIP_RENUNCIATION",
        "valid_from": date(2023, 1, 1),
        "valid_to": None,
    },
    {
        "code": "accepted",
        "name": "ACCEPTED",
        "processes": "WORK_PERMIT_REPLACEMENT,WORK_PERMIT,WORK_RESIDENT_PERMIT,SPECIAL_PERMIT,CITIZENSHIP_RENUNCIATION,CITIZENSHIP_INTENTION_FOREIGN_SPOUSE,MATURITY_PERIOD_WAIVER,PRESIDENT_POWER_REGISTER_CITIZENS_10A,REGISTRATION_OF_ADOPTED_CHILD_OVER_3YEARS,PRESIDENT_POWER_REGISTER_CITIZENS_10B,CITIZENSHIP_FOR_UNDER_20,CERTIFICATE_OF_CITIZENSHIP_INCASE_DOUBT,RESUMPTION_OF_CITIZENSHIP,SETTLEMENT,NATURALIZATION,NATURALIZATION_BY_FOREIGN_SPOUSE,DUAL_CITIZENSHIP_RENUNCIATION",
        "valid_from": date(2023, 1, 1),
        "valid_to": None,
    },
    {
        "code": "final_decision",
        "name": "FINAL_DECISION",
        "processes": "WORK_PERMIT_REPLACEMENT,WORK_RESIDENT_PERMIT,SPECIAL_PERMIT,CITIZENSHIP_RENUNCIATION,CITIZENSHIP_INTENTION_FOREIGN_SPOUSE,NATURALIZATION_INTENTION_FOREIGN_SPOUSE,MATURITY_PERIOD_WAIVER,PRESIDENT_POWER_REGISTER_CITIZENS_10A,REGISTRATION_OF_ADOPTED_CHILD_OVER_3YEARS,PRESIDENT_POWER_REGISTER_CITIZENS_10B,CITIZENSHIP_FOR_UNDER_20,CERTIFICATE_OF_CITIZENSHIP_INCASE_DOUBT,RESUMPTION_OF_CITIZENSHIP,SETTLEMENT,NATURALIZATION,NATURALIZATION_BY_FOREIGN_SPOUSE,DUAL_CITIZENSHIP_RENUNCIATION",
        "valid_from": date(2023, 1, 1),
        "valid_to": None,
    },
    {
        "code": "recommendation",
        "name": "RECOMMENDATION",
        "processes": "WORK_RESIDENT_PERMIT,SPECIAL_PERMIT,CITIZENSHIP_RENUNCIATION,CITIZENSHIP_INTENTION_FOREIGN_SPOUSE,MATURITY_PERIOD_WAIVER,REGISTRATION_OF_ADOPTED_CHILD_OVER_3YEARS,PRESIDENT_POWER_REGISTER_CITIZENS_10B,CITIZENSHIP_FOR_UNDER_20,CERTIFICATE_OF_CITIZENSHIP_INCASE_DOUBT,RESUMPTION_OF_CITIZENSHIP,SETTLEMENT,NATURALIZATION,NATURALIZATION_BY_FOREIGN_SPOUSE,DUAL_CITIZENSHIP_RENUNCIATION,PRESIDENT_POWER_REGISTER_CITIZENS_10B",
        "valid_from": date(2023, 1, 1),
        "valid_to": None,
    },
    {
        "code": "minister_decision",
        "name": "MINISTER_DECISION",
        "processes": "WORK_RESIDENT_PERMIT,SPECIAL_PERMIT,CITIZENSHIP_RENUNCIATION,CITIZENSHIP_INTENTION_FOREIGN_SPOUSE,MATURITY_PERIOD_WAIVER,REGISTRATION_OF_ADOPTED_CHILD_OVER_3YEARS,PRESIDENT_POWER_REGISTER_CITIZENS_10B,CITIZENSHIP_FOR_UNDER_20,CERTIFICATE_OF_CITIZENSHIP_INCASE_DOUBT,RESUMPTION_OF_CITIZENSHIP,SETTLEMENT,NATURALIZATION,NATURALIZATION_BY_FOREIGN_SPOUSE,DUAL_CITIZENSHIP_RENUNCIATION,PRESIDENT_POWER_REGISTER_CITIZENS_10B",
        "valid_from": date(2023, 1, 1),
        "valid_to": None,
    },
    {
        "code": "deferred",
        "name": "DEFERRED",
        "processes": "WORK_PERMIT_REPLACEMENT,WORK_RESIDENT_PERMIT,SPECIAL_PERMIT,CITIZENSHIP_RENUNCIATION,CITIZENSHIP_INTENTION_FOREIGN_SPOUSE,MATURITY_PERIOD_WAIVER,PRESIDENT_POWER_REGISTER_CITIZENS_10A,REGISTRATION_OF_ADOPTED_CHILD_OVER_3YEARS,PRESIDENT_POWER_REGISTER_CITIZENS_10B,CITIZENSHIP_FOR_UNDER_20,CERTIFICATE_OF_CITIZENSHIP_INCASE_DOUBT,RESUMPTION_OF_CITIZENSHIP,SETTLEMENT,NATURALIZATION,NATURALIZATION_BY_FOREIGN_SPOUSE,DUAL_CITIZENSHIP_RENUNCIATION,PRESIDENT_POWER_REGISTER_CITIZENS_10B",
        "valid_from": date(2023, 1, 1),
        "valid_to": None,
    },
    {
        "code": "pending",
        "name": "Pending",
        "processes": "WORK_PERMIT_REPLACEMENT,WORK_RESIDENT_PERMIT,SPECIAL_PERMIT,CITIZENSHIP_RENUNCIATION,CITIZENSHIP_INTENTION_FOREIGN_SPOUSE,MATURITY_PERIOD_WAIVER,PRESIDENT_POWER_REGISTER_CITIZENS_10A,REGISTRATION_OF_ADOPTED_CHILD_OVER_3YEARS,PRESIDENT_POWER_REGISTER_CITIZENS_10B,CITIZENSHIP_FOR_UNDER_20,CERTIFICATE_OF_CITIZENSHIP_INCASE_DOUBT,RESUMPTION_OF_CITIZENSHIP,SETTLEMENT,NATURALIZATION,NATURALIZATION_BY_FOREIGN_SPOUSE,DUAL_CITIZENSHIP_RENUNCIATION",
        "valid_from": date(2023, 1, 1),
        "valid_to": None,
    },
    {
        "code": "assessment",
        "name": "ASSESSMENT",
        "processes": "WORK_RESIDENT_PERMIT,SPECIAL_PERMIT,CITIZENSHIP_RENUNCIATION,CITIZENSHIP_INTENTION_FOREIGN_SPOUSE,MATURITY_PERIOD_WAIVER,REGISTRATION_OF_ADOPTED_CHILD_OVER_3YEARS,PRESIDENT_POWER_REGISTER_CITIZENS_10B,CITIZENSHIP_FOR_UNDER_20,CERTIFICATE_OF_CITIZENSHIP_INCASE_DOUBT,RESUMPTION_OF_CITIZENSHIP,SETTLEMENT,NATURALIZATION,NATURALIZATION_BY_FOREIGN_SPOUSE,DUAL_CITIZENSHIP_RENUNCIATION,PRESIDENT_POWER_REGISTER_CITIZENS_10B",
        "valid_from": date(2023, 1, 1),
        "valid_to": None,
    },
    {
        "code": "review",
        "name": "REVIEW",
        "processes": "WORK_RESIDENT_PERMIT,SPECIAL_PERMIT,CITIZENSHIP_RENUNCIATION,CITIZENSHIP_INTENTION_FOREIGN_SPOUSE,MATURITY_PERIOD_WAIVER,REGISTRATION_OF_ADOPTED_CHILD_OVER_3YEARS,PRESIDENT_POWER_REGISTER_CITIZENS_10B,CITIZENSHIP_FOR_UNDER_20,CERTIFICATE_OF_CITIZENSHIP_INCASE_DOUBT,RESUMPTION_OF_CITIZENSHIP,SETTLEMENT,NATURALIZATION,NATURALIZATION_BY_FOREIGN_SPOUSE,DUAL_CITIZENSHIP_RENUNCIATION,PRESIDENT_POWER_REGISTER_CITIZENS_10B",
        "valid_from": date(2023, 1, 1),
        "valid_to": None,
    },
    {
        "code": "ps_recommendation",
        "name": "PS_RECOMMENDATION",
        "processes": "WORK_RESIDENT_PERMIT,SPECIAL_PERMIT,CITIZENSHIP_RENUNCIATION,CITIZENSHIP_INTENTION_FOREIGN_SPOUSE,MATURITY_PERIOD_WAIVER,REGISTRATION_OF_ADOPTED_CHILD_OVER_3YEARS,PRESIDENT_POWER_REGISTER_CITIZENS_10B,CITIZENSHIP_FOR_UNDER_20,CERTIFICATE_OF_CITIZENSHIP_INCASE_DOUBT,RESUMPTION_OF_CITIZENSHIP,SETTLEMENT,NATURALIZATION,NATURALIZATION_BY_FOREIGN_SPOUSE,DUAL_CITIZENSHIP_RENUNCIATION,PRESIDENT_POWER_REGISTER_CITIZENS_10B",
        "valid_from": date(2023, 1, 1),
        "valid_to": None,
    },
    {
        "code": "pres_ps_recommendation",
        "name": "PRES_PS_RECOMMENDATION",
        "processes": "WORK_RESIDENT_PERMIT,SPECIAL_PERMIT,CITIZENSHIP_RENUNCIATION,CITIZENSHIP_INTENTION_FOREIGN_SPOUSE,MATURITY_PERIOD_WAIVER,REGISTRATION_OF_ADOPTED_CHILD_OVER_3YEARS,PRESIDENT_POWER_REGISTER_CITIZENS_10B,CITIZENSHIP_FOR_UNDER_20,CERTIFICATE_OF_CITIZENSHIP_INCASE_DOUBT,RESUMPTION_OF_CITIZENSHIP,SETTLEMENT,NATURALIZATION,NATURALIZATION_BY_FOREIGN_SPOUSE,DUAL_CITIZENSHIP_RENUNCIATION,PRESIDENT_POWER_REGISTER_CITIZENS_10B",
        "valid_from": date(2023, 1, 1),
        "valid_to": None,
    },
    {
        "code": "president_decision",
        "name": "PRESIDENT_DECISION",
        "processes": "WORK_RESIDENT_PERMIT,SPECIAL_PERMIT,CITIZENSHIP_RENUNCIATION,CITIZENSHIP_INTENTION_FOREIGN_SPOUSE,MATURITY_PERIOD_WAIVER,REGISTRATION_OF_ADOPTED_CHILD_OVER_3YEARS,PRESIDENT_POWER_REGISTER_CITIZENS_10B,CITIZENSHIP_FOR_UNDER_20,CERTIFICATE_OF_CITIZENSHIP_INCASE_DOUBT,RESUMPTION_OF_CITIZENSHIP,SETTLEMENT,NATURALIZATION,NATURALIZATION_BY_FOREIGN_SPOUSE,DUAL_CITIZENSHIP_RENUNCIATION,PRESIDENT_POWER_REGISTER_CITIZENS_10B",
        "valid_from": date(2023, 1, 1),
        "valid_to": None,
    },
    {
        "code": "foreign_renunciation",
        "name": "FOREIGN_RENUNCIATION",
        "processes": "WORK_RESIDENT_PERMIT,SPECIAL_PERMIT,CITIZENSHIP_RENUNCIATION,CITIZENSHIP_INTENTION_FOREIGN_SPOUSE,MATURITY_PERIOD_WAIVER,REGISTRATION_OF_ADOPTED_CHILD_OVER_3YEARS,PRESIDENT_POWER_REGISTER_CITIZENS_10B,CITIZENSHIP_FOR_UNDER_20,CERTIFICATE_OF_CITIZENSHIP_INCASE_DOUBT,RESUMPTION_OF_CITIZENSHIP,SETTLEMENT,NATURALIZATION,NATURALIZATION_BY_FOREIGN_SPOUSE,DUAL_CITIZENSHIP_RENUNCIATION,PRESIDENT_POWER_REGISTER_CITIZENS_10B",
        "valid_from": date(2023, 1, 1),
        "valid_to": None,
    }
]

offices = [{"name": "Gaborone", "code": "01"}]


data = [
    {
        "code": "ACCEPTED",
        "name": "Accepted",
        "valid_from": date(2023, 1, 1),
        "process_types": "visa,workresidentandpermit",
        "valid_to": date(2035, 1, 1),
    },
    {
        "code": "REJECTED",
        "name": "Rejected",
        "valid_from": date(2023, 1, 1),
        "process_types": "visa,workresidentandpermit",
        "valid_to": date(2035, 1, 1),
    },
    {
        "code": "PENDING",
        "name": "Pending",
        "valid_from": date(2023, 1, 1),
        "process_types": "visa,workresidentandpermit",
        "valid_to": date(2035, 1, 1),
    },
]
