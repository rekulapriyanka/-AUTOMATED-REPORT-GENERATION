import pandas as pd
from fpdf import FPDF
from datetime import datetime
import os

# STEP 1: Create data.csv with sample data if it doesn't exist
csv_filename = 'data.csv'

if not os.path.exists(csv_filename):
    sample_data = """Date,Product,Region,Sales
2025-08-01,Widget A,North,1200
2025-08-01,Widget B,South,950
2025-08-02,Widget A,North,1100
2025-08-02,Widget B,East,780
2025-08-03,Widget A,West,1400
2025-08-03,Widget B,South,990"""
    
    with open(csv_filename, 'w') as file:
        file.write(sample_data)
    print(f"✅ Created {csv_filename}")

# STEP 2: Load CSV data
df = pd.read_csv(csv_filename)

# STEP 3: Analyze data
total_sales = df['Sales'].sum()
sales_by_product = df.groupby('Product')['Sales'].sum()
sales_by_region = df.groupby('Region')['Sales'].sum()

# STEP 4: Generate PDF using FPDF
class PDFReport(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 16)
        self.cell(0, 10, 'Sales Report', ln=1, align='C')
        self.set_font('Arial', '', 12)
        self.cell(0, 10, f'Generated on: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}', ln=1, align='C')
        self.ln(10)

    def section_title(self, title):
        self.set_font('Arial', 'B', 14)
        self.set_text_color(0, 102, 204)
        self.cell(0, 10, title, ln=1)
        self.set_text_color(0, 0, 0)

    def section_table(self, data_dict):
        self.set_font('Arial', '', 12)
        for key, value in data_dict.items():
            self.cell(80, 10, str(key), border=1)
            self.cell(40, 10, f"${value:,.2f}", border=1, ln=1)

# STEP 5: Create PDF report
pdf = PDFReport()
pdf.add_page()

pdf.section_title("Total Sales")
pdf.set_font('Arial', '', 12)
pdf.cell(0, 10, f"${total_sales:,.2f}", ln=1)
pdf.ln(5)

pdf.section_title("Sales by Product")
pdf.section_table(sales_by_product.to_dict())
pdf.ln(5)

pdf.section_title("Sales by Region")
pdf.section_table(sales_by_region.to_dict())

# STEP 6: Save PDF
pdf.output("sales_report.pdf")
print("✅ PDF report generated: sales_report.pdf")
