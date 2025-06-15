This project is a PDF and image processing pipeline with professional code and data versioning using **Git + DVC**.

## Objective

To automate the processing of resumes (CVs) and other visual evidence (such as JPG images) by extracting text, storing clean versions, and generating annotated images.

---

## Project Structure

(To be added if needed, e.g., using tree or manually listing folders and files)

---

## Technologies Used

- **Python 3.10**
- PyMuPDF for reading PDF documents
- OpenCV for image annotation
- DVC for data versioning
- Git for code versioning
- Google Drive as remote storage for large files
- GitHub as the project repository

---

## Environment Setup

1. Clone the repository:
   
bash
   git clone https://github.com/cdiazcastilla/leadsync-pipeline.git
   cd leadsync-pipeline
2. Create and activate a virtual environment:
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

3. Install dependencies:
   pip install -r requirements.txt
   
4. Initialize DVC (only needed the first time):
   dvc init
   
5. Remove large files from Git tracking and add them to DVC:
   git rm --cached data/raw_pdfs/HV\ Carlos\ Diaz.pdf
git rm --cached data/raw_images/IMG-4235.jpg
git rm --cached data/annotated_images/IMG-4235.jpg

dvc add data/raw_pdfs/HV\ Carlos\ Diaz.pdf
dvc add data/raw_images/IMG-4235.jpg
dvc add data/annotated_images/IMG-4235.jpg

6. Configure remote storage (Google Drive):
  dvc remote add -d gdrive_remote gdrive://1wD9cBaduXEpNNwN8qhtMffQdHdea4aTg

7. Push data files to remote storage:
dvc push

8. Finally, push everything to GitHub:
   8. Finally, push everything to GitHub:
   ```bash
   git add .
   git commit -m "Initial commit with DVC setup"
   git push origin main

Usage
To run the pipeline for extracting and annotating files:
python scripts/process_pdfs.py
python scripts/annotate_images.py



Contact
For questions or contributions, please contact:

Carlos Díaz
cdiazcastilla3@gmail.com
GitHub: cdiazcastilla


