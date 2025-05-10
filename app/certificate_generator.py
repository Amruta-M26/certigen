import csv
import os
import zipfile
from fpdf import FPDF
from datetime import datetime

def generate_certificates(csv_path):
    # Create output directory
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_dir = os.path.join("app", "static", f"certificates_{timestamp}")
    os.makedirs(output_dir, exist_ok=True)
    
    # Process CSV
    with open(csv_path, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=24)
            pdf.cell(200, 10, txt="Certificate of Participation", ln=1, align="C")
            pdf.set_font("Arial", size=18)
            pdf.cell(200, 10, txt=f"This certifies that {row['Name']}", ln=1, align="C")
            pdf.cell(200, 10, txt=f"participated in {row['Event']}", ln=1, align="C")
            pdf.cell(200, 10, txt=f"on {row['Date']}", ln=1, align="C")
            output_path = os.path.join(output_dir, f"{row['Name']}_certificate.pdf")
            pdf.output(output_path)
    
    # Create zip file
    zip_path = f"{output_dir}.zip"
    with zipfile.ZipFile(zip_path, 'w') as zipf:
        for root, _, files in os.walk(output_dir):
            for file in files:
                file_path = os.path.join(root, file)
                zipf.write(file_path, os.path.relpath(file_path, output_dir))
    
    return zip_path