import pandas as pd
from app.core.database import SessionLocal

def load_csv(file_path:str):
    return pd.read_csv(file_path, sep=";")

def validate_row(row):
    if pd.isna(row['year']) or pd.isna(row['title']):
        return False
    return True

def main():
    session = SessionLocal()

    try:
        df = load_csv("../../../dump-database.csv")

        for _, row in df.iterrows():
            if not validate_row(row):
                continue

    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()