import os 
import shutil 

# 1. تحديد المجلد الحالي الذي توجد فيه الملفات
current_dir = os.getcwd()

# 2. قراءة أسماء كافة الملفات داخل المجلد
all_files = os.listdir(current_dir)

# 3. طباعة الأسماء للتأكد أن بايثون يراها
print("all files is :", all_files)

os.makedirs("Photos", exist_ok=True)
os.makedirs("Vedioes", exist_ok=True)
os.makedirs("Doc", exist_ok=True)

for photo in all_files:
    if photo.endswith (".jpg"):
        shutil.move(photo,os.path.join("Photos",photo))

PhotosFiles = os.listdir("Photos")
print (PhotosFiles)

for vedio in all_files:
    if vedio.endswith(".mp4"):
        shutil.move(vedio,os.path.join("Vedioes",vedio))

VedioFiles = os.listdir ("Vedioes")
print (VedioFiles)

for document in all_files:
    if document.endswith (".docx"):
        shutil.move(document,os.path.join("Doc",document))  

DocumentsFiles = os.listdir ("Doc")
print (DocumentsFiles)             