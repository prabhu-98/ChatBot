from libraries import model
def get_response(question):
    response=model.generate_content(question)
    return response.text

    