import streamlit as st
import google.generativeai as genai
from PIL import Image
genai.configure(api_key="AIzaSyDR3z9bQuZBbRkY6wJLBgdW3nx2T5VekQs")
model=genai.GenerativeModel("gemini-pro")
vision_model=genai.GenerativeModel("gemini-pro-vision")