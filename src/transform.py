from src.constants import columns_from_to_dict, english_months
import pandas as pd
import logfire

logfire = logfire.configure()

def identify_cents_in_number(value: str) -> float:
    """
    This function identifies if a float column has cents.
    
    Parameters
    ----------
    value : float
    The value to be checked.
    
    Returns
    float
    The value with cents or not.
    """
    
    try:
        cleanned_value = value.replace('.', '')
        full_value = cleanned_value.split(',')
        last_value = full_value[-1]
        if len(last_value) == 2:
            correct_value = float(''.join(full_value[:-1]) + '.' + last_value)
        else:
            correct_value = int(value.replace(',', '').replace('.', ''))
            
        return correct_value
    except:
        value = value
        return value    

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
    
    df = df.dropna(how='all')
    
    logfire.info("Dropped duplicates.", context={"rows": len(df)})
    
    for column in df.columns:
        if column in ['Month', 'State']:
            df[column] = df[column].str.strip()
        else:
            df[column] = df[column].fillna(0)
            df[column] = df[column].apply(lambda x: identify_cents_in_number(x))    
    logfire.info("Stripped strings and filled NaN values.", context={"columns": list(df.columns)})
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
    df['Month'] = df['Month'].map(english_months)
    logfire.info("Months translated.", context={"months": list(df['Month'].unique())})
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
    
    for column in df.columns:
        if column in int_column_list:
            df[column] = df[column].astype('int')
        elif column in ['Month', 'State']:
            df[column] = df[column].astype('object')        
        else:
            df[column] = df[column].astype('float')
    
    logfire.info("Columns data types defined.", context={"columns": list(df.columns)})
    
    return df
    