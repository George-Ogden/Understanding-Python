from tqdm.gui import trange
from tqdm import tqdm, trange
import random
import time

import pandas as pd
import numpy as np


help(tqdm.__init__)


total = 0
data = [random.random() for _ in range(1000)]
for x in tqdm(data):
    total += x ** 2
    time.sleep(1e-3)
print(total)


total = 0
for x in trange(1000, desc="Summing squares", colour="red"):
    total += random.random() ** 2
    time.sleep(1e-3)
print(total)


total = 0
t = tqdm(total=1000, desc="Summing squares", colour="red")
for x in range(100):
    for y in range(10):
        total += random.random() ** 2
        time.sleep(1e-3)
    t.update(10)
t.close()
print(total)


total = 0
t = tqdm(total=100, desc="Summing squares", colour="red")
for x in range(10):
    for y in range(100):
        total += random.random() ** 2
        time.sleep(1e-3)
        t.update()
    t.reset()
t.close()
print(total)

df = pd.DataFrame(np.random.randint(0, 1000, (10000000, 6)))
tqdm.pandas()
df.groupby(0).progress_apply(lambda x: x ** 2)


from tqdm.gui import trange

for i in trange(1000):
    time.sleep(1e-3)
