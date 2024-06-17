from pathlib import Path

documents = Path(r"C:\Users\Formation\Documents")

for f in documents.iterdir():
    print(f.name)
