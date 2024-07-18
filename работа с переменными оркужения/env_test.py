from dotenv import load_dotenv
import os

load_dotenv()

if os.getenv('DEVELOPER'):
    print("Привет разраб")
else:
    print("Hello")

#НЕ ЗАБЫВАЙ ПРО gitignore)