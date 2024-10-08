It is a regression problem aimed at predicting home prices based on 81 features. I did not rely heavily on visualization plots, as they are less suitable for such a large number of features. Instead, I focused on automating the process through code. My primary emphasis was on the preprocessing steps, as the dataset contained several issues that needed to be addressed. After completing the preprocessing and modeling, I tested the code on the competition's test data and achieved a score of 0.212 in the Kaggle competition.

### Link of Dataset:
[Click here](https://www.kaggle.com/c/house-prices-advanced-regression-techniques/data)
### Data Pre-processing:
 
1- Handling Null Values

2- Dropping Features which have more than 80% of values with the same value

3- removing highly correlated features to avoid multi-collinearity as much as we can

4- removing/clamping outliers

5- transforming highly skewed data to reduce their skewness

6- checking for each features whether it follows a normal distribution or not using Shapiro wilk test to decide whether to standardize or min-max scale)

7- classify your categorical features into (ordinal and nominal) to decide which features will be label encoded and which features should be OHE

8- check Multicollinearity and drop feature has high Multicollinearity with other features using VIF(variance inflation factor) 

9- measure the significance level of each feature and perform subset selection using the backward-stepwise method
