# import google.generativeai as genai

# genai.configure(api_key="AIzaSyDR3z9bQuZBbRkY6wJLBgdW3nx2T5VekQs")

# model= genai.GenerativeModel(
#   model_name="gemini-pro"
# )
# modelv=genai.GenerativeModel("gemini-pro-vision")
# chat_session = model.start_chat(
#   history=[
#     {
#       "role": "user",
#       "parts": [
#         "question: write about taj mahal?\n answer: i don't know \n\n evaluate the answer of the question on the scale of 5 star\nedit\n",
#       ],
#     },
#     {
#       "role": "model",
#       "parts": [
#         "The answer \"I don't know\" is a **1-star** response. \n\nHere's why:\n\n* **It lacks any information:** The answer doesn't provide any details about the Taj Mahal, even a simple sentence.\n* **It shows no effort:**  The person clearly didn't attempt to research or even offer a simple guess.\n* **It's unhelpful:**  The person asking the question is left with no information.\n\nHere's how the answer could be improved:\n\n**A 5-star response would be:**\n\n* **Informative:** Provide details about the Taj Mahal, such as its history, location, significance, and any other relevant facts.\n* **Engaging:**  Use descriptive language to paint a picture of the Taj Mahal's beauty and grandeur.\n* **Well-structured:**  Organize the information in a clear and concise manner.\n\n**Example of a",
#       ],
#     },
#   ]
# )
# def read_entire_file(filename):

#   try:
#     with open(filename, 'r') as f:
#       return f.read()
#   except FileNotFoundError:
#     print(f"Error: File '{filename}' not found.")
#     return None
# def evaluate(text,question):
#       response = chat_session.send_message("question: "+question+" ?"+"answer: "+text+"  evaluate the answer of the question on the scale of 5 star")
#       return response

# # # print(response.text)







# import google.generativeai as genai

# genai.configure(api_key="AIzaSyDR3z9bQuZBbRkY6wJLBgdW3nx2T5VekQs")

# model = genai.GenerativeModel(model_name="gemini-pro")
# modelv = genai.GenerativeModel("gemini-pro-vision")
from libraries import model
chat_session = model.start_chat(
    history=[
        {
            "role": "user",
            "parts": [
                "question: write about taj mahal?\n answer: i don't know \n\n evaluate the answer of the question on the scale of 5 star\nedit\n",
            ],
        },
        {
            "role": "model",
            "parts": [
                "The answer \"I don't know\" is a **1-star** response. \n\nHere's why:\n\n* **It lacks any information:** The answer doesn't provide any details about the Taj Mahal, even a simple sentence.\n* **It shows no effort:**  The person clearly didn't attempt to research or even offer a simple guess.\n* **It's unhelpful:**  The person asking the question is left with no information.\n\nHere's how the answer could be improved:\n\n**A 5-star response would be:**\n\n* **Informative:** Provide details about the Taj Mahal, such as its history, location, significance, and any other relevant facts.\n* **Engaging:**  Use descriptive language to paint a picture of the Taj Mahal's beauty and grandeur.\n* **Well-structured:**  Organize the information in a clear and concise manner.\n\n**Example of a",
            ],
        },
    ]
)

def read_entire_file(file):
    try:
        return file.read().decode('utf-8')
    except Exception as e:
        print(f"Error: {e}")
        return None

def evaluate(text1, question):
    response = chat_session.send_message("question: " + question + " ? answer: " + text1 + "  evaluate the answer of the question on the scale of 5 star")
    text_output = response.text
    return text_output