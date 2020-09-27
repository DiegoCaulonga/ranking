import requests
import pandas as pd

"""
def title(x):
    url = f"https://api.github.com/repos/ironhack-datalabs/datamad0820/pulls?state=all&page={x}&per_page=100"
    api = requests.get(url)
    tabla = api.json()
    norm = pd.json_normalize(tabla)
    w = norm[["title"]]
    e = pd.DataFrame(w.title.str.split(" ",1).tolist(),columns=["lab","student"])
    return e 

a = title(1)
b = title(2)
c = title(3)
d = title(4)
e = title(5)
f = title(6)

result1 = pd.concat([a,b,c,d,e,f],axis=0,sort=False)
result1
"""