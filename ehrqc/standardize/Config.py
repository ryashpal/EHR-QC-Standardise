# database connection details
db_details = {
    "sql_host_name": 'superbugai.erc.monash.edu',
    "sql_port_number": 5434,
    "sql_user_name": 'postgres',
    "sql_password": 'mysecretpassword',
    "sql_db_name": 'mimic4',
}

source_schema_name = 'eicu_etl_20231106'

etl_schema_name = 'eicu_etl_20231106'

lookup_schema_name = 'eicu_etl_20231106'

vocabulary = {
    'concept': '/superbugai-data/vocabulary_download_v5/CONCEPT.csv',
    'vocabulary': '/superbugai-data/vocabulary_download_v5/VOCABULARY.csv',
    'domain': '/superbugai-data/vocabulary_download_v5/DOMAIN.csv',
    'concept_class': '/superbugai-data/vocabulary_download_v5/CONCEPT_CLASS.csv',
    'concept_relationship': '/superbugai-data/vocabulary_download_v5/CONCEPT_RELATIONSHIP.csv',
    'relationship': '/superbugai-data/vocabulary_download_v5/RELATIONSHIP.csv',
    'concept_synonym': '/superbugai-data/vocabulary_download_v5/CONCEPT_SYNONYM.csv',
    'concept_ancestor': '/superbugai-data/vocabulary_download_v5/CONCEPT_ANCESTOR.csv',
    'tmp_custom_mapping': '/superbugai-data/vocabulary_download_v5/tmp_custom_mapping.csv',
}

patients = {
    'file_name': '/home/ehrqcadmin/workspace/ehr_data/blood_pos_cohort_20231023/demo_static1.csv',
    'file_separator': ',',
    'column_mapping': {
        'patient_id': 'PATIENT_ID',
        'age': 'Age',
        'gender': 'SEX',
        'dob': 'DATE_OF_BIRTH_DATETIME',
        'dod': 'DATEOFDEATH_DATETIME',
    },
}

admissions = {
    'file_name': '/home/ehrqcadmin/workspace/ehr_data/blood_pos_cohort_20231023/2023-04-29-blood-episode-1prio-plus-30days.csv',
    'file_separator': ',',
    'column_mapping': {
        'patient_id': 'PATIENT_ID',
        'episode_id': 'EPISODE_ID',
        'admittime': 'start_date',
        'dischtime': 'end_date',
        'deathtime': 'DATEOFDEATH_DATETIME',
        'admission_type': 'TYPE',
        'admission_location': 'ADMITTING_WARD',
        'discharge_location': None,
        'insurance': None,
        'language': None,
        'marital_status': None,
        'ethnicity': None,
        'edregtime': None,
        'edouttime': None,
        'hospital_expire_flag': None,
    },
}

chartevents = {
    'file_name': '/home/ehrqcadmin/workspace/ehr_data/blood_pos_cohort_20231023/blood-pos-vitals-all-rows.csv',
    'file_separator': ',',
    'column_mapping': {
        'patient_id': 'PATIENT_ID',
        'episode_id': 'EPISODE_ID',
        'vital_id': 'VITAL_ID',
        'charttime': 'PERFORMED_DATETIME',
        'storetime': 'RESULT_UPDATE_DATETIME',
        'itemid': 'TYPE',
        'value': 'RESULT',
        'valuenum': 'RESULT',
        'valueuom': 'RESULT_UNITS',
        'warning': None,
    },
}

labevents = {
    'file_name': '/home/ehrqcadmin/workspace/ehr_data/blood_pos_cohort_20231023/2023-10-23-bacteraemia-path-all-raw.csv',
    'file_separator': ',',
    'column_mapping': {
        'labevent_id': 'PATH_RESULT_ID',
        'patient_id': 'PATIENT_ID',
        'episode_id': 'EPISODE_ID',
        'specimen_id': 'ORDER_ID',
        'itemid': 'TYPE',
        'charttime': 'PERFORMED_DATETIME',
        'storetime': 'RESULT_UPDT_DATETIME',
        'value': 'RESULT',
        'valuenum': 'RESULT',
        'valueuom': 'RESULT_UNITS',
        'ref_range_lower': 'NORMAL_LOW',
        'ref_range_upper': 'NORMAL_HIGH',
        'flag': None,
        'priority': None,
        'comments': None,
    },
}

conceptmaps = {
    'file_name': '/home/ehrqcadmin/workspace/ehr_data/blood_pos_cohort_20231023/concepts_mapped.csv',
    'file_separator': '\t',
    'column_mapping': {
        'concept_name': 'searchPhrase',
        'snomed_concept_id': 'snomedConceptId',
    },
}

