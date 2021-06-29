# DATASET CREATION
This directory contains the Python code and resoruces used for the creation of a dataset containing news articles from the top-15 most read Spanish media outlets, determined by the [Reuters Institute](https://reutersinstitute.politics.ox.ac.uk/sites/default/files/2020-06/DNR_2020_FINAL.pdf). 

The process consists on four phases: 
1. Obtention of tweets
2. Hydration of tweets obtained in phase 1 
3. Classification of tweets according to their relationship with sexual violence
4. Obtention of news articles corresponding to tweets deemed to describe sexual violence

Each phase has been executed in a separate Python code file to create the dataset attached in the section `data` of the present repository. 

## Code description

### 1. `tweets_scraping.py`
   
Obtention of a summarized version of the last 10,000 (`NUM_DIRS`x`NUM_TWEETS`) tweets from medias Twitter accounts timelines.
* **Customizable global variables**:
    * `ACCOUNTS`: List with Twitter accounts to be considered
    * `DATA_PATH`: Path where to store the output
    * `NUM_DIRS`: Number of times to collect `MAX_TWEETS` = number of output directories
    * `MAX_TWEETS`: Number of tweets to collect for each account
* **Input arguments**: None
* **Output**: `NUM_DIRS` directories containing a CSV file for each Twitter account in `ACCOUNTS` containing main information about `MAX_TWEETS` tweets.
    
### 2. `tweets_hydration.py`
   
Hydration of tweets obtained in the first phase.
* **Customizable global variables**:
    * `DATA_PATH`: Path to a directory with the output from `tweets_scraping.py`
    * `ACCOUNTS`: List with Twitter accounts considered.
    * `TO_AVOID`: List with files that may be in `DATA_PATH` that need to be ignored.
* **Input arguments**: None
* **Additional requirements**:
    * Access to a Twitter developed account. Insert credentials in file `utilities/config.ini` 
* **Output**: JSON files containing the extended version of the tweets. 


### 3. `tweets_classification.py`
Training and classification of a logistic regression model that assign class `1` to tweets deemed to describe sexual violence, and `0` if they do not containing sexual violence-related information.
* **Input arguments**:
  * `-data`: Path to the data directory
  * `-train`: List of directories contained in `-data` with CSV files with tweets labeled. 
  * `-predict`: List of directories contained in `-data` with CSV files with tweets to be labeled.
  
  All arguments are required. 
* **Output**: Creates a directory called `Classified` in each directory inputed in `-predict` with predictions' outputs.

### 4. `download_news.py`
Obtain source articles from tweets about sexual violence by following the URL attached in the tweets. 
* **Customizable global variables**:
  * `GOOGLE_CHROMEDRIVER_PATH`: Path to a downloaded chrome driver. Availabel at: `utilities/ChromeDriver/chromedriver_google`
  * `TWEETS_PATH`: Path to the storage of tweets
  * `NEWS_PATH`: Destination path
* **Input arguments**:
  * `-directories` or `-dir`: Directories containing CSV files with classified tweets inside `TWEETS_PATH
  * `-media`: Media accounts to be considered.
  
  If none of them are specified, all directories and media accounts will be considered.

* **Output**: Stores XML files containing news articles in `NEWS_PATH` following the same structure as `TWEETS_PATH`.
