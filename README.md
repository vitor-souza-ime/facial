````markdown
<h1 align="center">🧠🎭 Análise de Emoções com DeepFace</h1>

<p align="center">
  <img src="https://img.shields.io/badge/python-3.8%2B-blue" alt="Python Version">
  <img src="https://img.shields.io/badge/deepface-Emotion%20Recognition-red" alt="DeepFace">
  <img src="https://img.shields.io/badge/license-MIT-green" alt="License">
</p>

---

## 🧾 **Descrição**

Este projeto realiza a **análise automática de expressões faciais** utilizando o modelo `DeepFace`, com imagens representando as **emoções básicas de Ekman**. As imagens são obtidas de repositórios gratuitos, como o Freepik.

---

## 🗂️ **Arquivo Principal**

- 📄 `main.py`  
  Script responsável por:
  - Baixar imagens que representam as 7 emoções básicas
  - Analisar com DeepFace
  - Exibir o resultado visual das emoções esperadas e detectadas

---

## 🎯 **Objetivo**

Exibir a capacidade do modelo **DeepFace** em identificar corretamente:

> 😠 **Angry** · 🤢 **Disgust** · 😨 **Fear** · 😀 **Happy** · 😐 **Neutral** · 😢 **Sad** · 😲 **Surprise**

---

## 🔧 **Tecnologias e Bibliotecas Utilizadas**

| Ferramenta  | Descrição                              |
|-------------|------------------------------------------|
| 🐍 Python   | Linguagem principal                     |
| 🧠 DeepFace | Reconhecimento facial e emoção          |
| 📸 OpenCV   | Leitura e conversão de imagens          |
| 🌐 Requests | Download de imagens online              |
| 📊 Matplotlib | Visualização dos resultados            |

---

## 💻 **Instalação**

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/seu-repo.git
cd seu-repo
````

2. Instale as dependências:

```bash
pip install deepface opencv-python matplotlib requests
```

> ⚠️ **Nota:** Pode ser necessário instalar uma versão específica do TensorFlow compatível:

```bash
pip install tensorflow==2.11.0
```

---

## ▶️ **Como Executar**

```bash
python main.py
```

📌 O script irá:

1. 📥 Baixar imagens de cada emoção (caso ainda não existam)
2. 🔍 Detectar a emoção dominante usando DeepFace
3. 🖼️ Exibir imagem, emoção esperada e emoção detectada

---

## 📁 **Estrutura de Diretórios**

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

---

## ⚠️ **Observações**

* 🧪 A precisão pode variar de acordo com a iluminação, pose e resolução da imagem
* 🤖 DeepFace retorna a **emoção dominante com maior probabilidade**
* 🖼️ Imagens são exibidas uma por uma com `matplotlib`

---

## 📚 **Referências**

* 📘 **Ekman, P.** (1999). *Basic Emotions*. In: Dalgleish & Power (Eds), *Handbook of Cognition and Emotion*.
* 🧠 **Serengil, S. I.**, & **Ozpinar, A.** (2020). *LightFace: A Hybrid Deep Face Recognition Framework*. [DeepFace GitHub](https://github.com/serengil/deepface)

---

## 👨‍💻 Autor

**Vitor Amadeu Souza**
📍 Nova Iguaçu, RJ
📧 \[[seu-email@email.com](mailto:seu-email@email.com)]
🔗 [github.com/seu-usuario](https://github.com/seu-usuario)

