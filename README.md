# Organizador de Arquivos por Categoria
## Descrição
Este script em Python automatiza a organização de arquivos, movendo-os para subpastas com base em categorias pré-definidas (como Imagens, Documentos, Vídeos, etc.).

Diferente de uma abordagem manual, este script utiliza uma janela de diálogo gráfica para que o usuário possa selecionar de forma interativa qual pasta deseja organizar, tornando o processo mais simples e seguro.

## Funcionalidades
Seleção de Diretório Interativa: Abre uma janela do sistema para que o usuário selecione a pasta a ser organizada, sem a necessidade de editar o código.

Organização por Categorias: Agrupa diferentes tipos de arquivos em pastas de categoria. Por exemplo, arquivos .png e .jpg são movidos para a pasta imagens.

Criação Automática de Pastas: As pastas de destino (ex: documentos, videos) são criadas automaticamente se ainda não existirem no diretório selecionado.

Eficiência: Arquivos que não correspondem a nenhuma categoria pré-definida são ignorados e permanecem em seu local original.

## Categorias e Extensões
O script organiza os arquivos de acordo com as seguintes regras:

imagens: .png, .jpg, .jpeg, .gif, .bmp, .webp, .ico

planilhas: .xlsx, .xls, .ods, .csv

documentos: .pdf, .docx, .txt, .odt, .pptx

video: .mp4, .mov, .avi, .mkv

musicas: .mp3, .wav, .flac

zips: .zip, .rar, .7z, .tar.gz

## Pré-requisitos
Python 3.x

Biblioteca Tkinter: Geralmente já vem incluída na instalação padrão do Python. Em algumas distribuições Linux, pode ser necessário instalá-la separadamente (ex: sudo apt-get install python3-tk).

## Aviso Importante
Este script executa operações de movimentação de arquivos no seu sistema. É altamente recomendável que você faça um backup do diretório que será organizado antes de executar o script pela primeira vez para prevenir qualquer perda acidental de dados.
