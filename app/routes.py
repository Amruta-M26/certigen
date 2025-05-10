from flask import Flask, render_template, request, send_file
import os
from app.certificate_generator import generate_certificates

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.path.join('app', 'static', 'uploads')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'csv_file' not in request.files:
        return "No file uploaded", 400
    
    file = request.files['csv_file']
    if file.filename == '':
        return "No selected file", 400
    
    if file and file.filename.endswith('.csv'):
        filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filename)
        
        # Generate certificates
        output_zip = generate_certificates(filename)
        
        return send_file(output_zip, as_attachment=True)
    
    return "Invalid file type", 400

if __name__ == '__main__':
    app.run(debug=True)