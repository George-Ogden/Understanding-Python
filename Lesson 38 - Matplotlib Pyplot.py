import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.DataFrame(columns=("weight","height"))
df["weight"] = np.random.normal(loc=70, scale=5, size=(1000))
df["height"] = np.random.normal(loc=1.8, scale=0.05, size=(1000))

# print(df)
# plt.plot(df)

fig, axs = plt.subplots(3,2,num="Health Data")
axs[0,0].scatter(df["weight"],df["height"],marker="x",c="black")
axs[0,1].hist2d(df["weight"],df["height"])

axs[1,0].hist(df["height"],color="b")
axs[1,1].hist(df["weight"],color="g")

df["bmi"] = df["weight"] / df["height"] ** 2

bmi = plt.subplot(3,1,3)
bmi.hist(df["bmi"],color="r")
bmi.title.set_text("BMI")

axs[1,0].title.set_text("Height")
axs[1,1].title.set_text("Weight")

axs[0,0].set_xlabel("Weight")
axs[0,0].set_ylabel("Height")
axs[0,1].set_xlabel("Weight")
axs[0,1].set_ylabel("Height")

fig.tight_layout()

plt.get_current_fig_manager().full_screen_toggle()

plt.show()