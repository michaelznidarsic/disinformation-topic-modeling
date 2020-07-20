# Topic Modeling of Russian Disinformation on Twitter. 


This data was obtained at https://transparency.twitter.com/en/information-operations.html. The "Tweet Information" was pulled from the Russian Bot dumps of May 2020, June 2019, and January 2019. These contain tweets going back as far as the early 2010s.

Latent Dirichlet Allocation models were run to approximate the topical foci of all Russian Bot tweets disclosed officially by Twitter. This algorithm attempts to explain similarity in word choice between the Tweets by separating them into a predetermined number of groups, or "topics". Separate models were run for tweets made by the Bot accounts and retweets made by those accounts. Words were stemmed using the Snowball Porter Stemmer. For example, the words "consoling" and "consolingly" both become "consol". Although it may lead to confusion when reading the most important words for each topic, this process was done to consolidate words for nearly identical conceptual meanings into a single token. 

Data cleaning and modelling was done in Python. The outcome of the models is visualized in interactive HTML files generated using the PyLDAvis Python package. Below is an example of a topic visualized in the HTML files. 

![alt text](https://github.com/michaelznidarsic/disinformation-topic-modeling/blob/master/LDAtopicvizsample.png?raw=true)

