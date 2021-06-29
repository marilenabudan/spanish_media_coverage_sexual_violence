# DATA
This directory contains a zip file—`data.zip`—containing the data collection of tweets and news articles obtained in the first phase of the project: [Dastaset creation](https://github.com/marilenabudan/spanish_media_coverage_sexual_violence/tree/main/dataset_creation). The zip file contains:

- `tweets`: a directory containing 10 sub-directories; each of them contains:
  * 15 CSV files, one per each media outlet considered, with 1.000 tweets.
  * `__Interval.csv` file: containing information about the date interval of the tweets collected
  * `extended_json`: a directory containing 15 JSON files with the extended version of the tweets stored in CSV files.
  * `Classified`: a directory containing the same 15 CSV files with the a new column specifying whether each tweet is about sexual violence. 

- `news`: a directory cotaining 10 sub-directories; each of them contains the news articles extracted from their corresponding directory in `tweets`. News are stored in XML format, following NewsML-G2 standards.

- `cases_labeled.csv`: a CSV file containing tweets labeled according to their case. 

- `cases_pairwise_proba.csv`, `cases_info.csv`, and `cases_ids.csv`: outputs generated in the second phase of the project [Cases classification](https://github.com/marilenabudan/spanish_media_coverage_sexual_violence/tree/main/cases_classification).


<br>The zip file is protected with a password that can be obtained by requesting it through email to `marilena.budan01@estudiant.upf.edu`. 
