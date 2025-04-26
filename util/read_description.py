import pandas as pd
from typing import List

DEFAULT = "data/extracted_fields_fixed.csv"


def extract_customer_descriptions(csv_file_path: str = DEFAULT) -> List[str]:
    df = pd.read_csv(csv_file_path)
    if '客户描述记录' not in df.columns:
        raise ValueError("CSV文件中没有找到 '客户描述记录' 这一列")

    descriptions = df['客户描述记录'].dropna().astype(str).tolist()
    return descriptions


if __name__ == "__main__":
    descriptions = extract_customer_descriptions("data/extracted_fields_fixed.csv")
    print(descriptions)