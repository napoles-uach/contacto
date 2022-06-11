import streamlit as st
import os
import subprocess
import sys


os.system("chmod +x a.out")




#subprocess.run([f"{sys.executable}", "a.out"])
#subprocess.run(['ls','-l'])
os.system("#!/bin/bash a.out")
ls=st.button('ls')
if ls:
    subprocess.run(['ls','-l'])
st.write("done")




