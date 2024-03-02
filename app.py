import pickle 
import streamlit as st
import requests
def recommend(course_name, similarity_matrix, df, top_n=5):
    course_index = df[df['name'] == course_name].index[0]
    
    course_similarity = similarity_matrix[course_index]
    
    similar_courses_indices = course_similarity.argsort()[::-1][1:top_n+1]  
    similar_courses = df.iloc[similar_courses_indices]['name'].values
    
    return similar_courses

st.header('Breadth Recommendation System ')
df= pickle.load(open('/Users/mayanksethia/Desktop/python /df.pkl','rb'))
similarity = pickle.load(open('/Users/mayanksethia/Desktop/python /similarity.pkl','rb'))

names_list = df['name'].values
selected_name = st.selectbox(
    "Type or select a name from the dropdown",
    names_list
)

if st.button('Show Recommendation'):
    recommended_name_names = recommend(selected_name, similarity, df)
    
    for name in recommended_name_names:
        st.write(name)

