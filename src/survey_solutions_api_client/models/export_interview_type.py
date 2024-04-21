from enum import Enum


class ExportInterviewType(str, Enum):
    ALL = "All"
    APPROVEDBYHEADQUARTERS = "ApprovedByHeadquarters"
    APPROVEDBYSUPERVISOR = "ApprovedBySupervisor"
    COMPLETED = "Completed"
    INTERVIEWERASSIGNED = "InterviewerAssigned"
    REJECTEDBYHEADQUARTERS = "RejectedByHeadquarters"
    REJECTEDBYSUPERVISOR = "RejectedBySupervisor"
    SUPERVISORASSIGNED = "SupervisorAssigned"

    def __str__(self) -> str:
        return str(self.value)
