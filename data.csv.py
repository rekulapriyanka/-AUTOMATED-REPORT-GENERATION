# Install dependencies if needed:
# pip install pandas fpdf matplotlib

import pandas as pd
from fpdf import FPDF
import matplotlib.pyplot as plt

# 1. Load & Analyze Data
df = pd.read_csv('data.csv')  
# Replace with your filename
summary = df.describe().round(2)

# 2. Generate a Plot (optional)
plt.figure(figsize=(4,3))
summary['mean'].plot(kind='bar', title='Mean by Column')
plt.tight_layout()
plt.savefig('plot.png')

# 3. Create PDF Report
class PDFReport(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 14)
        self.cell(0, 10, 'Automated Data Report', border=0, ln=1, align='C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', align='C')
        

pdf = PDFReport()
pdf.add_page()
pdf.set_font('Arial', '', 12)

# Add Summary Table
for col in summary.columns:
    pdf.cell(40, 10, col, border=1, align='C')
pdf.ln()
for idx, row in summary.iterrows():
    for val in row:
        pdf.cell(40, 10, str(val), border=1, align='C')
    pdf.ln()

# Insert Plot
pdf.image('plot.png', x=60, y=None, w=90)

pdf.output('report.pdf')
print("Report generated: report.pdf")
