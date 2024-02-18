import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
sns.set_style("dark")
sns.set()

def plot_bar(savings, usr):
    year = [i +usr.current_age for i in list(range(usr.target_year))]
    df = pd.DataFrame(
    {'year': year,
     'savings': savings
    })

    plt.figure(
    figsize=(8, 4),  # Set the figure size here
    dpi=100,  # Set the dpi (or resolution) here
    )
    ax = plt.gca()
    plt.ticklabel_format(style='plain', axis='y')
    ax.yaxis.set_major_formatter('${x:1.2f}')
    # Create a horizontal barplot
    sns.barplot(
    data=df,
    x="year",  # Set the variable for the width of the bars
    y="savings",  # Set the categorical variable on the y-axis
    #ci=False,  # Turn off confidence intervals
    color="#2b7bba",  # Set a custom color
    )
    # Set the main title
    plt.suptitle(
    "Linda's Projected Savings",  # Main title text
    fontsize=18,  # Set the font size
    color="black",  # Set the color
    x=0.51,  # Adjust this to align with the subtitle
    y=1.01,  # Adjust this to align with the subtitle
    )

    # Set the subtitle
    plt.title(
    "In millions of dollars (USD)",  # Subtitle text
    fontsize=14,  # Set the font size
    color="grey",  # Set the color
    )
    # Set axis labels
    plt.xlabel("Age", fontsize=12)  # Set the x-axis label and fontsize
    plt.xticks(fontsize=10)  # Set the font size of the x-axis ticks
    plt.tick_params(axis="x", labelrotation= 90)
    plt.ylabel("", fontsize=12)  # Set the y-axis label and fontsize
    plt.yticks(fontsize=10)  # Set the font size of the y-axis ticks

    # Set the subtitle
    plt.title(
    "In dollars (USD)",  # Subtitle text
    fontsize=14,  # Set the font size
    color="grey",  # Set the color
    )
    # Set axis labels
    plt.xlabel("Age", fontsize=12)  # Set the x-axis label and fontsize
    plt.xticks(fontsize=10)  # Set the font size of the x-axis ticks
    plt.tick_params(axis="x", labelrotation= 90)
    plt.ylabel("", fontsize=12)  # Set the y-axis label and fontsize
    plt.yticks(fontsize=10)  # Set the font size of the y-axis ticks

    plt.ylim(0, 2000000)
    # Show the plot
    plt.show()


def plot_simulation_percentiles(usr, sav_sim):
    year = [i + usr.current_age for i in list(range(usr.target_year))]
    df = pd.DataFrame(sav_sim)
    df.columns = year

    fig = plt.figure(
        figsize=(8, 4),  # Set the figure size here
        dpi=100,  # Set the dpi (or resolution) here
    )
    ax = fig.add_subplot(111)
    plt.ylim(0, 2000000)
    plt.ticklabel_format(style='plain', axis='y')
    ax.yaxis.set_major_formatter('${x:1.2f}')
    ax.plot(np.percentile(sav_sim, 25, axis=0), c='r', linewidth=2, label="Percentile=25")
    ax.plot(np.percentile(sav_sim, 50, axis=0), c='b', linewidth=2, label="Percentile=50")
    ax.plot(np.percentile(sav_sim, 75, axis=0), c='g', linewidth=2, label="Percentile=75")

    # Set the main title
    plt.suptitle(
        "Monte Carlo Simulation of Linda's Projected Savings",  # Main title text
        fontsize=18,  # Set the font size
        color="black",  # Set the color
        x=0.51,  # Adjust this to align with the subtitle
        y=1.01,  # Adjust this to align with the subtitle
    )

    # Set the subtitle
    plt.title(
        "In dollars (USD)",  # Subtitle text
        fontsize=14,  # Set the font size
        color="grey",  # Set the color
    )

    # Set axis labels
    plt.xlabel("Age", fontsize=12)  # Set the x-axis label and fontsize
    plt.xticks(fontsize=10)  # Set the font size of the x-axis ticks
    labels = [item.get_text() for item in ax.get_xticklabels()]
    labels = [35, 40, 45, 50, 55, 60, 65]

    ax.set_xticklabels(labels)
    plt.legend(loc="upper left");