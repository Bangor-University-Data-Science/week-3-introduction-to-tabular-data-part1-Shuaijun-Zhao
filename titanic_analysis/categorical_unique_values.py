import pandas as pd

def display_unique_values(df, categorical_features):
    """
    Displays unique values for each categorical feature in the DataFrame.
    
    Args:
        df (pd.DataFrame): The Titanic dataset as a DataFrame.
        categorical_features (list): List of categorical feature names.
    
    Returns:
        dict: A dictionary where keys are feature names and values are the unique values.
    """
    unique_values = {}
    for feature in categorical_features:
        if feature in df:
            unique_values[feature] = df[feature].unique()  # List of unique values for each categorical feature
    return unique_values

df = pd.read_csv('data/titanic.csv')
categorical_features = df.select_dtypes(include=['object', 'category', 'bool']).columns.to_list()
print (display_unique_values(df, categorical_features))
