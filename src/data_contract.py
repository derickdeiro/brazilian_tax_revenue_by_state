import pandera as pa
import logfire
import pandas as pd
from src.constants import states_list

logfire.configure()

data_schema = pa.DataFrameSchema(
    {
    'Year': pa.Column(int, pa.Check.greater_than_or_equal_to(2000), nullable=False),
    'Month': pa.Column(str, pa.Check.isin(['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']), nullable=False),
    'State': pa.Column(str, pa.Check.isin(states_list), nullable=False),
    'Import Tax': pa.Column(float, nullable=False),
    'Export Tax': pa.Column(float, nullable=False),
    'Excise Tax - Tobacco': pa.Column(float, nullable=False),
    'Excise Tax - Beverages': pa.Column(float, nullable=False),
    'Excise Tax - Automobiles': pa.Column(float, nullable=False),
    'Excise Tax - Linked to Import': pa.Column(float, nullable=False),
    'Excise Tax - Others': pa.Column(float, nullable=False),
    'Individual Income Tax': pa.Column(float, nullable=False),
    'Corporate Income Tax - Financial Entities': pa.Column(float, nullable=False),
    'Corporate Income Tax - Other Companies': pa.Column(float, nullable=False),
    'Withholding Tax - Employment Income': pa.Column(float, nullable=False),
    'Withholding Tax - Capital Income': pa.Column(float, nullable=False),
    'Withholding Tax - Transfers Abroad': pa.Column(float, nullable=False),
    'Withholding Tax - Other Income': pa.Column(float, nullable=False),
    'Tax on Financial Transactions': pa.Column(float, nullable=False),
    'Rural Land Tax': pa.Column(float, nullable=False),
    'Provisional Tax on Financial Transactions - IPMF': pa.Column(float, nullable=False),
    'Provisional Contribution on Financial Transactions': pa.Column(float, nullable=False),
    'Contribution for Social Security Financing': pa.Column(int, nullable=False),
    'Contribution for Social Security Financing - Financial Entities': pa.Column(float, nullable=False),
    'Contribution for Social Security Financing - Others': pa.Column(int, nullable=False),
    'Contribution to PIS/PASEP': pa.Column(int, nullable=False),
    'Contribution to PIS/PASEP - Financial Entities': pa.Column(float, nullable=False),
    'Contribution to PIS/PASEP - Others': pa.Column(int, nullable=False),
    'Social Contribution on Net Profit': pa.Column(float, nullable=False),
    'Social Contribution on Net Profit - Financial Entities': pa.Column(float, nullable=False),
    'Social Contribution on Net Profit - Others': pa.Column(float, nullable=False),
    'CIDE-Fuels (Non-Deductible Portion)': pa.Column(float, nullable=False),
    'CIDE-Fuels': pa.Column(float, nullable=False),
    'Contribution to Social Security Plan for Public Servants': pa.Column(float, nullable=False),
    'CPSSS - Contribution to Public Servants Social Security Plan': pa.Column(float, nullable=False),
    'Contributions to FUNDAF': pa.Column(float, nullable=False),
    'Tax Recovery Program (REFIS)': pa.Column(int, nullable=False),
    'Special Installment Program (PAES)': pa.Column(int, nullable=False),
    'Withholding at Source - Law 10.833, Art. 30': pa.Column(int, nullable=False),
    'Unified Payment': pa.Column(int, nullable=False),
    'Other Administered Revenues': pa.Column(float, nullable=False),
    'Other Revenues': pa.Column(float, nullable=False),
    'Social Security Revenue': pa.Column(float, nullable=False),
    'Social Security Revenue - Own Resources': pa.Column(float, nullable=False),
    'Social Security Revenue - Other Sources': pa.Column(float, nullable=False),
    'Administered by Other Agencies': pa.Column(float, nullable=False),
    }
)


def schema_validator(df: pd.DataFrame) -> pd.DataFrame:
    """
    This function validates the DataFrame against the data schema.
    
    Parameters
    ----------
    df : pd.DataFrame
    The DataFrame to be validated.
    
    Returns
    pd.DataFrame
    The DataFrame with the schema validated. 
    """
    validated_df = data_schema.validate(df)
    logfire.info("Data schema validated.", context={"columns": list(validated_df.columns)})
    return validated_df