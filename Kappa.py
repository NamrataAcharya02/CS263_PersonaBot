import csv
import pandas as pd
import os
from sklearn.metrics import cohen_kappa_score

ann1 = "K/"
ann2 = "N/"

coherence_K = []
coherence_N = []
compassion_K = []
compassion_N = []
completness_K = []
completness_N = []

K_files = sorted(os.listdir(ann1))
N_files = sorted(os.listdir(ann2))

print(K_files == N_files)

for name in K_files:
    if name.endswith(".csv"):
        filename = ann1 + name
        df = pd.read_csv(filename)
        if df.isnull().values.any():
            print(filename)
            break
        coh = list(df['coherence_score'])
        coherence_K.extend(coh)
        compassion_K.extend(list(df['compassion_score']))
        completness_K.extend(list(df['correctness']))

for name in N_files:
    if name.endswith(".csv"):
        filename = ann2 + name
        df = pd.read_csv(filename)
        if df.isnull().values.any():
            print(filename)
            break
        coh = list(df['coherence_score'])
        coherence_N.extend(coh)
        compassion_N.extend(list(df['compassion_score']))
        completness_N.extend(list(df['correctness']))

print(len(coherence_K), len(coherence_N))
print(len(compassion_K), len(compassion_N))
print(len(completness_K), len(completness_N))

df = pd.DataFrame({'complete_K': completness_K, 'complete_N': completness_N})
df.to_csv('completeness.csv', index=False)
print(df['complete_K'].value_counts())
print(df['complete_N'].value_counts())

df['same'] = df['complete_K'] == df['complete_N']
print(df['same'].value_counts())

alag = df[df['same'] == False]
print(alag)
print(alag['complete_K'].value_counts())



sam = df[df['same'] == True]
print(sam)
print(sam['complete_K'].value_counts())
#kappa_coh = cohen_kappa_score(coherence_K, coherence_N, weights='linear')
#kappa_com = cohen_kappa_score(compassion_K, compassion_N, weights='linear')
kappa_compl = cohen_kappa_score(completness_K, completness_N, weights='linear')
#print("KN", kappa_coh, kappa_com, kappa_compl)
print(kappa_compl)
rater1 = [0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0]
rater2 = [0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0]

#calculate Cohen's Kappa
c = cohen_kappa_score(rater1, rater2)
print(c)

ann1 = "A/"
ann2 = "J/"

coherence_K = []
coherence_N = []
compassion_K = []
compassion_N = []
completness_K = []
completness_N = []

A_files = sorted(os.listdir(ann1))
J_files = sorted(os.listdir(ann2))
for name in A_files:
    if name.endswith(".csv"):
        filename = ann1 + name
        print(name)
        df = pd.read_csv(filename)
        if df.isnull().values.any():
            print(filename)
            break
        coh = list(df['coherence_score'])
        coherence_K.extend(coh)
        compassion_K.extend(list(df['compassion_score']))
        completness_K.extend(list(df['correctness']))

for name in J_files:
    if name.endswith(".csv"):
        filename = ann2 + name
        df = pd.read_csv(filename)
        if df.isnull().values.any():
            print(filename)
            break
        coh = list(df['coherence_score'])
        coherence_N.extend(coh)
        compassion_N.extend(list(df['compassion_score']))
        completness_N.extend(list(df['correctness']))

print(len(coherence_K), len(coherence_N))
print(len(compassion_K), len(compassion_N))
print(len(completness_K), len(completness_N))


df = pd.DataFrame({'complete_K': completness_K, 'complete_N': completness_N})
df.to_csv('correctness.csv', index=False)
print(df['complete_K'].value_counts())
print(df['complete_N'].value_counts())

df['same'] = df['complete_K'] == df['complete_N']
print(df['same'].value_counts())

alag = df[df['same'] == False]
print(alag)
print(alag['complete_K'].value_counts())



sam = df[df['same'] == True]
print(sam)
print(sam['complete_K'].value_counts())
kappa_coh = cohen_kappa_score(coherence_K, coherence_N, weights='linear')
kappa_com = cohen_kappa_score(compassion_K, compassion_N, weights='linear')
kappa_compl = cohen_kappa_score(completness_K, completness_N, weights='linear')
print("AJ", kappa_coh, kappa_com, kappa_compl)