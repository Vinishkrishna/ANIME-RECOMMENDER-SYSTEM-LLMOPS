import streamlit as st
from pipeline.pipeline import AnimeRecommendationPipeline
from dotenv import load_dotenv

st.set_page_config(page_title="Anime Recommender",layout="wide")#once you give this then only you can go the main code it is compulsory in streamlit

load_dotenv()

@st.cache_resource #we are running it in cache to save our time
def init_pipeline():
    return AnimeRecommendationPipeline() #whenever our app starts we want to automatically initialise these things,we want to start the pipeline and catch it everytime

pipeline = init_pipeline()

st.title("Anime Recommender System")

query=st.text_input("Enter your anime preferences eg. : light hearted anime with school settings")
if query:
    with st.spinner("Fetching recommendations for you...."):
        response=pipeline.recommend(query)
        st.markdown("### Recommendations")
        st.write(response)

'''
A Dockerfile is just a set of instructions that tells Docker how to build a container image for your app.
Think of it like a recipe 📜 for creating a container.
'''
'''
Kubernetes Deployment File

Kubernetes (K8s) is a system to manage containers at scale.

A Deployment file (YAML) tells Kubernetes what containers to run, how many copies, and how to keep them healthy
'''