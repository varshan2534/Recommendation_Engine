import streamlit as st
import pickle
import pandas as pd


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    rec_mov=[]
    for i in movie_list:
        rec_mov.append(movies.loc[i[0]].title)

    return rec_mov

movies_list=pickle.load(open('movies_dict.pkl','rb'))
movies=pd.DataFrame(movies_list)

similarity=pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommender')

sel_mov = st.selectbox('Select Movie',movies['title'].values)

if st.button("Recommend"):
    recommendations = recommend(sel_mov)
    for i in recommendations:
        st.write(i)