# Topic Modeling of Russian Disinformation on Twitter. 


This data was obtained at https://transparency.twitter.com/en/information-operations.html. The "Tweet Information" was pulled from the Russian Bot dumps of May 2020, June 2019, and January 2019.

Latent Dirichlet Allocation models were run to approximate the topical foci of all Russian Bot tweets disclosed officially by Twitter. Separate models were run for tweets made by the Bot accounts and retweets made by those accounts. 

Data cleaning and modelling was done in Python. The outcome of the models is visualized in interactive HTML files generated using the PyLDAvis Python package. Below is an example of a topic visualized in the HTML files.

![alt text](https://github.com/michaelznidarsic/disinformation-topic-modeling/blob/master/LDAtopicvizsample.png?raw=true)



