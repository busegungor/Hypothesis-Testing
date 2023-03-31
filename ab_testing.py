import pandas as pd
from scipy.stats import shapiro, levene, mannwhitneyu,  kruskal

# read csv data
def import_csv(dataframe):
    pd.set_option("display.max_columns", None)
    pd.set_option("display.width", 500)
    pd.set_option("display.expand_frame_repr", False)
    pd.set_option("display.float_format", lambda x: "%.5f" % x)
    df_ = pd.read_csv(dataframe)
    return df_

df_ = import_csv("BRCA.csv")
df = df_.copy()
df.head()
#      Patient_ID      Age  Gender  Protein1  Protein2  Protein3  Protein4 Tumour_Stage                      Histology ER status PR status HER2 status                 Surgery_type Date_of_Surgery Date_of_Last_Visit Patient_Status
# 0  TCGA-D8-A1XD 36.00000  FEMALE   0.08035   0.42638   0.54715   0.27368          III  Infiltrating Ductal Carcinoma  Positive  Positive    Negative  Modified Radical Mastectomy       15-Jan-17          19-Jun-17          Alive
# 1  TCGA-EW-A1OX 43.00000  FEMALE  -0.42032   0.57807   0.61447  -0.03150           II             Mucinous Carcinoma  Positive  Positive    Negative                   Lumpectomy       26-Apr-17          09-Nov-18           Dead
# 2  TCGA-A8-A079 69.00000  FEMALE   0.21398   1.31140  -0.32747  -0.23426          III  Infiltrating Ductal Carcinoma  Positive  Positive    Negative                        Other       08-Sep-17          09-Jun-18          Alive
# 3  TCGA-D8-A1XR 56.00000  FEMALE   0.34509  -0.21147  -0.19304   0.12427           II  Infiltrating Ductal Carcinoma  Positive  Positive    Negative  Modified Radical Mastectomy       25-Jan-17          12-Jul-17          Alive
# 4  TCGA-BH-A0BF 56.00000  FEMALE   0.22155   1.90680   0.52045  -0.31199           II  Infiltrating Ductal Carcinoma  Positive  Positive    Negative                        Other       06-May-17          27-Jun-19           Dead

# check_df function views quickly csv file.
def check_df(dataframe):
    print(" SHAPE ".center(70,'~'))
    print(dataframe.shape)
    print(" TYPES ".center(70,'~'))
    print(dataframe.dtypes)
    print(" HEAD ".center(70,'~'))
    print(dataframe.head())
    print(" MISSING VALUES ".center(70,'~'))
    print(dataframe.isnull().sum())
    print(" DESCRIBE ".center(70,'~'))
    print(dataframe.describe().T)
check_df(df)
df = df.dropna()

# Background
# This dataset consists of a group of breast cancer patients, who had surgery to remove their tumour.
# The dataset consists of the following variables:

# Patient_ID: unique identifier id of a patient
# Age: age at diagnosis (Years)
# Gender: Male/Female
# Protein1, Protein2, Protein3, Protein4: expression levels (undefined units)
# Tumour_Stage: I, II, III
# Histology: Infiltrating Ductal Carcinoma, Infiltrating Lobular Carcinoma, Mucinous Carcinoma
# ER status: Positive/Negative
# PR status: Positive/Negative
# HER2 status: Positive/Negative
# Surgery_type: Lumpectomy, Simple Mastectomy, Modified Radical Mastectomy, Other
# Date_of_Surgery: Date on which surgery was performed (in DD-MON-YY)
# Date_of_Last_Visit: Date of last visit (in DD-MON-YY)
# [can be null, in case the patient didn’t visit again after the surgery]
# Patient_Status: Alive/Dead [can be null, in case the patient didn’t visit again after the surgery and
# there is no information available whether the patient is alive or dead].


######################################################
# AB Testing
######################################################
# 1. Build hypotheses
# 2. Assumption check
# - 1. Normality assumption
# - 2. Variance homogeneity
# 3. Implementation of the hypothesis
# - 1. Independent two-sample t-test (parametric test) if assumptions are provided.
# - 2. Mannwhitneyu test if assumptions are not provided (non-parametric test)
# 4. Interpret results based on p-value
# Note:
# - Direct number 2 if normality is not achieved. If the assumption is not homogeneous,
# an argument is entered at number 1.
# - It may be useful to perform outlier analysis and correction before examining normality


# Is there a statistically significant difference between the mean age of patients who lived and did not survive after the surgery?
df.groupby("Patient_Status").agg({"Age": "mean"})
#                     Age
# Patient_Status
# Alive          58.80392
# Dead           58.40323

# 1. Build hypotheses
# H0: M1 = M2 there is no statistically significant difference between living and non-living.
# H1: M1 != M2 there is a significant difference.

# 2. Assumption check
# - H0: Normal distribution assumption is provided.
# - H1: ... is not provided.

test_stat, pvalue = shapiro(df.loc[df["Patient_Status"] == "Alive", "Age"])
print("Test Stat = %.4f, p-value = %.4f" %(test_stat, pvalue))
# Test Stat = 0.9785, p-value = 0.0007, p-value is lower than 0.05 so H0 hypothesis is rejected.
# The assumption of normality is not provided.

test_stat, pvalue = shapiro(df.loc[df["Patient_Status"] == "Dead", "Age"])
print("Test Stat = %.4f, p-value = %.4f" %(test_stat, pvalue))
# Test Stat = 0.9887, p-value = 0.8382 p-value is higher than 0.05 so H0 hypothesis is rejected.


# We should use a non-parametric test because normality is not ensured.

# Variance Homogeneity Assumption

# -H0: Variances are homogeneous.
# -H1: Variances are not homogeneous.
test_stat, pvalue = levene(df.loc[df["Patient_Status"] == "Alive", "Age"],
                           df.loc[df["Patient_Status"] == "Dead", "Age"])
print("Test Stat = %.4f, p-value = %.4f" %(test_stat, pvalue))
# Test Stat = 0.0277, p-value = 0.8680 (p-value is higher than 0.05 so, H0 cannot be rejected.
# That is, the variances are homogeneous.)

# 3. Implementation of the hypothesis
# - 1. Independent two-sample t-test (parametric test) if assumptions are provided.
# - 2. Mannwhitneyu test if assumptions are not provided (non-parametric test)

test_stat, pvalue = mannwhitneyu(df.loc[df["Patient_Status"] == "Alive", "Age"],
                                 df.loc[df["Patient_Status"] == "Dead", "Age"])
print("Test Stat = %.4f, p_value = %.4f" % (test_stat, pvalue))
# Test Stat = 7909.5000, p_value = 0.9951
# 4. Interpret results based on p-value
# p-value is higher than 0.05 so, H0 cannot be rejected.
# There is no statistically significant difference between living and non-living.


####################################################################################################
# ANOVA (Analysis of Variance): It is used to compare the mean of more than two groups.
####################################################################################################

# Is there a statistically significant difference between the mean age of the patients and the stage of their cancer?
df.groupby("Tumour_Stage").agg({"Age": "mean"})
#                   Age
# Tumour_Stage
# I            61.81667
# II           58.80000
# III          56.14286


# 1. Build hypotheses
# H0: m1 = m2 = m3, There is no significant difference between group averages.
# H1: ..., There is a significant difference between group averages.

# 2. Assumption check
# Assumption of normality
# Assumption of homogeneity of variance

# One way anova if the assumption is provided
# Kruskal if the assumption is not provided

##########################################################
# Assumption of normality
# H0: The assumption of normal distribution is provided.
# H1: The assumption of normal distribution is not provided.
##########################################################

# We have converted the classes of a categorical variable into an object to visit.

for group in list(df["Tumour_Stage"].unique()):
    pvalue = shapiro(df.loc[df["Tumour_Stage"] == group, "Age"])[1] # [1] because we want the p-value (test-stat[0], pvalue[1]
    print(group, "p-value: %.4f" %pvalue)

# III p-value: 0.0086
# II p-value: 0.0358
# I p-value: 0.6106
# According to these values, H0 is rejected because III and II pvalues are less than <0.05.
# So it is not a normal distribution.

##########################################################
# Assumption of homogeneity of variance
# H0: variance homogeneity assumption is provided.
# H1: the assumption of homogeneity of variance is not provided.
##########################################################

test_stat, pvalue = levene(df.loc[df["Tumour_Stage"] == "III", "Age"],
                           df.loc[df["Tumour_Stage"] == "II", "Age"],
                           df.loc[df["Tumour_Stage"] == "I", "Age"])

print("Test State: %.4f, pvalue: %.4f" %(test_stat, pvalue))
# Test State: 0.9313, pvalue: 0.3951
# p-value higher than 0.05. So, H0 cannot be rejected. It provides variance homogeneity.
# But we already rejected the first assumption, so we will use non-parametric test.

# 3. Implementation of the hypothesis
# One way anova test if the assumption is provided.
# Kruskal test if the assumption is not provided.
kruskal(df.loc[df["Tumour_Stage"] == "III", "Age"],
        df.loc[df["Tumour_Stage"] == "II", "Age"],
        df.loc[df["Tumour_Stage"] == "I", "Age"])

# KruskalResult(statistic=7.51013119723737, pvalue=0.023398915622321548)
# H0 is rejected because it has a p value less than 0.05. That is, there is a significant difference between the groups.


################################################################
# There is a difference, but which group is causing it?
################################################################

from statsmodels.stats.multicomp import MultiComparison
comparison = MultiComparison(pd.to_numeric(df['Age'], errors='coerce'), df['Tumour_Stage'])
tukey = comparison.tukeyhsd(0.05)
print(tukey.summary())

# Multiple Comparison of Means - Tukey HSD, FWER=0.05
# =====================================================
# group1 group2 meandiff p-adj   lower    upper  reject
# -----------------------------------------------------
#      I     II  -3.0167 0.2517  -7.4865  1.4531  False
#      I    III  -5.6738 0.0272 -10.8372 -0.5104   True
#     II    III  -2.6571 0.2771  -6.7401  1.4259  False
# -----------------------------------------------------






