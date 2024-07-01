from enum import Enum


class ApplicationProcesses(Enum):
    VISA = "VISA"
    WORK_RESIDENT_PERMIT = "WORK_RESIDENT_PERMIT"
    WORK_PERMIT = "WORK_PERMIT"
    RESIDENT_PERMIT = "RESIDENT_PERMIT"
    SPECIAL_PERMIT = "SPECIAL_PERMIT"
    EXEMPTION_CERTIFICATE = "EXEMPTION_CERTIFICATE"


class ApplicationStatusEnum(Enum):
    NEW = "NEW"
    DRAFT = "DRAFT"
    VERIFICATION = "VERIFICATION"
    VETTING = "VETTING"
    COMMITEE_EVALUATION = "COMMITEE_EVALUATION"
    REJECTED = "REJECTED"
    ACCEPTED = "ACCEPTED"
    CANCELLED = "CANCELLED"
    RECOMMENDATION = "RECOMMENDATION"
    DEFERRED = "DEFERRED"
    PENDING = "PENDING"
    COMPLETED = "COMPLETED"


class WorkflowEnum(Enum):
    RECOMMENDATION = "RECOMMENDATION"
    VERIFICATION = "VERIFICATION"
    VETTING = "VETTING"
    FINAL_DECISION = "FINAL_DECISION"
    PERMIT_CANCELLATION = "PERMIT_CANCELLATION"
    END = "END"


class ApplicationDecisionEnum(Enum):
    PENDING = "Pending"
    ACCEPTED = "Accepted"
    REJECTED = "Rejected"
    APPROVED = "approved"
    DEFERRED = "deferred"

    
