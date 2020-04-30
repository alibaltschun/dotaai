from collections import Counter
import pandas as pd

df = pd.read_csv("./hero.csv")


def summary_countered(heros, df=df):
    bad_against = []
    df = df.loc[df['Hero'].isin(heros)]
    
    for row in df['Bad against']:
        str1 = row.replace(']','').replace('[','').replace(" '","").replace("'","").replace(" I","I")
        [bad_against.append(i) for i in str1.replace('"','').split(",") if i != ""]
    
    max_countered = max(list(Counter(bad_against).values()))
    summary_countered = [ [i, []] for i in range(1, max_countered)]
    
    for i in range(len(Counter(bad_against).keys())):
        total_countred = list(Counter(bad_against).values())[i]
        if total_countred > 1:
            summary_countered[total_countred-2][1].append(
                str(list(Counter(bad_against).keys())[i]))

    return dict(summary_countered)

    
def summary_attack_abilities(heros, df=df):
    attack_type = []
    attack_demage = []
    summary_attack = []
    summary_demage = []
    
    df = df.loc[df['Hero'].isin(heros)]
    
    for row in df['Abilities attack type']:
        str1 = row.replace(']','').replace('[','').replace(" '","").replace("'","")
        [attack_type.append(i) for i in str1.replace('"','').split(",") if i != ""]
    
    for row in df['Abilities attack demage']:
        str1 = row.replace(']','').replace('[','').replace(" '","").replace("'","").replace(" I","I")
        [attack_demage.append(i) for i in str1.replace('"','').split(",") if i != ""]
    
    summary_attack = [
        list(Counter(attack_type).keys()),
        list(Counter(attack_type).values())
        ]

    summary_demage = [
        list(Counter(attack_demage).keys()),
        list(Counter(attack_demage).values())]
    
    return summary_attack, summary_demage
