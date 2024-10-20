import pandas as pd


def get_numerical_df(df, numerical_features):
    """
    Creates a DataFrame containing only numerical features.
    
    Args:
        df (pd.DataFrame): The Titanic dataset as a DataFrame.
        numerical_features (list): List of numerical feature names.
    
    Returns:
        pd.DataFrame: DataFrame containing only numerical features.
    """
    return df[numerical_features]
df = pd.read_csv("data/titanic.csv")
numerical_features = df.select_dtypes(include=['int64', 'float64']).columns.to_list()
print(get_numerical_df(df, numerical_features))
