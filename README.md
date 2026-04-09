# AI-Manga-Scanlator
AI-powered manga scanlation pipeline. Takes raw Japanese manga pages, detects text regions, extracts text with OCR, translates using DeepL, removes original text, and typesets English back into speech bubbles.

Features:
Japanese OCR using MangaOCR, 
Translation via DeepL API, 
Text region detection using YOLOv8, 
Automatic text removal (inpainting), 
Basic typesetting inside detected regions, 
Batch processing of entire chapters 

Prerequisites:
Python 3.10 recommended, 
DeepL API Key

Required Python Packages (pip):
manga-ocr, 
torch, 
transformers, 
fugashi, 
unidic-lite, 
pillow, 
numpy, 
opencv-python, 
ultralytics, 
deepl, 
python-dotenv, 
tqdm
(Run "pip install -r requirements.txt" to install all required packages)

Notes:
This project does not translate sound effects (SFX). 
Typesetting is basic and can be improved. 
Performance depends on hardware (GPU recommended for faster OCR). 

Future Improvements:
Better text detection (CRAFT / segmentation models), 
Improved inpainting (LaMa / diffusion models), 
Advanced typesetting (auto wrapping, fonts, alignment), 
GUI for easier usage. 
