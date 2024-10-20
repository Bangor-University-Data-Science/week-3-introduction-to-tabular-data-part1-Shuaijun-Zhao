# import pandas as pd

# def load_titanic_data(filepath: str) -> pd.DataFrame:
#     """
#     Loads the Titanic dataset from the specified file path.
    
#     Args:
#         filepath (str): Path to the Titanic CSV file.
    
#     Returns:
#         pd.DataFrame: Loaded Titanic dataset as a DataFrame.
#     """
#     df = pd.read_csv(filepath)
#     return df

# print(load_titanic_data("data/titanic.csv")) 

import pandas as pd

def load_titanic_data(filepath: str) -> pd.DataFrame:
    """
    Loads the Titanic dataset from the specified file path.
    
    Args:
        filepath (str): Path to the Titanic CSV file.
    
    Returns:
        pd.DataFrame: Loaded Titanic dataset as a DataFrame.
    """
    try:
        df = pd.read_csv(filepath)
        
        # Check if essential columns are present
        required_columns = ['Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp', 'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked']
        for col in required_columns:
            if col not in df.columns:
                raise ValueError(f"Missing required column: {col}")
        
        return df
    except FileNotFoundError:
        print(f"Error: The file at {filepath} was not found.")
        return pd.DataFrame()  # Return an empty DataFrame
    except pd.errors.EmptyDataError:
        print("Error: The file is empty.")
        return pd.DataFrame()  # Return an empty DataFrame
    except ValueError as ve:
        print(ve)
        return pd.DataFrame()  # Return an empty DataFrame
    except Exception as e:
        print(f"An error occurred: {e}")
        return pd.DataFrame()  # Return an empty DataFrame

# Example usage
print(load_titanic_data("data/titanic.csv"))

