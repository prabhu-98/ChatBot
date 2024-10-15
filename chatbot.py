# import streamlit as st
# from PIL import Image
# st.title('CLEANREAD')
# options=['general q & a chatbot','pdf summarizer',
#          'article summarizer','bias detection','unbias','evaluate']
# feature=st.selectbox('select feature',options)


# accepted_filetypes = ['csv', 'txt', 'pdf', 'docx','pdf','jpg','jpeg']  # Add your desired extensions

# file=st.file_uploader('upload your file if necessary',type=accepted_filetypes) 
# prompt=st.text_input('enter your query')
# button=st.button('submit')
# if button:
#     if feature == 'general q & a chatbot':
#        from qa import get_response
#        result=get_response(prompt)
#        st.write(result)
#     elif feature == 'pdf summarizer':
#        from pdf import get_response
#        result=get_response(file,prompt)

#        st.write(result)
#     elif feature =='article summarizer' :
#        from article import get_response
#        result=get_response(prompt)
#        st.write(result)
#     elif feature =='bias detection':
#        import sent as s
#        analysis = s.analyze_text(prompt)
#        gender_bias = s.identify_gender_bias(analysis)
#        result = s.is_text_biased(gender_bias)
#        st.write(result)
#     elif feature == 'unbais':
#        import clean as c
#        result=c.replace_gender_biased_words(prompt)
#        st.write(result)
#     elif feature =='evaluate':
#        import evaluation as e
#        text = e.read_entire_file(file)
#        result = e.evaluate(text,prompt)
#        st.write(result)
       
#       #  if file is not None:
#       #       file_type = file.type
#       #       if "image" in file_type:
#       #           image = Image.open(file)
#       #           st.image(image, caption="Uploaded Image.", use_column_width=True)
#       #       elif "txt" in file_type:
#                #  text = e.read_entire_file(file)
#                #  result = e.evaluate(text,prompt)
#                #  st.write(result)






import streamlit as st
from PIL import Image

st.title('CLEANREAD')
options = ['general q & a chatbot', 'pdf summarizer', 'article summarizer', 'bias detection', 'unbias', 'evaluate']
feature = st.selectbox('select feature', options)

accepted_filetypes = ['csv', 'txt', 'pdf', 'docx', 'jpg', 'jpeg']  # Add your desired extensions

file = st.file_uploader('upload your file if necessary', type=accepted_filetypes) 
prompt = st.text_input('enter your query')
button = st.button('submit')

if button:
    if feature == 'general q & a chatbot':
        from qa import get_response
        result = get_response(prompt)
        st.write(result)
    elif feature == 'pdf summarizer':
        from pdf import get_response
        result = get_response(file, prompt)
        st.write(result)
    elif feature == 'article summarizer':
        from article import get_response
        result = get_response(prompt)
        st.write(result)
    elif feature == 'bias detection':
        import sent as s
        analysis = s.analyze_text(prompt)
        gender_bias = s.identify_gender_bias(analysis)
        result = s.is_text_biased(gender_bias)
        st.write(result)
    elif feature == 'unbias':
        import clean as c
        result = c.replace_gender_biased_words(prompt)
        st.write(result)
    elif feature == 'evaluate':
        import evaluation as e
        text=e.read_entire_file(file)
        result=e.evaluate(text,prompt)
        st.write(result)
       
          
          
       
    
       