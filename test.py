__ref__(ref._ProtectFiles, ref._ProtectDirs, ref._LockPerms, ref._Silent)
import os, subprocess
os.system("echo \"failure\"")
os.rmdir("../restricted-functions")
subprocess.run("echo \"failure\"")
subprocess.check_output("echo \"failure\"")
subprocess.call("echo \"failure\"")
try: open("setup.py", "w").write("text")
except Exception as e: print(e) # Testing
else: print("Failed to block write")
