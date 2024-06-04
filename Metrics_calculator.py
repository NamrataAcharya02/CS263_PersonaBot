import csv
import pandas as pd


folder = "Prompt2"
path = "Others/" + folder + "/"
scenarios = ["Adventure_trip_", "FeelingSad_", "Career_advice_", "Romantic_"]
persona = ["ESFP_", "INTJ_"]
fieldnames = ['turn', 'prompt', 'response', 'compassion_score', 'coherence_score', 'correctness']

for i in range(2, 4):
    for j in range(0, 2):
        for k in range(1, 3):
            for l in range(0, 2):
                filename = path + scenarios[i] + persona[j] +  "prompt2_" + str(k) + ".csv"

                if l == 1:
                    filename = path + scenarios[i] + persona[j] + "prompt2_" + str(k) + " (1).csv"

                df = pd.read_csv(filename)
                #print(df)

                coherence = sum(df['coherence_score'] * df['turn']) / sum(df['turn'])
                print(coherence)

                compassion = sum(df['compassion_score'])/len(df['compassion_score'])
                correctness = sum(df['correctness'])/len(df['correctness'])

                output = folder + "_scores.csv"
                fields = ['scenario', 'persona', 'coherence', 'compassion', 'correctness']

                with open(output,'a') as csvFile:
                    writer = csv.DictWriter(csvFile,fieldnames=fields)
                    #if i == 0 and j == 0 and k == 1:
                        #writer.writeheader()
                    writer.writerow({'scenario':scenarios[i], "persona": persona[j], 'coherence':coherence,'compassion':compassion,'correctness':correctness})
