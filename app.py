import streamlit as st
import os

n=st.text_input("enter n")
crys = st.text_input("cristal")
if (n and crys):
    outF = open("input","w")
    st.write(n,crys)
    outF.write(n+'\n'+crys)
    #outF.write("\n")
    #outF.write(crys)
    outF.close()
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file:
#uploaded_files = st.sidebar.file_uploader("Choose xyz files", accept_multiple_files=False)
#for uploaded_file in uploaded_files:
    xyz = uploaded_file.getvalue().decode("utf-8")
    # add a new line when non integer is found in the xyz file
    #for line in xyz.splitlines():
    #    st.write(line)
    

    #st.write(xyz)
    mol = open("FileInput.xyz","w")
    for line in xyz.splitlines():
        mol.write(line+'\n')
    mol.close()
os.system("chmod +x a.out")
os.system("./a.out")
st.write("done")
os.system("cat input")
os.system("ls")
st.write(mol)
