import pickle
import streamlit as st
import numpy as np
from PIL import Image

model = pickle.load(open('bestmodel.sav', 'rb'))

#judul web
st.title('PREDIKSI HARGA RUMAH DI KOTA YOGYAKARTA')

kcm = ("Kotagede","Wirobrajan","Umbulharjo","Tegalrejo","Mergangsan","Mantrijeron","Gondomanan","Kraton",
        "Gondokusuman","Pakualaman","Ngampilan","Danurejan","Gedongtengen","Jetis")

fn = ("Non Furnished","Semi Furnished","Furnished")

options = list(range(len(kcm)))
optionss = list(range(len(fn)))

tab1, tab2, tab3= st.tabs(["Home","Predict","Contact"])

with tab1:

	st.write('<div style="text-align: justify;"> Website ini dibuat untuk kamu para calon pembeli atau penjual rumah di Kota Yogyakarta. Masukkan beberapa kriteria yang kamu inginkan yaitu lokasi kecamatan, luas tanah (m2), luas bangunan (m2), jumlah kamar tidur, jumlah kamar mandi, jumlah lantai, kelengkapan fasilitas rumah, dan jumlah carport. Semoga website ini dapat membantu Anda dalam menentukan budget yang sesuai.</div>', unsafe_allow_html=True)
	image = Image.open('angga.jpg')
	st.image(image, use_column_width=True)
	st.write('Mulai prediksi harga rumah dengan klik pada menu **:red["Predict"]** di atas! 	:arrow_up:')

with tab2:

	col1, col2 = st.columns(2)
	with col1:
		Kecamatan = st.selectbox("Kecamatan", options, format_func=lambda x: kcm[x])
		LT = st.number_input('Luas Tanah (m2)',min_value=0.00)
		LB = st.number_input('Luas Bangunan (m2)',min_value=0.00) 
		KT = st.number_input('Jumlah Kamar Tidur',min_value=0, step=1)
		KM = st.number_input('Jumlah Kamar Mandi',min_value=0, step=1) 

	with col2:
		Lantai = st.radio('Jumlah Lantai',(1,2,3)) 
		Furnished = st.radio("Fasilitas", optionss, format_func=lambda x: fn[x])   
		Carport = st.number_input('Jumlah Carport',min_value=0, step=1)

		if st.button('Submit'):
			cost = model.predict(np.array([[Kecamatan,KT,KM,LT,LB,Lantai,Furnished,Carport]]))
			st.success(f'Prediksi Harga Rumah: Rp{cost[0]:,.2f}')
with tab3:
	st.write('Terima Kasih telah mengungjungi website ini 	:house_with_garden:')
	st.write(':mailbox_with_mail: Kirimkan kritik dan saran atau pertanyaan Anda!')
	
	contact_form = """
	<form action="https://formsubmit.co/nferita5@gmail.com" method="POST">
		<input type="hidden" name="_captcha" value="false">
		<input type="text" name="Nama" placeholder="Nama Anda" required>
		<input type="email" name="email" placeholder="Email Anda" required>
		<textarea name="massage" placeholder="Masukkan pesan Anda"></textarea>
		<button type="submit">Send</button>
	</form>
	"""
	st.markdown(contact_form, unsafe_allow_html=True)
	
	def local_css(file_name):
		with open(file_name) as f:
			st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
	local_css("style/style.css")
	
