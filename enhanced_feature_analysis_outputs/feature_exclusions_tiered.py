"""
Tiered Feature Exclusion Lists for MVA Qualification Model
Generated on: 2025-10-18 05:05:51
Enhanced version with aggressive risk detection
Target: MVA_Qualified = (Qualified="Yes" AND Law_Type="MVA")
"""

# TIER 1: Auto-exclude (Risk Score >= 8)
# These features have very high risk of data leakage or are inappropriate
TIER1_AUTO_EXCLUDE = [
    "CaseComplexityScore",
    "CaseUrgencyScore",
    "ChannelCountLast30d",
    "ChannelDiversityIndex",
    "ChannelIsPhone",
    "DuplicateInquiryFlag",
    "EngagementScore",
    "EngagementZScore",
    "HoursIncidentToCall",
    "IncidentRecencyDays",
    "Inquiry Call Type Qualified Flag",
    "LogDaysSinceIncident",
    "PriorContactCount",
    "ResponseTimeHours",
    "SourceReliabilityScore",
    "StatuteRiskScore",
    "TimeToFirstResponseMinutes",
    "TouchpointsLast7d",
    "UniqueInquiryFlag",
]

# TIER 2: Strong review needed (Risk Score 5-7)
# These features require careful domain expert review
TIER2_STRONG_REVIEW = [
    "CallTimeOfDay",
    "DaysIncidentToCall",
    "DaysIncidentToInquiry",
    "HoursIncidentToInquiry",
    "InOptimalWindowFlag",
    "IncidentMonth",
    "IncidentQuarter",
    "IncidentSeason",
    "IncidentWithin180d",
    "IncidentWithin30d",
    "IncidentWithin365d",
    "IncidentWithin90d",
    "InquiryTimeOfDay",
    "IsWeekendIncident",
    "QuickResponseFlag",
    "RetainedByAttorneyFlag",
    "SameDayIncidentToCall",
    "SameDayIncidentToInquiry",
]

# TIER 3: Consider carefully (Risk Score 3-4)
# These features may be useful but need validation
TIER3_CONSIDER_CAREFULLY = [
]

# TIER 4: Likely safe features (Risk Score < 3)
# These features appear safe for modeling
TIER4_LIKELY_SAFE = [
    "AbandonedCallFlag",
    "BrandGroup",
    "CallDayOfWeek",
    "CallSeason",
    "CampaignTier",
    "ChannelIsSMS",
    "ChannelIsWeb",
    "CompanyGroup",
    "ConsumerAge",
    "ConsumerGender",
    "DeviceType",
    "HasUninsuredMotoristCoverage",
    "HospitalizationFlag",
    "Inquiry Call Type Law Type (Broad)",
    "InquiryDayOfWeek",
    "LanguageGroup",
    "LawTypeShared",
    "MarketingSpendBucket",
    "OptInSMSFlag",
    "RecencyBucket",
    "RegionGroup",
    "SourceMedium",
    "WebLeadAttempts",
]

# Helper function to get safe features for modeling
def get_safe_features(include_tier3=False, include_tier2=False):
    """Get features safe for modeling based on tier preferences"""
    safe = TIER4_LIKELY_SAFE.copy()
    if include_tier3:
        safe.extend(TIER3_CONSIDER_CAREFULLY)
    if include_tier2:
        safe.extend(TIER2_STRONG_REVIEW)
    return safe
