# Hypothesis-Testing

![image](https://user-images.githubusercontent.com/64617036/229249227-e76faea1-0364-4129-a727-aa2d20c3696a.png)

## About Dataset

This dataset consists of a group of breast cancer patients, who had surgery to remove their tumour. The dataset consists of the following variables:

* Patient_ID: unique identifier id of a patient
* Age: age at diagnosis (Years)
* Gender: Male/Female
* Protein1, Protein2, Protein3, Protein4: expression levels (undefined units)
* Tumour_Stage: I, II, III
* Histology: Infiltrating Ductal Carcinoma, Infiltrating Lobular Carcinoma, Mucinous Carcinoma
* ER status: Positive/Negative
* PR status: Positive/Negative
* HER2 status: Positive/Negative
* Surgery_type: Lumpectomy, Simple Mastectomy, Modified Radical Mastectomy, Other
* Date_of_Surgery: Date on which surgery was performed (in DD-MON-YY)
* Date_of_Last_Visit: Date of last visit (in DD-MON-YY) can be null, in case the patient didn’t visit again after the surgery]
* Patient_Status: Alive/Dead can be null, in case the patient didn’t visit again after the surgery and there is no information available whether the patient is alive or dead.

## Hypothesis Testing
Statistical methods used to test a hypothesis or an argument. It is to test whether the resulting difference is by chance. We make scientific decisions by using data to support a business decision. Either the means for the two groups or the ratios for the two groups are compared. Two things with the same property can be compared.

Example: Has the average daily time spent by users in the application increased after the interface change in the mobile application?

  Group 1: Users before the interface change Group A
  Group 2: Users after the interface change Group B 

  Hypothesis 0: There is no time difference between group A and group B. (tested) 
  Hypothesis 1: There is a difference between group A and group B. 
Let's say that the time has increased as a result of the change, but it still needs to be tested because we take a sample and we see it like this in every sample.

![image](https://user-images.githubusercontent.com/64617036/229249365-00cec37b-1ba8-4079-b2d3-fbe0e2d17382.png)

H0: It is the null hypothesis. The situation we are going to test is in the H0 hypothesis. There is no difference between the two groups. We can evaluate whether there is a difference between the two groups according to the H0 rejection or no rejection status.

## Hypothesis Testing Steps
1. Build hypotheses

2. Assumption check

2.1. Normality assumption: The distribution of the relevant groups is normal. (The mean of the samples must be in accordance with the normal distribution). Again, we have to test the hypothesis. Shapiro tests whether the distribution of a variable is normal.

2.2. Variance homogeneity: The distribution of the variances of the two groups is similar to each other: Levene performs the control of variance homogeneity test.

3. Implementation of the hypothesis

3.1. Independent two-sample t-test (parametric test) if assumptions are provided.

3.2. Mannwhitneyu test if assumptions are not provided (non-parametric test)

4. Interpret results based on p-value Note:

Direct number 2 if normality is not achieved. If the assumption is not homogeneous, an argument is entered at number 1.
It may be useful to perform outlier analysis and correction before examining normality

## ANOVA (Analysis of Variance)
It is used to compare the mean of more than two groups. When comparing these groups, at least one of them is compared as different. Why do we compare all of them at once and not one by one? Because error evaluation processes will not be healthy as a result of the evaluation of all of them one by one and the result of one comparison.

## ANOVA Testing Steps
1. Build hypotheses

H0: M1 = M2 = M3 = … There is no significant difference between group means.
H1: … there is a difference.
2. Assumption check

2.1. Normality assumption: The distribution of the relevant groups is normal. (The mean of the samples must be in accordance with the normal distribution). Again, we have to test the hypothesis. Shapiro tests whether the distribution of a variable is normal.

2.2. Variance homogeneity: The distribution of the variances of the two groups is similar to each other: Levene performs the control of variance homogeneity test.

3. Implementation of the hypothesis

3.1. One way anova test if the assumption is provided.

3.2. Kruskal test if the assumption is not provided.

4. Interpret results based on p-value





