import geopandas as gpd
import pandas as pd
from shapely import wkt

from datetime import datetime
from .models import SoilSample, SoilAnalysis
from ..core.base_models import Location
from ..core.ingest import dict_to_model

def load_soil_analysis_row_to_model


def soil_samples_to_geodataframe(soil_samples: list) -> gpd.GeoDataFrame:
    """
    Convert a list of SoilSample objects into a GeoDataFrame.

    Args:
        soil_samples: List of SoilSample objects

    Returns:
        geopandas.GeoDataFrame: GeoDataFrame with soil sample data and geometry

    Raises:
        ImportError: If geopandas is not installed
        ValueError: If soil_samples is empty or contains invalid data
    """
    if not soil_samples:
        raise ValueError("soil_samples list cannot be empty")

    # Prepare data for DataFrame
    data = []
    for sample in soil_samples:
        # Flatten the nested structure
        row = {
            'sample_id': sample.sample_id,
            'timestamp': sample.timestamp,
            'lab_id': sample.lab_id,
            'sample_radius_m': sample.sample_radius_m,
            'start_depth_cm': sample.start_depth_cm,
            'end_depth_cm': sample.end_depth_cm,
            'extraction_type': sample.extraction_type,
            'location_id': sample.location.id,
            'location_name': sample.location.name,
            'latitude': sample.location.latitude,
            'longitude': sample.location.longitude,
            'elevation_m': sample.location.elevation_m,
            'location_crs': sample.location.crs,

            # analysis results
            'ph': sample.analysis_results.ph,
            'organic_matter_percent': sample.analysis_results.organic_matter_percent,
            'nitrogen_ppm': sample.analysis_results.nitrogen_ppm,
            'phosphorus_ppm': sample.analysis_results.phosphorus_ppm,
            'potassium_ppm': sample.analysis_results.potassium_ppm,
            'sulfur_ppm': sample.analysis_results.sulfur_ppm,
            'calcium_ppm': sample.analysis_results.calcium_ppm,
            'magnesium_ppm': sample.analysis_results.magnesium_ppm,
            'zinc_ppm': sample.analysis_results.zinc_ppm,
            'iron_ppm': sample.analysis_results.iron_ppm,
            'manganese_ppm': sample.analysis_results.manganese_ppm,
            'copper_ppm': sample.analysis_results.copper_ppm,
            'boron_ppm': sample.analysis_results.boron_ppm,
            'molybdenum_ppm': sample.analysis_results.molybdenum_ppm,
            'cation_exchange_capacity': sample.analysis_results.cation_exchange_capacity,
        }

        # Parse geometry from WKT if available
        if sample.location.geometry:
            row['geometry'] = wkt.loads(sample.location.geometry)
        else:
            # Fall back to creating Point from lat/lon if geometry is not provided
            if sample.location.latitude is not None and sample.location.longitude is not None:
                from shapely.geometry import Point
                row['geometry'] = Point(sample.location.longitude, sample.location.latitude)
            else:
                row['geometry'] = None

        data.append(row)

    # Create GeoDataFrame
    gdf = gpd.GeoDataFrame(data, geometry='geometry')

    # Set CRS if available (default to WGS84 if not specified)
    if data[0].get('crs'):
        gdf.set_crs(data[0]['crs'], inplace=True)
    else:
        gdf.set_crs('EPSG:4326', inplace=True)

    return gdf


def dataframe_to_soil_samples(df: pd.DataFrame) -> list:
    """
    Convert a pandas DataFrame into a list of SoilSample objects.

    The DataFrame should have columns matching the flattened structure from
    soil_samples_to_geodataframe, including:
    - sample_id, timestamp, lab_id, sample_radius_m, start_depth_cm, end_depth_cm, extraction_type
    - location fields: location_id, location_name, latitude, longitude, elevation_m, crs, etc.
    - analysis results: ph, organic_matter_percent, nitrogen_ppm, phosphorus_ppm, etc.
    - notes (as list or string)
    - geometry (optional, for GeoDataFrames)

    Args:
        df: pandas DataFrame or GeoDataFrame with soil sample data

    Returns:
        list: List of SoilSample objects

    Raises:
        ValueError: If required columns are missing or data is invalid
        ValidationError: If the data doesn't match the SoilSample model requirements
    """

    if df.empty:
        raise ValueError("DataFrame cannot be empty")


    soil_samples = []

    for idx, row in df.iterrows():
        # Handle geometry for WKT conversion
        geometry_wkt = None
        if 'geometry' in df.columns and row.get('geometry') is not None:
            try:
                from shapely import wkt as wkt_module
                geometry_wkt = wkt_module.dumps(row['geometry'])
            except Exception:
                # If geometry column exists but can't be converted, use lat/lon for WKT
                if row.get('latitude') is not None and row.get('longitude') is not None:
                    geometry_wkt = f"POINT ({row['longitude']} {row['latitude']})"
        elif row.get('latitude') is not None and row.get('longitude') is not None:
            # Create WKT from lat/lon if no geometry column
            geometry_wkt = f"POINT ({row['longitude']} {row['latitude']})"

        # Build Location object
        location = dict_to_model(data=row.to_dict(), model_class=Location)

        # Build SoilAnalysis object
        analysis = dict_to_model(data=row.to_dict(), model_class=SoilAnalysis)

        # Handle notes - could be a list, string, or None
        notes = row.get('notes', [])
        if isinstance(notes, str):
            # If notes is a string, convert to list
            notes = [notes] if notes else []
        elif notes is None or (
                hasattr(notes, '__iter__') and not isinstance(notes, str) and len(notes) == 0):
            notes = []
        elif not isinstance(notes, list):
            notes = list(notes)

        # Handle timestamp - convert string to datetime if needed
        timestamp = row.get('timestamp')

        if isinstance(timestamp, str):
            # Try to parse ISO format or common datetime formats
            try:
                timestamp = datetime.fromisoformat(timestamp.replace('Z', '+00:00'))
            except Exception:
                timestamp = datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S')

        # Build SoilSample object
        sample = SoilSample(
            sample_id=row.get('sample_id'),
            timestamp=timestamp,
            lab_id=row.get('lab_id'),
            sample_radius_m=row['sample_radius_m'],
            start_depth_cm=row['start_depth_cm'],
            end_depth_cm=row['end_depth_cm'],
            extraction_type=row.get('extraction_type'),
            location=location,
            analysis_results=analysis,
            notes=notes
        )

        soil_samples.append(sample)

    return soil_samples
