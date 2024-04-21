from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.assignment_details import AssignmentDetails
    from ..models.import_data_verification_state import ImportDataVerificationState


T = TypeVar("T", bound="CreateAssignmentResult")


@_attrs_define
class CreateAssignmentResult:
    """
    Attributes:
        assignment (Union[Unset, AssignmentDetails]):
        verification_status (Union[Unset, ImportDataVerificationState]):
        web_interview_link (Union[None, Unset, str]):
    """

    assignment: Union[Unset, "AssignmentDetails"] = UNSET
    verification_status: Union[Unset, "ImportDataVerificationState"] = UNSET
    web_interview_link: Union[None, Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        assignment: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.assignment, Unset):
            assignment = self.assignment.to_dict()

        verification_status: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.verification_status, Unset):
            verification_status = self.verification_status.to_dict()

        web_interview_link: Union[None, Unset, str]
        if isinstance(self.web_interview_link, Unset):
            web_interview_link = UNSET
        else:
            web_interview_link = self.web_interview_link

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if assignment is not UNSET:
            field_dict["Assignment"] = assignment
        if verification_status is not UNSET:
            field_dict["VerificationStatus"] = verification_status
        if web_interview_link is not UNSET:
            field_dict["WebInterviewLink"] = web_interview_link

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.assignment_details import AssignmentDetails
        from ..models.import_data_verification_state import ImportDataVerificationState

        d = src_dict.copy()
        _assignment = d.pop("Assignment", UNSET)
        assignment: Union[Unset, AssignmentDetails]
        if isinstance(_assignment, Unset):
            assignment = UNSET
        else:
            assignment = AssignmentDetails.from_dict(_assignment)

        _verification_status = d.pop("VerificationStatus", UNSET)
        verification_status: Union[Unset, ImportDataVerificationState]
        if isinstance(_verification_status, Unset):
            verification_status = UNSET
        else:
            verification_status = ImportDataVerificationState.from_dict(_verification_status)

        def _parse_web_interview_link(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        web_interview_link = _parse_web_interview_link(d.pop("WebInterviewLink", UNSET))

        create_assignment_result = cls(
            assignment=assignment,
            verification_status=verification_status,
            web_interview_link=web_interview_link,
        )

        return create_assignment_result
