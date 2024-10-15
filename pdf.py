prompt=f"""Given the text provided, please generate a concise and informative summary as bullet points, highlighting
the main ideas, key points, and significant details. Ensure the summary is coherent and captures
the essence of the text. If possible, include any notable examples or supporting evidence mentioned
in the original text and change your summary text size along with original text size. Please aim for brevity
while maintaining accuracy and relevance. If there are specific sections or aspects you find particularly
important, feel free to emphasize those in the summary.Text to be summarized:"""
def get_response(pdf_path,question):
    import pdfplumber
    from libraries import model
    text_content = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text_content += page.extract_text()
    if question == "":
        response=model.generate_content(prompt+text_content)
    else:
        response=model.generate_content(text_content+" "+question)
        
    return response.text