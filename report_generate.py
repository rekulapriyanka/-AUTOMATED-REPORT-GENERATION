import pandas as pd
from fpdf import FPDF
import os

# Sample data to include in the report
report_data = [
    {"name": "Alice", "sales": 1200, "region": "North"},
    {"name": "Bob", "sales": 950, "region": "East"},
    {"name": "Charlie", "sales": 1130, "region": "South"},
]


# Create a PDF class inheriting from FPDF
class PDFReport(FPDF):
    def header(self):
        self.set_font("Arial", "B", 14)
        self.cell(0, 10, "Monthly Sales Report", ln=True, align="C")
        self.set_font("Arial", "", 10)
        self.cell(0, 10, "Generated on: 2025-08-11", ln=True, align="C")
        self.ln(10)

    def add_table(self, data):
        self.set_font("Arial", "B", 12)
        self.cell(40, 10, "Name", 1)
        self.cell(40, 10, "Sales", 1)
        self.cell(60, 10, "Region", 1)
        self.ln()

        self.set_font("Arial", "", 12)
        for row in data:
            self.cell(40, 10, row["name"], 1)
            self.cell(40, 10, str(row["sales"]), 1)
            self.cell(60, 10, row["region"], 1)
            self.ln()

# Generate the PDF report
pdf = PDFReport()
pdf.add_page()
pdf.add_table(report_data)

# Output the PDF to a file
output_filename= "sales_report.pdf"
pdf.output(output_filename)
print("Report saved at:",output_filename)
