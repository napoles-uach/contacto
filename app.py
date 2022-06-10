import streamlit as st
import os
outF = open("input","w")
n=st.text_input("enter n")
crys = st.text_input("cristal")
if (n and crys):
    outF.write(n)
    outF.write("\n")
    outF.write(crys)
    outF.close()
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file:
#uploaded_files = st.sidebar.file_uploader("Choose xyz files", accept_multiple_files=False)
#for uploaded_file in uploaded_files:
    xyz = uploaded_file.getvalue().decode("utf-8")
    mol = open("FileInput.xyz","w")
    for line in xyz:
        mol.write(line,"\n")
    mol.close()
os.system("chmod +x a.out")
#os.system(" ./a.out")
#os.system("ls")
