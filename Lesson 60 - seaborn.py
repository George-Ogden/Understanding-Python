import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")
print(tips.info())

plt.hist(tips["total_bill"])

themes = ["paper","notebook","talk","poster"]

for theme in themes:
    sns.set_theme(theme)
    sns.displot(x=tips["total_bill"])

sns.catplot(x="day",y="total_bill",hue="sex",data=tips)

palettes = ["deep","muted","bright","pastel","dark","colorblind"]
for palette in palettes:
    sns.scatterplot(x="tip",y="total_bill",hue="day",style="time",size="size",data=tips,legend="brief",palette=palette)

sns.catplot(x="day",y="tip",col="time",data=tips)

sns.boxplot(y="tip",x="day",hue="time",orient="v",data=tips)

sns.jointplot(x="total_bill",y="tip",kind="reg",data=tips)

sns.pairplot(tips, hue="day",corner=True,kind="kde")

sns.histplot(x="tip",y="total_bill",data=tips)
sns.kdeplot(x="tip",y="total_bill",data=tips)

g = sns.FacetGrid(tips,col="sex",row="smoker",hue="day")
g = sns.FacetGrid(tips,col="day",row="time",hue="size",despine=False)

g.map(sns.scatterplot,"total_bill","tip")
g.add_legend()

plt.show()