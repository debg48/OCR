#import dependencies
import streamlit as st
import easyocr
import cv2
import numpy as np
import datetime
import time 

uploaded_file = st.file_uploader("Choose a image file", type=["jpg","png"])

if uploaded_file is not None:
    # Convert the file to an opencv image.
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    opencv_image = cv2.imdecode(file_bytes, 1)

    # display image
    st.image(opencv_image, channels="BGR")

    schedule = False

    option = st.selectbox(
        'Would you like to schedule the extraction ?',
        ('Yes', 'No'),index=1)

    schedule = st.button('Submit')

    # this loop will run until the user clicks the submit button
    while(schedule == False):
        # print(schedule)
        pass
    

    if(option == 'Yes'):
        t = st.time_input('Schedule Time for Extraction',value= None )
        
        st.write('Extraction time is set for', t)
        loop_button = st.button('Submit')
        while(loop_button == False):
            pass
        
    else : 
        t=datetime.datetime.now().time()

    print(t)
    print(datetime.datetime.now().time())
    if (t <= datetime.datetime.now().time()):

        st.subheader('Extracting Text ! This may take a few minutes......')

        # performing OCR
        reader = easyocr.Reader(['en'],gpu=False)
        result = reader.readtext(opencv_image)
        
        st.subheader('Extracted Text :')

        # text = ''

        with st.expander('', expanded=True):
            for i in range(len(result)):
                st.write(result[i][1])
        
        #     print(result[i][1])
        #     text = text + ' ' + (result[i][1])
        #     print(text)
        # st.write(text.strip())
        