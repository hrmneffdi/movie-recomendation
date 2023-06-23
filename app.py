import streamlit as st
import pickle
import pandas as pd


film = pickle.load(open('film.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))


def system(name_movie):
	index = film[film['title'] == name_movie].index[0]
	recomend = similarity[index]
	recomend = sorted(list(enumerate(recomend)), reverse=True, key=lambda x:x[1])[1:6]

	id_recomend = []
	for i in recomend:
		movie_id = i[0]
		st.write(film.iloc[i[0]].title)



st.title('Film Recomender System')

opsi = st.selectbox('Mau lihat film apa?',
	film.title.values.tolist())

if st.button('Search'):
	system(opsi)