import pandas
import pandas as pd
from open_aglabs.annotations.models import PlantAnnotationStandardization

approved_columns = ["standardized_annotation_name", "annotation_name", "annotation_class_id", "organism_name", "organism_cultivar", "organism_family",
                    "organism_genus", "organism_species", "organism_subspecies", "plant_dev_name",
                    "plant_dev_ontology_source", "plant_dev_ontology_name", "plant_dev_ontology_id",
                    "plant_dev_growth_stage", "plant_struct_name", "plant_struct_state", "plant_struct_ontology_source",
                    "plant_struct_ontology_name", "plant_struct_ontology_id", "notes"]

def validate_annotation_csv(data_df: pd.DataFrame):
    columns = data_df.columns.tolist()
    unknown_cols = []
    missing_cols = []

    for col in columns:
        if col not in approved_columns:
            unknown_cols.append(col)

    for col in approved_columns:
        if col not in columns:
            missing_cols.append(col)

    if len(unknown_cols) > 0 or len(missing_cols) > 0:
        print(f"The following columns are not approved: {unknown_cols}")
        print(f"The following columns are missing: {missing_cols}")
        print(f" here is the approved list: {approved_columns}")
        return False

    return True


def generate_model_from_csv(data_df : pd.DataFrame):
    model_list = []
    col_validation = validate_annotation_csv(data_df)
    if not col_validation:
        print("Failed to validate the columns")
        return None

    for idx, row in data_df.iterrows():
        model_dict = {
            "annotation_name": row["annotation_name"],
            "annotation_class_id": row["annotation_class_id"],
            "standardized_annotation_name": row["standardized_annotation_name"],
            "standardized_growth_stage": row["standardized_growth_stage"],
            "organism_properties": {
                "common_name": row["organism_name"] if row["organism_name"] else None,
                "cultivar": row["organism_cultivar"] if row["organism_cultivar"] else None,
                "family": row["organism_family"] if row["organism_family"] else None,
                "genus": row["organism_genus"] if row["organism_genus"] else None,
                "species": row["organism_species"] if row["organism_species"] else None,
                "subspecies": row["organism_subspecies"] if row["organism_subspecies"] else None
            },
            "plant_development": {
                "common_name": row['plant_dev_name'] if row['plant_dev_name'] else None,
                "ontology_source": row['plant_dev_ontology_source'] if row['plant_dev_ontology_source'] else None,
                "ontology_name": row['plant_dev_ontology_name'] if row['plant_dev_ontology_name'] else None,
                "ontology_id": row['plant_dev_ontology_id'] if row['plant_dev_ontology_id'] else None,
                "crop_growth_stage": row['plant_dev_growth_stage'] if row['plant_dev_growth_stage'] else None
            },
            "plant_structure": {
                "common_name": row["plant_struct_name"] if row["plant_struct_name"] else None,
                "state": row["plant_struct_state"] if row["plant_struct_state"] else None,
                "ontology_source": row["plant_struct_ontology_source"] if row["plant_struct_ontology_source"] else None,
                "ontology_name": row["plant_struct_ontology_name"] if row["plant_struct_ontology_name"] else None,
                "ontology_id": row["plant_struct_ontology_id"] if row["plant_struct_ontology_id"] else None
            },
            "notes": row["notes"] if row["notes"] else None
        }
        model_list.append(model_dict)

    pas = {'schema_name': 'PlantAnnotationStandardization',
           'annotations': model_list}

    try:
        return PlantAnnotationStandardization(**pas)
    except Exception as e:
        print(f'Failed to make the model {e}')
        return None
