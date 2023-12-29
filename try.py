from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel
import uvicorn
import numpy as np
from io import BytesIO
from PIL import Image
from torchvision import transforms
import torch
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# This will allow requests from all origins. You can customize this as needed.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with specific origins if needed
    allow_credentials=True,
    allow_methods=["*"],  # You can specify specific methods if required
    allow_headers=["*"],  # You can specify specific headers if required
)

@app.get('/ping')
async def ping():
    return "hello"

##Preprocessing the image
def preprocessImage(data):
    try:
        device = torch.device('mps' if torch.backends.mps.is_available() else 'cpu')
        img = Image.open(BytesIO(data))
        transform = transforms.Compose([
            transforms.Resize([224, 224]),
            transforms.ToTensor(),
        ])
        img = transform(img).unsqueeze(0).to(device)  # Convert to tensor and move to device
        return img
    except Exception as e:
        print(f"Error processing image: {e}")
        return None

@app.post('/predict')
async def predict(file: UploadFile = File(...)):
    try:
        image_data = await file.read()
        prediction = predict_image(image_data)
        return {"prediction": prediction}
    except Exception as e:
        return {"error": str(e)}


## For prediction
def predict_image(img):

    
    model = torch.load('aerialDelterOtherOne.pth')
    model.eval()
    img = preprocessImage(img)

    with torch.no_grad():
        output = model(img)

    classes = ['grass', 'marshy', 'rocky', 'sandy']
    _, pred = output.max(1)
    return classes[pred.item()]
@app.get('/pixel_color/')
async def get_pixel_color(x: int, y: int):
    # Assuming `image` is a global variable that contains the uploaded image
    pixel_color = tuple(image[y, x])
    return {"pixel_color": pixel_color}
