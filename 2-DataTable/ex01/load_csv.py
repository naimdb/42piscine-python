import pandas as pd


def load(path: str) -> pd.DataFrame | None:
    """
    Load a CSV dataset and print its dimensions.

    Args:
        path: Path to the CSV file

    Returns:
        DataFrame if successful, None otherwise
    """

    try:
        dataframe = pd.read_csv(path)
        print(f"Loading dataset of dimensions {dataframe.shape}")
        return dataframe
    except FileNotFoundError:
        print(f"Error: File at path '{path}' not found.")
        return None
    except pd.errors.EmptyDataError:
        print(f"Error: File at path '{path}' is empty.")
        return None
    except pd.errors.ParserError:
        print(f"Error: File at path '{path}' has bad format.")
        return None
    except Exception as e:
        print(f"Error: An unexpected error occurred: {e}")
        return None
