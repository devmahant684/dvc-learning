import os
import pandas as pd
from sklearn.datasets import load_iris

# 1. Create a "data" directory if it doesn't exist
data_dir = "data"
os.makedirs(data_dir, exist_ok=True)

# 2. Load Iris dataset
iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['target'] = iris.target

# 3. Save dataset to CSV inside "data" folder
csv_path = os.path.join(data_dir, "iris.csv")
df.to_csv(csv_path, index=False)

print(f"Dataset saved to {csv_path}")
