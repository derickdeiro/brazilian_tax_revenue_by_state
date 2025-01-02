import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
            
import logfire
logfire.configure()
logfire.install_auto_tracing(modules=['src'], min_duration=0.01)
logfire.instrument_system_metrics()

from src.extract import get_br_gov_data
from src.transform import clean_dataframe, rename_columns_to_english

if __name__ == '__main__':

    df_raw = get_br_gov_data()
    
    df_cleanned = clean_dataframe(df_raw)
    
    df_english = rename_columns_to_english(df_cleanned)
    
    print(df_english.dtypes)