from pathlib import Path
import pandas as pd
Path("datasets").mkdir(exist_ok=True)
users = pd.DataFrame({"user_id": list(range(1,101)), "segment": (["A","B","C","D"] * 25)})
users.to_parquet("datasets/users.parquet", index=False)
users.to_csv("datasets/users.csv", index=False)
print("Wrote datasets/users.parquet and datasets/users.csv")
