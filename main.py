import streamlit as st 
from PIL import Image
import scan as s 
import numpy as np 

st.title('Document Scanner')
st.markdown('you can scan your document by uploading the picture')
uploaded = st.file_uploader("Upload your picture", type=("png", "jpg","jpeg"))
if uploaded is not None:
	st.write('Sucessfully Uploaded!')
	img = Image.open(uploaded)
	st.image(img,width=400)
	image=np.array(img)
	st.write('Detecting edges...')
	edged, ratio=s.edge_detection(image)
	egde_pic=Image.fromarray(edged)
	st.image(egde_pic)
	st.write('Finding countour...')
	contoured,screenCnt=s.find_contours(image,edged)
	contoured_pic=Image.fromarray(contoured)
	st.image(contoured_pic)
	st.write('Almost Ready...')
	final=s.perspective(image,screenCnt,ratio)
	final_pic=Image.fromarray(final)
	st.image(final_pic)
	if st.button("Download"):
		s.download(final)
		st.write('Downloaded Sucessfully')





