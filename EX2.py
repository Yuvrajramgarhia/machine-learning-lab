import pandas as pd
from openpyxl.styles import Font, PatternFill, Border, Side

data = {
    'Model': ['Logistic Regression', 'Random Forest', 'SVM', 'XGBoost'],
    'Accuracy': [0.85, 0.92, 0.88, 0.95],
    'Inference_Time_ms': [12, 45, 30, 50]
}

df = pd.DataFrame(data)

with pd.ExcelWriter('ml_experiment_report.xlsx', engine='openpyxl') as writer:
    sheet_name = 'Model_Performance'
    df.to_excel(writer, sheet_name=sheet_name, index=False)

    worksheet = writer.book[sheet_name]

    header_font = Font(bold=True, color="FFFFFF")
    header_fill = PatternFill(start_color="4F81BD", fill_type="solid")
    border = Border(left=Side(style='thin'),
                    right=Side(style='thin'),
                    top=Side(style='thin'),
                    bottom=Side(style='thin'))

    for cell in worksheet[1]:
        cell.font = header_font
        cell.fill = header_fill
        cell.border = border

    worksheet.column_dimensions['A'].width = 25
    worksheet.column_dimensions['B'].width = 15
    worksheet.column_dimensions['C'].width = 20

print("Excel file created successfully.")