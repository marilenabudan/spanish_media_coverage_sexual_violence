# ARTICLES ANALYSIS
This directory contains the Python notebook where the articles analysis has been conducted, and the resources required. 

Articles analysis focuses on two types of analysis: 
1. **Coverage analysis**: Assessment of the coverage of sexual violence articles focusing on three different aspects: type of sexual violence, victim-perpetrator bond and place where the crime occurred.
2. **Content analysis**: Evaluation of the type of information provided in news articles, centering the analysis in three main categories: case-related information, stigmatized information and expression.

Both analysis have been based on the presence of terms and regular expressions characteristics of the attributes studied; we also studied the most significant association rules for the obtention of insights.

## Notebook description
### articles_analysis.ipynb
* **Customizable global variables**:
  * `NEWS_PATH`: Path to the directory containing news in XML format.
  * `INPUT_FILE_PATH`: Path to `cases_info.csv`, the CSV file outputed in the previous part of the project (Cases classification) mapping each tweet id with its cluster. 

* **Additional requirements**:
  * A Python file containing a dictionary with the regular expressions stored in categories. This file can be found in [utilities/regex_categories.py]().
  * A txt file containing a list of nationalities in Spanish. This file can be found in [utilities/nacionalidades.txt]()

The notebook is self-explanatory and contains prints the results without storing them in any file-
