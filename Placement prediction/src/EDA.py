import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# -----------------------------
# Load Dataset
# -----------------------------
df = pd.read_csv("../data/placement_predict_50k Dataset (2).csv")

# -----------------------------
# Print Dataset Information
# -----------------------------
print("Dataset Shape:", df.shape)
print("\nColumns:")
print(df.columns.tolist())

# -----------------------------
# Select Numerical Columns
# -----------------------------
cols = [
    'CGPA',
    'Internships',
    'CodingTestScore',
    'SoftSkillsRating'
]

# -----------------------------
# Pair Plot
# -----------------------------
sns.set_theme(style="white", font_scale=1.1)

g = sns.pairplot(
    df[cols],
    diag_kind="kde",
    height=3,
    plot_kws={
        "color": "teal",
        "s": 25,
        "alpha": 0.6
    },
    diag_kws={
        "fill": True,
        "color": "teal"
    }
)

g.fig.suptitle(
    "Pair Plot & Scatter Plot Matrix",
    fontsize=18,
    y=1.02
)

plt.show()