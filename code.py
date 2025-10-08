import os
import pandas as pd

def main():
    data_dir = "data"
    os.makedirs(data_dir, exist_ok=True)

    # Version 3: 7 friends
    friends = ["Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace"]
    df = pd.DataFrame({"name": friends})

    csv_path = os.path.join(data_dir, "friends.csv")
    df.to_csv(csv_path, index=False)

    print(f"✅ Friends list (v3) saved to {csv_path}")

if __name__ == "__main__":
    main()
