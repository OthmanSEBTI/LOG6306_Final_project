import pandas as pd
import os
import re

file_list = os.listdir('/mnt/c/Users/Othman/Desktop/TP-LOG6306/Final_project/Data_collection')

all_commits = pd.DataFrame()

for file in file_list[:len(file_list)-1]:
    commits = pd.read_csv('/mnt/c/Users/Othman/Desktop/TP-LOG6306/Final_project/Data_collection/'+ file)
    all_commits = pd.concat([all_commits,commits])

all_commits.to_csv('/mnt/c/Users/Othman/Desktop/TP-LOG6306/Final_project/Data_collection/all_commits.csv')