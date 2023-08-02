
import streamlit as st
import pickle
import requests
import pandas as pd

def recommend(movie):
    movie_index = movies[movies["title"] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    # This return the five movies name in return
    recommended_movies = []

    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)

    return recommended_movies


# this is used to load the movie list here firstly convert the values into the dictionary
movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title("Movie Recommender System")


# This code is used for the creating a box
selected_movie_name = st.selectbox('How would you like to be contacted?',
movies["title"].values)
st.write("Your selected movie :", selected_movie_name)


if st.button("Recommended"):
    recommendation = recommend(selected_movie_name)
    for i in recommendation:
        st.write(i)
