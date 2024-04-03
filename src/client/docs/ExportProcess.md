# ExportProcess

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **int** | Export process id | [optional] 
**export_status** | [**ExportStatus**](ExportStatus.md) |  | [optional] 
**start_date** | **datetime** | Export process stated date | [optional] 
**complete_date** | **datetime** | Export process completed date | [optional] 
**create_date** | **datetime** | Export process stated date | [optional] 
**progress** | **int** | Progress of export in percents | [optional] 
**eta** | **str** | Estimated time to finish of export | [optional] 
**error** | **str** |  | [optional] 
**links** | [**ExportJobLinks**](ExportJobLinks.md) |  | [optional] 
**has_export_file** | **bool** | True, if export process is finished and exported file ready for download, otherwise false | [optional] 
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

