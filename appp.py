import pickle
import streamlit as st
import pandas as pd

# Load pickle files
with open('similarity.pkl', 'rb') as f:
    similarity = pickle.load(f)

with open('title.pkl', 'rb') as f:
    recommender_df = pickle.load(f)

# Define the Streamlit app
def main():
    st.title('Movie Recommender System')
    
    # Movie selection dropdown
    selected_movie = st.selectbox('Select a movie:', list(recommender_df["title"]))

    # Button to trigger recommendations
    if st.button('Get Recommendations'):
        st.write("Fetching recommendations for:", selected_movie)
        
        # Call the recommend function
        def recommend(movie):
            try:
                recommendations = []
                index = recommender_df[recommender_df['title'] == movie].index[0]
                distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
                # List top ten recommended movies
                for i in distances[1:11]:
                    recommendations.append(recommender_df.iloc[i[0]]['title'])
                return recommendations
            except IndexError:
                return 'Invalid Entry'

        # Display recommendations
        recommendations = recommend(selected_movie)
        if recommendations != 'Invalid Entry':
            st.write("You may also enjoy:")
            st.write(recommendations)
        else:
            st.write("Invalid entry. Please try again.")

if __name__ == "__main__":
    main()
