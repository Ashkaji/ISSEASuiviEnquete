from enum import Enum


class InterviewStatus(str, Enum):
    APPROVEDBYHEADQUARTERS = "ApprovedByHeadquarters"
    APPROVEDBYSUPERVISOR = "ApprovedBySupervisor"
    COMPLETED = "Completed"
    CREATED = "Created"
    DELETED = "Deleted"
    INTERVIEWERASSIGNED = "InterviewerAssigned"
    READYFORINTERVIEW = "ReadyForInterview"
    REJECTEDBYHEADQUARTERS = "RejectedByHeadquarters"
    REJECTEDBYSUPERVISOR = "RejectedBySupervisor"
    RESTARTED = "Restarted"
    RESTORED = "Restored"
    SENTTOCAPI = "SentToCapi"
    SUPERVISORASSIGNED = "SupervisorAssigned"

    def __str__(self) -> str:
        return str(self.value)
