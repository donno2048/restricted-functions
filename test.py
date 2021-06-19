import ref
ref.main(__builtins__, restrictwrite = True)
import os, subprocess, shutil
try: os.system("echo \"failure\"")
except: pass
else: raise Exception("failed")
try: os.rmdir("../restricted-functions")
except: pass
else: raise Exception("failed")
try: subprocess.run("echo \"failure\"")
except: pass
else: raise Exception("failed")
try: subprocess.check_output("echo \"failure\"")
except: pass
else: raise Exception("failed")
try: subprocess.call("echo \"failure\"")
except: pass
else: raise Exception("failed")
try: shutil.rmtree("../restricted-functions")
except: pass
else: raise Exception("failed")
try: open("w", "setup.py").write("text")
except: pass
else: print("Failed to block write")
