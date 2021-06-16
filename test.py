exec(open("importer.py").read())
import os, subprocess, shutil
try:
  os.system("echo \"failure\"")
except:
  print("success")
try:
  os.rmdir("../restricted-functions")
except:
  print("success")
try:
  subprocess.run("echo \"failure\"")
except:
  print("success")
try:
  subprocess.check_output("echo \"failure\"")
except:
  print("success")
try:
  subprocess.call("echo \"failure\"")
except:
  print("success")
try:
  shutil.rmtree("../restricted-functions")
except:
  print("success")