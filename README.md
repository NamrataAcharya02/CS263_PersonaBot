# CS263_PersonaBot
## Annotation guidelines:

This folder contains the guidelines for the 3 evaluation metrics used: coherence, compassion, correctness. Each guideline contains guiding information and instructions for annotating the generated conversations. 
## table_gen:
This folder contains code to facilitate converting the json files of chatbot conversations into CSV files with the desired format. The generated CSV files are in the folder `CSV_files`. 
To use this, please edit the settings.yml in `./table_gen/` and change the input json and output csv names. Make sure you include the extension at the end. 
Then, just run the jsonParser with `python jsonParser.py`. Note that you should probably run it from inside the table-gen directory.

## mbti-scorer:
`questionMapping.csv` contains questions and their corresponding personality aspect number (`p_i`) and coefficient (`C`). `questionMapping.py` reads this and turns it into a dictionary where the keys are the questions and the values are a list of the p_i and C corresponding to that question.

We made a facsimile of the MBTI personality scoring system. 
There are 4 scales on which we score: Introversion/Extroversion, Intuition/Sensing, Thinking/ Feeling, and Judging/Prospecting.  They are appropriate numbered as personality aspects: so for example Introversion/ Extroversion has a `p_i` of 1, Intuition/ Sensing has a `p_i` of 2 and so on until 4.

We maintain thus an array of the corresponding values of these entries. Based on the responses that someone gives to the questions posed (abstracted as 1-7), we calculate the corresponding sum of values for each of their personality aspects as follows:

for each question with index j:
    p_i += C_j * (a_j - 4)

if p_1 <0 then introverted, if >0 then extroverted
if p_2 <0 then intuitive if >0 then sensing
if p_3 <0 then thinking, if >0 then feeling
if p_4 <0 then judging, if >0 then prospecting

`scorer.py` takes a json file representing the responses of a chatbot to the questions posed in questionMapping, and scores it according to the above criteria. It will then at the end print out the letters corresponding to the personality type

##Kappa.py

This file calculates Cohen's Kappa to measure inter annotater agreement for 2 different pairs of annotators. 

##Metrics_calculator.py

This file automatically calculates coherence, compassion and correctness averages for each annotated file. 