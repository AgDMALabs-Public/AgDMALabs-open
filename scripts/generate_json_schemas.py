import json
from pathlib import Path

from open_aglabs.annotations.models import (
    OrganismProperties,
    PlantDevelopmentalStage,
    PlantStructure,
)

ANNOTATION_MODELS = [OrganismProperties, PlantDevelopmentalStage, PlantStructure]

from open_aglabs.applicator.models import (
    ApplicationEvent,
    ApplicatorZone,
    ApplicatorRx
)

APPLICATOR_MODELS = [ApplicationEvent, ApplicatorZone, ApplicatorRx]

from open_aglabs.core.base_models import (
    MLOutput,
    ImageTransformations,
    Location
)

CORE_MODELS = [MLOutput, ImageTransformations, Location]

from open_aglabs.field_management.models import (
    TillageEvent,
    FieldManagement
)

FIELD_MGMT_MODELS = [TillageEvent, FieldManagement]

from open_aglabs.harvest.models import (
    HarvestEvent,
)

HARVEST_MODELS = [HarvestEvent]

from open_aglabs.image.models import (
    ImageProtocol,
    AgronomicProperties,
    CameraProperties,
    AcquisitionProperties,
    ImageQuality,
    Image
)

IMAGE_MODELS = [ImageProtocol, AgronomicProperties, CameraProperties, AcquisitionProperties, ImageQuality, Image]

from open_aglabs.planting.models import (
    PlantingEvent
)

PLANTING_MODELS = [PlantingEvent]

from open_aglabs.products.models import (
    NutrientComposition,
    PesticideProduct,
    IngredientModel,
    Product
)

PRODUCT_MODELS = [NutrientComposition, PesticideProduct, IngredientModel, Product]

from open_aglabs.soil.models import (
    SoilAnalysis,
    SoilSample
)

SOIL_MODELS = [SoilAnalysis, SoilSample]

from open_aglabs.tank_mix.models import (
    SimpleProduct,
    TankMix,
)

TANK_MIX_MODELS = [SimpleProduct, TankMix]

from open_aglabs.tissue.models import (
    TissueAnalysis,
    TissueSample
)

TISSUE_MODELS = [TissueAnalysis, TissueSample]


def generate_schemas(models, schemas_dir):
    schemas_dir.mkdir(exist_ok=True)

    for model_class in models:
        schema = model_class.model_json_schema()
        file_name = f"{model_class.__name__.lower()}_schema.json"
        file_path = schemas_dir / file_name

        with open(file_path, "w") as f:
            json.dump(schema, f, indent=4)
        print(f"Generated schema for {model_class.__name__} at {file_path}")


# ---------------------------------------------Annotations Models------------------------------------------------------#
if len(ANNOTATION_MODELS) > 0:
    generate_schemas(models=ANNOTATION_MODELS,
                     schemas_dir=Path("open_aglabs/annotations/schemas"))

# ----------------------------------------------Applicator Models------------------------------------------------------#
if len(APPLICATOR_MODELS) > 0:
    generate_schemas(models=APPLICATOR_MODELS,
                     schemas_dir=Path("open_aglabs/applicator/schemas"))

# ----------------------------------------------------CORE Models------------------------------------------------------#
if len(CORE_MODELS) > 0:
    generate_schemas(models=CORE_MODELS,
                     schemas_dir=Path("open_aglabs/core/schemas"))

# ---------------------------------------FIELD MANAGEMENT Models-------------------------------------------------------#
if len(FIELD_MGMT_MODELS) > 0:
    generate_schemas(models=FIELD_MGMT_MODELS,
                     schemas_dir=Path("open_aglabs/field_management/schemas"))

# -------------------------------------------------HARVEST Models------------------------------------------------------#
if len(HARVEST_MODELS) > 0:
    generate_schemas(models=HARVEST_MODELS,
                     schemas_dir=Path("open_aglabs/harvest/schemas"))

# ---------------------------------------------------IMAGE Models------------------------------------------------------#
if len(IMAGE_MODELS) > 0:
    generate_schemas(models=IMAGE_MODELS,
                     schemas_dir=Path("open_aglabs/image/schemas"))

# -------------------------------------------------PLANTING Models-----------------------------------------------------#
if len(PLANTING_MODELS) > 0:
    generate_schemas(models=PLANTING_MODELS,
                     schemas_dir=Path("open_aglabs/planting/schemas"))

# -------------------------------------------------PRODUCT Models------------------------------------------------------#
if len(PRODUCT_MODELS) > 0:
    generate_schemas(models=PRODUCT_MODELS,
                     schemas_dir=Path("open_aglabs/products/schemas"))

# -------------------------------------------------SOIL Models---------------------------------------------------------#
if len(SOIL_MODELS) > 0:
    generate_schemas(models=SOIL_MODELS,
                     schemas_dir=Path("open_aglabs/soil/schemas"))

# -------------------------------------------------TANK Models---------------------------------------------------------#
if len(TANK_MIX_MODELS) > 0:
    generate_schemas(models=TANK_MIX_MODELS,
                     schemas_dir=Path("open_aglabs/tank_mix/schemas"))

# -------------------------------------------------TISSUE Models-------------------------------------------------------#
if len(TISSUE_MODELS) > 0:
    generate_schemas(models=TISSUE_MODELS,
                     schemas_dir=Path("open_aglabs/tissue/schemas"))