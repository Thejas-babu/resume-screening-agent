import pandas as pd

def rank_candidates(results):
    df = pd.DataFrame(results)
    return df.sort_values(by="score", ascending=False)
