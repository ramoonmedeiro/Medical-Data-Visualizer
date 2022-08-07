# coded by Ramon Medeiro. Please use this content only to knowledge. Try to do this project yourself.
# FREECODECAMP project 4.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('./medical_examination.csv')

# Add 'overweight' column
df['BMI'] = df['weight']/((df['height']*0.01)**2)
df['overweight'] = df['BMI'].apply(lambda x: 0 if x <= 25 else 1)
del df['BMI']

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df['cholesterol'] = df['cholesterol'].apply(lambda x: 1 if x > 1 else 0)
df['gluc'] = df['gluc'].apply(lambda x: 1 if x > 1 else 0)

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    var = sorted(["cholesterol", "gluc", "smoke", "alco", "active", "overweight"])

    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    df_melt = pd.melt(df, id_vars="cardio", value_vars=var)
    df_cat = df_melt.value_counts().reset_index(name="total")    

    # Draw the catplot with 'sns.catplot()'

    fig = sns.catplot(data=df_cat, x = "variable", y = "total", col = "cardio", hue = "value", kind = "bar", order=var)


    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df.loc[
        (df["ap_lo"] <= df["ap_hi"])
        & (df["height"] >= df["height"].quantile(0.025))
        & (df["height"] <= df["height"].quantile(0.975))
        & (df["weight"] >= df["weight"].quantile(0.025))
        & (df["weight"] <= df["weight"].quantile(0.975))
    ]

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mascara = np.zeros_like(corr)
    mascara[np.triu_indices_from(mascara)] = True


    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(12, 9))

    # Draw the heatmap with 'sns.heatmap()'
    ax = sns.heatmap(corr,mask=mascara,vmax=0.4,square=True,fmt=".1f",annot=True)


    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
