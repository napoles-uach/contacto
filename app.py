import streamlit as st
import os
import subprocess
import sys

import sys, string, os, subprocess
from subprocess import PIPE, Popen, STDOUT
os.system("chmod +x a.out")
s = Popen("a.out", stdin=PIPE, stdout=PIPE, stderr=PIPE, shell = True)


#subprocess.run([f"{sys.executable}", "a.out"])
subprocess.run(['ls','-l'])
#os.system("#!/bin/bash a.out")
st.write("done")




