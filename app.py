import streamlit as st
import pickle
import pandas as pd
# import requests
#
# def fetch_poster(movie_id):p
#     requests
def recomender(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])


    recommended_movies =[]
    for i in distances[1:6]:
        movie_id= i[0]
        recommended_movies.append(movies.iloc[i[0]].title)

    return recommended_movies

movies_dict = pickle.load(open('movie1_list.pkl','rb'))
movies  = pd.DataFrame(movies_dict)
st.title("Movie Recommedeer System")

similarity = pickle.load(open('similarity.pkl','rb'))

selected_movie_name = st.selectbox(
'How would you like to be contacted?',
movies['title'].values)

if st.button('Recommend'):
    recomendation = recomender(selected_movie_name)
    for i in recomendation:
        st.write(i)
