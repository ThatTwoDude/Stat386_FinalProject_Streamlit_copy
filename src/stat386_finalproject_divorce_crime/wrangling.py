from pathlib import Path
import pandas as pd
import json

def load_data(file_path: str | Path) -> pd.DataFrame:
    """
    Load data from a file

    Parameters
    ----------
    file_path : str or Path

    Returns 
    ----------
    pd.DataFrame
    """
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")
    
    suffix = path.suffix.lower()
    if suffix == ".csv":
        return pd.read_csv(path)
    elif suffix == ".parquet":
        return pd.read_parquet(path)
    else:
        raise ValueError("File must be a .csv or .parquet file")


def load_offense_mapping(json_path: str | Path) -> dict:
    """
    Load crime offense mapping json

    Parameters
    ----------
    json_path : str or Path

    Returns 
    ----------
    dict
    """
    path = Path(json_path)
    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")
    
    suffix = path.suffix.lower()
    if suffix == ".json":
        with open(path, 'r') as file:
            crime_json = json.load(file)
            offense_map = crime_json["offenses"]
            return offense_map
    else:
        raise ValueError("File must be a .json file")


    
