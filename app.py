# -*- coding: utf-8 -*-
"""
Created on Thu Jun 19 14:10:42 2025

@author: dkglt
"""

import streamlit as st
import pickle
import pandas as pd

import pickle

df = pickle.load(open(r'D:\datasets\movies\movies.pkl', 'rb'))
similarity = pickle.load(open(r'D:\datasets\movies\similarity.pkl', 'rb'))

def recommend(movie):
    movie = movie.lower()
    if movie not in df['title'].str.lower().values:
        return ["Movie not found in dataset."]
    index = df[df['title'].str.lower() == movie].index[0]
    distances = similarity[index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    return [df.iloc[i[0]].title for i in movie_list]

st.title('🎥 Movie Recommender System')

movie_name = st.text_input('Enter a movie name:')

if st.button('Recommend'):
    recommendations = recommend(movie_name)
    st.write("### Recommended Movies:")
    for movie in recommendations:
        st.write("✅ " + movie)
