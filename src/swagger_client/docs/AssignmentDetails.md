# AssignmentDetails

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifying_data** | [**list[AssignmentIdentifyingDataItem]**](AssignmentIdentifyingDataItem.md) |  | [optional] 
**id** | **int** |  | [optional] 
**responsible_id** | **str** |  | [optional] 
**responsible_name** | **str** | Name of the responsible person  Can be used for ordering | [optional] 
**questionnaire_id** | **str** | Questionnaire Id | [optional] 
**interviews_count** | **int** | Quantity of submitted interviews for this assignment  Can be used for ordering | [optional] 
**quantity** | **int** | Maximum allowed quantity of interviews that can be created from this assignment  Can be used for ordering | [optional] 
**archived** | **bool** | Archived status to filter by. True or False | [optional] 
**created_at_utc** | **datetime** | Date (UTC) when assignment were created  Can be used for ordering | [optional] 
**updated_at_utc** | **datetime** | Last Update Date (UTC) of assignment  Can be used for ordering | [optional] 
**email** | **str** |  | [optional] 
**password** | **str** |  | [optional] 
**web_mode** | **bool** |  | [optional] 
**received_by_tablet_at_utc** | **datetime** | Represents date (UTC) when assignment was received by tablet | [optional] 
**is_audio_recording_enabled** | **bool** | Determines if interview from this assignment must record voice during interview (only on tablet) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

