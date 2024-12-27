import requests
import pandas as pd
import logfire
from io import StringIO

if __name__ == '__main__':

    url = 'https://www.gov.br/receitafederal/dados/arrecadacao-estado.csv'

    logfire = logfire.configure()
    logfire.i

    logfire.info("Starting the data fetching process.", context={"url": url})

    try:
        response = requests.get(url=url)
        logfire.info("Request sent to URL.", context={"status_code": response.status_code})

        if response.status_code == 200:
            logfire.info("Request successful. Processing data...")
            
            data = response.content
            csv_data = StringIO(data.decode('latin1'))
            df = pd.read_csv(csv_data, sep=';')
            
            logfire.info("Data loaded successfully.", context={
                "columns": list(df.columns),
                "rows": len(df),
                "preview": df.head(3).to_dict()
            })
        else:
            logfire.error("Failed to fetch data.", context={"status_code": response.status_code, "url": url})

    except Exception as e:
        logfire.error("An error occurred while processing the data.", context={"error": str(e)})
