import os
from tkinter.filedialog import askdirectory

caminho = askdirectory(title="Selecione uma pasta")

lista_arquivos = os.listdir(caminho)

locais = {
    "imagens": [".png", ".jpg", ".jpeg", ".gif", ".bmp", ".webp", ".ico"],
    "planilhas": [".xlsx"],
    "documentos": [".pdf", ".docx", ".txt", ".odt", ".pptx"],
    "csv": [".csv"],
    "planilhas": [".xlsx", ".xls", ".ods", ".csv"],
    "video": [".mp4", ".mov", ".avi", ".mkv"],
    "musicas": [".mp3", ".wav", ".flac"],
    "zips": [".zip", ".rar", ".7z", ".tar.gz"]
}

for arquivo in lista_arquivos:
    
    nome, extensao = os.path.splitext(f"{caminho}/{arquivo}")
    for pasta in locais:
        if extensao in locais[pasta]:
            if not os.path.exists(f"{caminho}/{pasta}"):
                os.mkdir(f"{caminho}/{pasta}")

            os.rename(f"{caminho}/{arquivo}", f"{caminho}/{pasta}/{arquivo}")
