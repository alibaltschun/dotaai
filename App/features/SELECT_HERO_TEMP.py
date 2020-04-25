from collections import Counter
import pandas as pd

df = pd.read_csv("./hero.csv")

radiant = ['Bristleback','Sniper','Lion','Warlock','Pudge']
hero_data = df.loc[df['Hero'].isin(radiant)]

df = hero_data

def __get_summary_attack_abilities__(df):
    attack_type = []
    attack_demage = []
    bad_against = []
    
    for row in df['Abilities attack type']:
        str1 = row.replace(']','').replace('[','').replace(" '","").replace("'","")
        [attack_type.append(i) for i in str1.replace('"','').split(",") if i != ""]
    
    for row in df['Abilities attack demage']:
        str1 = row.replace(']','').replace('[','').replace(" '","").replace("'","").replace(" I","I")
        [attack_demage.append(i) for i in str1.replace('"','').split(",") if i != ""]
    
    for row in df['Bad against']:
        str1 = row.replace(']','').replace('[','').replace(" '","").replace("'","").replace(" I","I")
        [bad_against.append(i) for i in str1.replace('"','').split(",") if i != ""]
        
    
    Counter(attack_type).keys()
    Counter(attack_type).values()
    
    Counter(attack_demage).keys()
    Counter(attack_demage).values()

    Counter(bad_against).keys()
    Counter(bad_against).values()