import streamlit as st
import os
outF = open("input","w")
n=st.text_input("enter n")
crys = st.text_input("cristal")
outF.write(n,n,n,"\n")
outF.write(crys)
outF.close()
os.startfile("a.out")
