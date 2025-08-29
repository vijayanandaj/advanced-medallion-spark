from pathlib import Path
from faker import Faker
from random import randint, choice
import pandas as pd

def main(n=2000, seed=42, outdir="datasets"):
    Path(outdir).mkdir(exist_ok=True)
    Faker.seed(seed)
    fake = Faker()

    rows = []
    for i in range(n):
        rows.append({
            "id": i + 1,
            "user_id": randint(1, 100),
            "event": choice(["impression","click","view","add_to_cart","purchase"]),
            "ts": pd.Timestamp("2024-01-01") + pd.to_timedelta(randint(0, 60*60*24*14), unit="s"),
            "referrer": choice(["direct","email","ad","search"]),
            "price": round(abs(fake.pyfloat(left_digits=2, right_digits=2)), 2),
        })

    df = pd.DataFrame(rows).sort_values("ts")
    df.to_parquet(f"{outdir}/clickstream.parquet", index=False)
    df.to_csv(f"{outdir}/clickstream.csv", index=False)
    print(f"Wrote {outdir}/clickstream.parquet and {outdir}/clickstream.csv with {len(df)} rows")

if __name__ == "__main__":
    main()
