from src.constants import columns_from_to_dict
import pandas as pd
import logfire

logfire = logfire.configure()

@logfire.instrument(span_name='transform_brazilian_tax_revenue_data')
def clean_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """
    This function removes duplicates from the DataFrame.
    
    Parameters
    ----------
    df : pd.DataFrame
    The DataFrame to be cleaned.
        
    Returns
    pd.DataFrame    
    The cleaned DataFrame.  
    """
    df = df.drop_duplicates()
    
    logfire.info("Dropped duplicates.", context={"rows": len(df)})    
    return df

@logfire.instrument(span_name='transform_brazilian_tax_revenue_data')
def rename_columns_to_english(df: pd.DataFrame) -> pd.DataFrame:
    """
    This function renames the columns of the DataFrame to English.
    
    Parameters
    ----------
    df : pd.DataFrame
    The DataFrame to be renamed.
    
    Returns
    pd.DataFrame
    The DataFrame with the columns renamed.
    """
    df = df.rename(columns=columns_from_to_dict)
    logfire.info("Columns renamed.", context={"columns": list(df.columns)})
    return df


@logfire.instrument(span_name='transform_brazilian_tax_revenue_data')
def define_columns_dtypes(df: pd.DataFrame) -> pd.DataFrame:
    """
    This function defines the data types of the columns in the DataFrame.
    
    Parameters
    ----------
    df : pd.DataFrame
    The DataFrame to be transformed.
    
    Returns
    pd.DataFrame
    The DataFrame with the columns' data types defined.
    """
    
    int_column_list = ['Year', 
                       'Contribution for Social Security Financing', 
                       'Contribution for Social Security Financing - Others',
                       'Contribution to PIS/PASEP',
                       'Contribution to PIS/PASEP - Others',
                       'Special Installment Program (PAES)',
                       'Tax Recovery Program (REFIS)',
                       'Withholding at Source - Law 10.833, Art. 30',
                       'Unified Payment']
    
    for column in df.columns():
        if column in int_column_list:
            df[column] = df[column].astype('int')
        elif column in ['Month', 'State']:
            df[column] = df[column].astype('object')        
        else:
            df[column] = df[column].astype('float')
    