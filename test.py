import glob
import time

time_start = time.time()
text_files = glob.glob("C:\**\chrome.exe", recursive=True)

print(text_files)
print(time.time() - time_start)
