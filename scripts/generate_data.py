import pandas as pd
from faker import Faker

fake = Faker()
data = pd.DataFrame({
    "id": range(1, 101),
    "name": [fake.name() for _ in range(100)],
    "email": [fake.email() for _ in range(100)],
    "amount": [round(fake.random_number(digits=5),2) for _ in range(100)],
})

data.to_csv("data/sample_data.csv", index=False)
print("Sample data generated at data/sample_data.csv")
