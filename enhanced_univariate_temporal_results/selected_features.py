"""
Selected features for synthetic demo (no proprietary columns)
Generated on: 2025-10-18 00:00:00
Target variable: MVA_Qualified
"""

# Top 30 features by predictiveness score (synthetic)
TOP_30_FEATURES = ['IncidentRecencyDays', 'IncidentWithin365d', 'IncidentWithin180d', 'DaysIncidentToInquiry', 'DaysIncidentToCall', 'HoursIncidentToInquiry', 'HoursIncidentToCall', 'InquiryTimeOfDay', 'CallTimeOfDay', 'IncidentSeason', 'ResponseTimeHours', 'QuickResponseFlag', 'CaseUrgencyScore', 'EngagementScore', 'ChannelIsWeb', 'ChannelIsPhone', 'ChannelIsSMS', 'ChannelCountLast30d', 'TouchpointsLast7d', 'HasUninsuredMotoristCoverage', 'ConsumerAge', 'LanguageGroup', 'WebLeadAttempts', 'AbandonedCallFlag', 'StatuteRiskScore', 'InOptimalWindowFlag', 'LogDaysSinceIncident', 'RecencyBucket', 'IncidentMonth', 'IncidentQuarter']

# Top 50 features by predictiveness score (synthetic)
TOP_50_FEATURES = ['IncidentRecencyDays', 'IncidentWithin365d', 'IncidentWithin180d', 'IncidentWithin90d', 'IncidentWithin30d', 'DaysIncidentToInquiry', 'DaysIncidentToCall', 'HoursIncidentToInquiry', 'HoursIncidentToCall', 'SameDayIncidentToInquiry', 'SameDayIncidentToCall', 'InquiryTimeOfDay', 'CallTimeOfDay', 'IncidentSeason', 'CallSeason', 'IsWeekendIncident', 'ResponseTimeHours', 'QuickResponseFlag', 'CaseUrgencyScore', 'CaseComplexityScore', 'EngagementScore', 'ChannelIsWeb', 'ChannelIsPhone', 'ChannelIsSMS', 'ChannelCountLast30d', 'TouchpointsLast7d', 'RetainedByAttorneyFlag', 'HasUninsuredMotoristCoverage', 'ConsumerGender', 'ConsumerAge', 'LanguageGroup', 'RegionGroup', 'CampaignTier', 'SourceMedium', 'DeviceType', 'WebLeadAttempts', 'AbandonedCallFlag', 'OptInSMSFlag', 'HospitalizationFlag', 'StatuteRiskScore', 'PriorContactCount', 'DuplicateInquiryFlag', 'UniqueInquiryFlag', 'InOptimalWindowFlag', 'LogDaysSinceIncident', 'RecencyBucket', 'InquiryDayOfWeek', 'CallDayOfWeek', 'IncidentMonth', 'IncidentQuarter']

# ML target
TARGET_VARIABLE = "MVA_Qualified"

# Convenience: export all = TOP_50 for modeling
ALL_FEATURES = TOP_50_FEATURES
