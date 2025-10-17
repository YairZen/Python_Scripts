import time
from datetime import datetime

print("🚀 Starting script...")
time.sleep(1)
print(f"Hello {input('Enter your name: ')}!")
print("Current time:", datetime.now().strftime("%H:%M:%S"))
time.sleep(1)
print("✅ Done successfully!")
input("Press enter to exit...")
