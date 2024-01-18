# %%
import seaborn as sns 
import matplotlib.pyplot as plt

# Load the Planets dataset from seaborn
planets_df=sns.load_dataset('planets')
planets_df

# 1. Scatter plot: Visualize the relationship between 'orbital_period' and 'mass' of the planets
# %%
sns.scatterplot(x='orbital_period',y='mass',data=planets_df)
plt.title("Orbital Period vs. Mass of Planets")
plt.xlabel("Orbital Period (days)")
plt.ylabel("Mass (Jupiter Mass)")
plt.savefig("scatter_plot.png")
plt.show()
# %%
# Bar plot: Display the count of planets discovered by each method.
sns.countplot(x='method', data=planets_df)
plt.xticks(rotation=90)
plt.title("Count of Planets Discovered by Method")
plt.xlabel("Discovery Method")
plt.ylabel("Count")
plt.savefig("bar_plot.png")
plt.show()
# %%
# Histogram: Visualize the distribution of 'distance' of planets from their respective stars.
sns.histplot(x='distance',data=planets_df,bins=20,kde=True)
plt.title("Distribution of Distance of Planets from Stars")
plt.xlabel("Distance (parsecs)")
plt.ylabel("Count")
plt.savefig("histogram_plot.png")
plt.show()
# %%
# Pair plot: Show pairwise relationships between 'orbital_period', 'mass', 'year', and 'distance'
sns.pairplot(planets_df[['orbital_period', 'mass', 'year', 'distance']])
plt.suptitle("Pairwise Relationships in Planets Dataset", y=1.02)
plt.savefig("Pair_plot.png")
plt.show()
# %%
# Violin plot: Compare the distribution of 'year' for different 'method' of planet discovery.
sns.violinplot(x='method', y='year', data=planets_df)
plt.xticks(rotation=90)
plt.title("Distribution of Year for Different Discovery Methods")
plt.xlabel("Discovery Method")
plt.ylabel("Year")
plt.savefig("Violin_plot.png")
plt.show()
# %%
# Swarm plot: Visualize the 'mass' of planets discovered by different 'method'
sns.swarmplot(x='method', y='mass', data=planets_df)
plt.xticks(rotation=90)
plt.title("Mass of Planets Discovered by Different Methods")
plt.xlabel("Discovery Method")
plt.ylabel("Mass (Jupiter Mass)")
plt.savefig("Swarm_plot.png")
plt.show()
# %%
# Heatmap: Create a heatmap to show the correlation matrix between numerical columns in the dataset.
numeric_col=planets_df.select_dtypes(include=['float64','int64']).columns
numeric_corr=planets_df[numeric_col].corr()
sns.heatmap(numeric_corr, annot=True, cmap='coolwarm')
plt.title("Correlation Matrix Heatmap")
plt.savefig("heatmap_plot.png")
plt.show()
# %%
# Point plot: Compare the mean 'orbital_period' for each 'year' of planet discovery.
sns.pointplot(x='year', y='orbital_period', data=planets_df, ci=None)
plt.xticks(rotation=90)
plt.title("Mean Orbital Period for Each Year")
plt.xlabel("Year")
plt.ylabel("Mean Orbital Period (days)")
plt.savefig("Point_plot.png")
plt.show()
# %%
# Bar plot with error bars: Show the mean 'mass' of planets for different 'method' of discovery with confidence intervals.
sns.barplot(x='method', y='mass', data=planets_df, ci='sd')
plt.xticks(rotation=90)
plt.title("Mean Mass of Planets Discovered by Different Methods")
plt.xlabel("Discovery Method")
plt.ylabel("Mean Mass (Jupiter Mass)")
plt.savefig("Bar_plot.png")
plt.show()
# %%
planets_df.to_csv('planets.csv')
# %%
