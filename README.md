Project: Autofillr (temp name)

## Description

An open-source Python-based OCR tool designed to read forms from images or PDFs, extract relevant fields, and autofill them into structured formats like .json, .docx, and .txt. Designed for high accuracy (goal: 95%) with error handling and warnings based on OCR confidence scores.

## Core Features

* Multi-format input: .jpg, .png, .pdf
* Image preprocessing for OCR accuracy
* Intelligent field mapping schema
* Confidence-based warning system:
* Above 90%: "Autofill succeeded. Please review"
* 80% - 90%: "Success with minor issues. Diligent review advised."
* Below 80%: "Warning: Autofill unreliable. Manual entry recommended."
* Export options: .json, .docx, .txt

## Tech Stack

* Python
* Tesseract / EasyOCR
* OpenCV
* Pillow
* Flask (Phase 2 UI)
* PyTest
* Export: python-docx, json, txt
