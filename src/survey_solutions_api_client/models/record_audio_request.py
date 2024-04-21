from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RecordAudioRequest")


@_attrs_define
class RecordAudioRequest:
    """
    Attributes:
        enabled (Union[Unset, bool]): Enable or disable recording
    """

    enabled: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        enabled = self.enabled

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if enabled is not UNSET:
            field_dict["Enabled"] = enabled

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        enabled = d.pop("Enabled", UNSET)

        record_audio_request = cls(
            enabled=enabled,
        )

        return record_audio_request
