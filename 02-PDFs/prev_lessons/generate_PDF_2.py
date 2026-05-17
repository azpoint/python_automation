import pandas
from fpdf import FPDF

df = pandas.read_excel("input/data.xlsx")
# print(df)

for index, row in df.iterrows():
    # print(row["name"])
    pdf = FPDF(orientation="P", unit="pt", format="A4")
    pdf.add_page()

    pdf.set_font(family="Times", style="B", size=24)
    pdf.cell(w=0, h=50, txt=row["name"], align="C", ln=1)  # type: ignore

    for column in df.columns[1:]:
        pdf.set_font(family="Times", style="B", size=14)
        pdf.cell(w=100, h=30, txt=f"{column.title()}:")  # type: ignore

        pdf.set_font(family="Times", size=14)
        pdf.cell(w=100, h=30, txt=row[column], ln=1)  # type: ignore

    pdf.output(f"output/{row['name']}.pdf")
