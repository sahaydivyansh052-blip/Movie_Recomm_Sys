import requests
import streamlit as st
import pickle
import pandas as pd

def fetch_poster(movie_id):
 response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=5f4d75a7341b625d0feed6accdac7f10&language=en-US'.format(movie_id))
 data = response.json()
 return "https://image.tmdb.org/t/p/w500/"+data['poster_path']

def recommend(movie):
     movie_index = movies[movies['title'] == movie].index[0]
     distances = similarity[movie_index]
     movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

     recommended_movies = []
     recommended_movies_posters = []

     for i in movies_list:
         # Get movie id to fetch poster
         movie_id = movies.iloc[i[0]].movie_id

         # Append the title
         recommended_movies.append(movies.iloc[i[0]].title)

         # Append the poster using the fetch_poster function
         recommended_movies_posters.append(fetch_poster(movie_id))

     return recommended_movies, recommended_movies_posters



# Change this:
# movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))

# To this:
movies_dict = pickle.load(open('movies.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

# Change this:
# similarity = pickle.load(open('similarity', 'rb'))

# To this:
similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    'Select a movie to get recommendations:',
    movies['title'].values)

import streamlit as st

if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)

    # Use st.columns instead of st.beta_columns
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])





    def fetch_poster(movie_id):
            url = f"https://api.themoviedb.org/3/movie/{movie_id}"
            params = {
                "api_key": "5f4d75a7341b625d0feed6accdac7f10",
                "language": "en-US"
            }

            try:
                response = requests.get(url, params=params, timeout=5)
                response.raise_for_status()
                data = response.json()
                return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

            except requests.exceptions.RequestException as e:
                print("Error fetching poster:", e)
                return "https://via.placeholder.com/300x450?text=No+Image"




