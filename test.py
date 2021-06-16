exec(open("importer.py").read())
import os
try:
  os.system("echo \"failure\"")
except:
  print("success")
import subprocess
try:
  subprocess.run("echo \"failure\"")
except:
  print("success")