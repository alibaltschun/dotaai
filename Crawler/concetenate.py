# -*- coding: utf-8 -*-

import pandas as pd

hero_counter = pd.read_csv("./hero_counters.csv")
hero_atribute = pd.read_csv("./atribut.tsv", sep="\t")

hero = hero_counter.merge(hero_atribute, on="Hero", how = 'inner')
hero.to_csv("./hero.csv", index=False)