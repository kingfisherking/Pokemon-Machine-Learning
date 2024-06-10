#import modules
#load csv > dataframe
#separate into features and data
#train GAN
#create function to automatically produce 1 new pokemon or a list of "n" new pokemon


import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sklearn.model_selection as sk
import os
from keras import layers
import time
from IPython import display

pokedex = pd.read_csv("pokedex.csv", names=["Pokedex No.", "Name", 
                                            "Type", "Total", "HP", 
                                            "Attack", "Defense", 
                                            "Special Attack", "Special Defense", "Speed"])

pokedex_features = pokedex.copy()
pokedex_labels = pokedex_features.pop("Pokedex No.") #splitting data into labels and features

#labels will be used to predict new features
#ideally, predict new features by predicting X + length of pokedex (new pokedex entries)
pokeX_train, pokeX_test, pokeY_train, pokeY_test = sk.train_test_split(pokedex_features, 
                                                                       pokedex_labels, 
                                                                       test_size=0.2, 
                                                                       random_state=23)

#Normalize types by splitting it into 1 of 18 , perhaps a tuple for dual types
#what I'm thinking is, use keras multihot category encoding
#have to make a function that checks the type to a dict of types
#if it has dual typing, split using '/' as delimiter
#normalize into list with number 1-18 then encode

#I guess all stats can be minmax normalized, but I'm also thinking standardized
#apparently, standardization works better for normal distributions, which I think pokemon stats are