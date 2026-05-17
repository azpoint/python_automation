from fpdf import FPDF

# Setup Document
pdf = FPDF(orientation="P", unit="pt", format="A4")

# Add a page
pdf.add_page()

# Add content
# Image
pdf.image("tiger.jpeg", w=80, h=50)

# Add Text
pdf.set_font(family="Times", style="B", size=24)
pdf.cell(w=0, h=50, txt="Malayan Tiger", align="C", border=1, ln=1)  # type: ignore

pdf.set_font(family="Times", style="B", size=14)
pdf.cell(w=0, h=30, txt="Description", ln=1)  # type: ignore

pdf.set_font(family="Times", size=12)
txt1 = """The Malayan tiger is a tiger from a specific population of the Panthera tigris tigris subspecies that is native to Peninsular Malaysia. This population inhabits the southern and central parts of the Malay Peninsula, and has been classified as critically endangered. As of April 2014, the population was estimated at 80'-'120 mature individuals, with a continuing downward trend."""
pdf.multi_cell(w=0, h=15, txt=txt1)  # type: ignore

pdf.set_font(family="Times", style="B", size=14)
pdf.cell(w=100, h=30, txt="Kingdom:")  # type: ignore
pdf.set_font(family="Times", size=14)
pdf.cell(w=100, h=30, txt="Animalia", ln=1)  # type: ignore

pdf.set_font(family="Times", style="B", size=14)
pdf.cell(w=100, h=20, txt="Phylum:")  # type: ignore
pdf.set_font(family="Times", size=14)
pdf.cell(w=100, h=20, txt="Chordata")  # type: ignore

pdf.output("output.pdf")
