import importer
import os, subprocess
try:
  os.system("echo \"failure\"")
except:
  print("success")
try:
  subprocess.run("echo \"failure\"")
except:
  print("success")
