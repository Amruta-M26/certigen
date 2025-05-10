import pytest
from app.certificate_generator import generate_certificates
import os
import csv

@pytest.fixture
def sample_csv(tmp_path):
    csv_path = tmp_path / "sample.csv"
    with open(csv_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Name', 'Event', 'Date'])
        writer.writerow(['John Doe', 'DevOps Workshop', '2023-10-15'])
        writer.writerow(['Jane Smith', 'DevOps Workshop', '2023-10-15'])
    return csv_path

def test_certificate_generation(sample_csv):
    output_zip = generate_certificates(sample_csv)
    assert os.path.exists(output_zip)
    assert output_zip.endswith('.zip')