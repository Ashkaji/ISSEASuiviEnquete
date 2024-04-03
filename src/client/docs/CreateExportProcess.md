# CreateExportProcess

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**export_type** | [**ExportType**](ExportType.md) |  | 
**questionnaire_id** | **str** | Questionnaire id in format [QuestionnaireGuid$Version] | 
**interview_status** | [**ExportInterviewType**](ExportInterviewType.md) |  | 
**_from** | **datetime** | Started date for timeframe of exported interviews (when change was done to an interview). Should be in UTC date | [optional] 
**to** | **datetime** | Finished date for timeframe of exported interviews (when change was done to an interview). Should be in UTC date | [optional] 
**access_token** | **str** | Access token to external storage | [optional] 
**refresh_token** | **str** | Refresh token to external storage | [optional] 
**storage_type** | [**ExternalStorageType**](ExternalStorageType.md) |  | [optional] 
**translation_id** | **str** | Translation Id of the questionnaire | [optional] 
**include_meta** | **bool** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

