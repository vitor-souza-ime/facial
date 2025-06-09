import os
import cv2
import requests
from deepface import DeepFace
import matplotlib.pyplot as plt

# Emoções a serem testadas
emotions = {
    "disgust": "https://img.freepik.com/free-photo/teenager-girl-grimaces-with-displeasure-white-background-isolated_169016-55118.jpg?semt=ais_hybrid&w=740",
    "happy": "https://img.freepik.com/premium-photo/laughing-positive-young-afro-american-man-red-shirt-good-mood-with-closed-eyes_165285-1399.jpg?semt=ais_hybrid&w=740",
    "sad": "https://img.freepik.com/premium-photo/man-sitting-couch-deep-thought-inside-home_922936-30597.jpg?semt=ais_hybrid&w=740",
    "angry": "https://img.freepik.com/free-photo/emotional-screaming-young-african-man_171337-9636.jpg?semt=ais_items_boosted&w=740",
    "surprise": "https://img.freepik.com/free-photo/man-wearing-denim-shirt-red-suspenders_273609-19912.jpg?semt=ais_hybrid&w=740",
    "neutral": "https://img.freepik.com/free-photo/indoor-shot-angry-grumpy-young-mixed-race-female-dressed-casually-keeping-arms-folded-looking-with-strict-skeptical-expression_273609-1244.jpg?semt=ais_items_boosted&w=740",
    "fear": "https://img.freepik.com/free-photo/intense-afraid-handsome-male-feeling-scared-shocked-biting-fingernail-staring-with-popped-eyes_176420-25006.jpg"
    
}

# Pasta para salvar imagens
os.makedirs("emotion_images", exist_ok=True)

# Função para baixar imagem
def download_image(url, filename):
    response = requests.get(url)
    with open(filename, "wb") as f:
        f.write(response.content)

# Baixar imagens
for emotion, url in emotions.items():
    img_path = f"emotion_images/{emotion}.jpg"
    download_image(url, img_path)

# Analisar imagens com DeepFace
for emotion in emotions:
    img_path = f"emotion_images/{emotion}.jpg"
    try:
        result = DeepFace.analyze(img_path=img_path, actions=['emotion'], enforce_detection=True)[0]
        detected_emotion = result['dominant_emotion']

        # Mostrar imagem e resultado
        img = cv2.imread(img_path)
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        plt.imshow(img_rgb)
        plt.title(f"Expected: {emotion.capitalize()} | Detected: {detected_emotion.capitalize()}")
        plt.axis("off")
        plt.show()
    except Exception as e:
        print(f"Erro ao processar {emotion}: {str(e)}")
