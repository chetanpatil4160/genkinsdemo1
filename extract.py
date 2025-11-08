import pandas as pd

data = {
    "id":[1,2,3],
    "name":["a","b","c"],
    "age":[10,20,30]
}

df = pd.DataFrame(data)
print(df)