import streamlit as st
import os
import subprocess
import sys



os.system("chmod +x a.out")
subprocess.run([f"{sys.executable}", "a.out"])
#os.system("#!/bin/bash a.out")
st.write("done")
os.system("ls")
st.button("donde")



