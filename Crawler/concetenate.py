# -*- coding: utf-8 -*-

import pandas as pd

import os

BASE = (os.path.dirname(os.path.realpath(__file__)))

hero_counter = pd.read_csv(BASE + "/hero_counters.csv")
hero_abilities = pd.read_csv(BASE + "/hero_abilities.csv")
hero_atribute = pd.read_csv(BASE + "/atribut.tsv", sep="\t")

hero = hero_counter.merge(hero_atribute, on="Hero", how = 'inner')
hero = hero.merge(hero_abilities, on="Hero", how = 'inner')
hero.to_csv(BASE + "/../App/assets/csv/hero.csv", index=False)