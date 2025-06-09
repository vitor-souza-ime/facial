````markdown
# Análise de Emoções com DeepFace

Este projeto realiza a **análise automática de expressões faciais** utilizando o modelo `DeepFace`, aplicando-o em imagens que representam as **emoções básicas de Ekman**. As imagens são baixadas diretamente de repositórios gratuitos, como o Freepik.

## 📄 Arquivo Principal

- `main.py`: script responsável por baixar imagens representando sete emoções básicas, analisá-las com DeepFace e exibir os resultados esperados e detectados.

## 🎯 Objetivo

Demonstrar a capacidade do modelo DeepFace em identificar corretamente as emoções **disgust, happy, sad, angry, surprise, neutral e fear**, comparando os resultados com os rótulos esperados.

## 🔧 Tecnologias e Bibliotecas Utilizadas

- [Python 3.x](https://www.python.org/)
- [DeepFace](https://github.com/serengil/deepface)
- [OpenCV (cv2)](https://opencv.org/)
- [Requests](https://docs.python-requests.org/)
- [Matplotlib](https://matplotlib.org/)

## 📦 Instalação

Antes de executar o script, certifique-se de ter as bibliotecas necessárias instaladas. Você pode instalá-las com o seguinte comando:

```bash
pip install deepface opencv-python matplotlib requests
````

> **Nota**: Pode ser necessário instalar também o `tensorflow` compatível com o DeepFace, por exemplo:

```bash
pip install tensorflow==2.11.0
```

## ▶️ Execução

Execute o script com:

```bash
python main.py
```

O script irá:

1. Baixar imagens de cada emoção (se ainda não estiverem salvas).
2. Utilizar o DeepFace para detectar a emoção dominante em cada imagem.
3. Exibir a imagem, a emoção esperada e a emoção detectada.

## 📂 Estrutura de Pastas

```
📁 emotion_images/
    ├── angry.jpg
    ├── disgust.jpg
    ├── fear.jpg
    ├── happy.jpg
    ├── neutral.jpg
    ├── sad.jpg
    └── surprise.jpg
main.py
README.md
```

## 📌 Observações

* A acurácia da detecção pode variar com base na qualidade, iluminação e pose da imagem.
* O DeepFace retorna uma análise probabilística da emoção dominante.
* A imagem é processada uma por vez e exibida via `matplotlib`.

## 📚 Referências

* Ekman, P. (1999). **Basic Emotions**. In: Dalgleish & Power (Eds), *Handbook of Cognition and Emotion*.
* Serengil, S. I., & Ozpinar, A. (2020). **LightFace: A Hybrid Deep Face Recognition Framework**. *DeepFace* [https://github.com/serengil/deepface](https://github.com/serengil/deepface)

