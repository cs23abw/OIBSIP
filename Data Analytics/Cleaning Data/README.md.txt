# Cleaning Data

## Project Overview

This project was completed as part of the Oasis Infobyte Data Analytics Internship.

The objective of this task is to clean a dataset by identifying and handling common data quality issues such as missing values, duplicate records, inconsistent formatting, incorrect data types, and outliers.

The dataset used for this project is the New York City Airbnb Open Data dataset.

## Dataset

The original dataset was stored in the `raw data` folder before cleaning.

The cleaned dataset was saved in the `Cleaned data` folder as:

```text
cleaned_airbnb_data.csv
```

## Tools Used

* Python
* Jupyter Notebook
* Pandas
* Matplotlib

## Cleaning Steps Performed

The following steps were completed in the notebook:

1. Loaded the dataset using Pandas.
2. Previewed the first rows of the dataset.
3. Checked the dataset shape.
4. Checked column names and data types.
5. Identified missing values.
6. Checked for duplicate rows.
7. Created a copy of the original dataset before cleaning.
8. Standardized column names.
9. Filled missing listing names with `Unknown Listing`.
10. Filled missing host names with `Unknown Host`.
11. Filled missing `reviews_per_month` values with `0`.
12. Converted `last_review` into a proper date format.
13. Removed duplicate records.
14. Removed invalid records where `price` was `0`.
15. Checked price outliers using summary statistics and a boxplot.
16. Removed extreme price outliers above the 99th percentile.
17. Saved the cleaned dataset as a new CSV file.

## Missing Values Handling

The dataset contained missing values in columns such as:

* `name`
* `host_name`
* `last_review`
* `reviews_per_month`

The missing `name` values were replaced with:

```text
Unknown Listing
```

The missing `host_name` values were replaced with:

```text
Unknown Host
```

The missing `reviews_per_month` values were replaced with:

```text
0
```

The missing `last_review` values were kept because they likely represent listings that had not received a review yet.

## Duplicate Records

Duplicate rows were checked using Pandas. This helped confirm whether the dataset contained repeated records that could affect the accuracy of analysis.

## Outlier Detection

The `price` column was checked for unusual values.

A boxplot was created to visually identify extreme price values. Some listings had very high prices compared to most of the dataset.

To reduce the effect of extreme outliers, listings above the 99th percentile price value were removed.

## Files Included

```text
Cleaning Data/
├── data_cleaning.ipynb
├── README.md
├── raw data/
├── Cleaned data/
│   └── cleaned_airbnb_data.csv
└── Screenshots/
```

## What I Learned

Through this project, I learned how to:

* Load a CSV file into Python using Pandas
* Inspect the structure of a dataset
* Check column names and data types
* Identify missing values
* Handle missing data appropriately
* Check for duplicate rows
* Convert text-based date columns into date format
* Detect invalid values
* Identify outliers using summary statistics and visualization
* Save a cleaned dataset as a new CSV file
* Document a data cleaning process clearly

## Conclusion

The dataset was successfully cleaned by handling missing values, checking duplicates, converting date values, removing invalid prices, detecting outliers, and saving a cleaned version of the dataset.

This task improved my understanding of data quality and showed how proper cleaning helps make analysis more accurate and reliable.

## Author

Chukwukaima Sam
