import pandas as pd


def save_csv(products):

    df = pd.DataFrame(products)

    df.to_csv("products.csv", index=False)

    print("CSV Saved Successfully")