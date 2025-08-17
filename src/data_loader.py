import pandas as pd

class AnimeDataLoader:
    def __init__(self,original_csv:str,processed_csv:str):
        self.original_csv = original_csv
        self.processed_csv = processed_csv

    def load_and_process(self):
        df=pd.read_csv(self.original_csv, encoding='utf-8',on_bad_lines='skip').dropna() #error_bad_lines=False will ignore lines with depreciated warning , dropna will drop all rows with null value

        required_cols = {"Name","Genres","sypnopsis"}

        missing = required_cols - set(df.columns)
        if missing:#if missing has some value than it is true
            raise ValueError("Missing column in CSV File")
        
        df['combined_info'] = (
            "Title: " + df["Name"] + " Overview: " + df["sypnopsis"] + "Genres : " + df["Genres"]
        )

        df[['combined_info']].to_csv(self.processed_csv,index=False,encoding='utf-8')
        #index=False avoids extra column, make sure you keep same encoding
        return self.processed_csv
