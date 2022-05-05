# ANALYSIS OF ONLINE NEWS ARTICLES: The coverage of sexual violence in Spanish Media

---

**Marilena Budan** - Mathematical engineering in Data Science at UPF. <br>
**Project director: Carlos Castillo**

---

This repository contains the code and resources used for the development of my end of degree project, in which I studied the coverage of sexual violence in Spanish Media.

>More than 10% of women in Spain have suffered from sexual violence instances at least once in their lives. Nevertheless, there are huge prejudices and stigma in society regarding this type of offences, which influence victim’s decision when it comes to reporting the crime. The present study analyses news articles, from the most popular media outlets in Spain, to get insights on the coverage of sexual violence, with a focus on the perpetration of harmful preconceptions and myths surrounding sexual violence by means of supervised classification and NLP techniques. The study finds that media outlets over-represent extreme cases of sexual violence, meaning those that satisfy the preconceptions’ requirements, to maximize their profit instead of providing a fair portrayal of the reality keeping stigmas alive. This paper will look into sexual violence coverage, by first creating a dataset with news articles related to the sexual violent crimes, then putting them into clusters according to the cases they represent; the cases’ main characteristics are then extracted in order to finally compare them with official statistics and social prejudices.


## Data and code release
The project consists on three main phases, which correspond with the directories of the present repository: 
1. **[Dataset creation](https://github.com/marilenabudan/spanish_media_coverage_sexual_violence/tree/main/dataset_creation)**: The analysis has been conducted on the basis of the dataset created in this first phase. The dataset consist on a collection of news articles about sexual violence, published by the top-15 online media outlets in Spain. For the obtention of this dataset, we collected tweets from the official accounts of the said media outlets, classified them depending on their topic (sexaul violence or not) and we downloaded tweets' corresponding news articles.<br>
   * [Code and resources](https://github.com/marilenabudan/spanish_media_coverage_sexual_violence/tree/main/dataset_creation) 
   * [Resulting dataset](https://github.com/marilenabudan/spanish_media_coverage_sexual_violence/tree/main/data)


2. **[Cases classification](https://github.com/marilenabudan/spanish_media_coverage_sexual_violence/tree/main/cases_classification)**: News articles were grouped according to the sexual violence case they share information about. The clustering was done in two steps: first, we computed the similarity of each pair of cases; next, we clustered articles based on this similarity. 
   * [Code and resources](https://github.com/marilenabudan/spanish_media_coverage_sexual_violence/tree/main/cases_classification)
   * [Results](https://github.com/marilenabudan/spanish_media_coverage_sexual_violence/tree/main/data)


3. **[Articles analysis](https://github.com/marilenabudan/spanish_media_coverage_sexual_violence/tree/main/articles_analysis)**: Articles were analyzed from two points of view: the coverage of sexual violence, infering cases' characteristics and studying their correspondence with official statistics; and the analysis of the information provided in articles, focusing on the presence of distinct information, and the perpetration of stereotypes and misconceptions about sexual violence.
   * [Code and resources](https://github.com/marilenabudan/spanish_media_coverage_sexual_violence/tree/main/articles_analysis)
   * Results are included in code (Python notebook). 
   


## Report 
A detailed report (in PDF format) is included in this repository and can be downloaded [here](https://github.com/marilenabudan/spanish_media_coverage_sexual_violence/blob/main/report.pdf).

