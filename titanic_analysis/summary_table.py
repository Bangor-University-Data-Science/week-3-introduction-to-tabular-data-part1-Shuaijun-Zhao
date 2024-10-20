import pandas as pd

def create_summary_table(df):
    """
    Creates a summary DataFrame with feature name, data type, number of unique values, and if it has missing values.
    
    Args:
        df (pd.DataFrame): The Titanic dataset as a DataFrame.
    
    Returns:
        pd.DataFrame: A summary DataFrame.
    """
    summary_data = {
        'Feature Name': df.columns,
        'Data Type': df.dtypes.values,
        'Number of Unique Values': df.nunique().values,
        'Has Missing Values?': df.isnull().any().values
    }
    
    summary_df = pd.DataFrame(summary_data)
    return summary_df
df = pd.read_csv('data/titanic.csv')

print (create_summary_table(df))
