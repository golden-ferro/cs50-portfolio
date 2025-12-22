from fpdf import FPDF

def main() :
    name = input("Name: ")

    pdf = FPDF(orientation="P", format="A4")
    pdf.add_page()

    pdf.set_auto_page_break(False)

    pdf.image("shirtificate.png", x=0, y=70, w=210)

    pdf.set_font("Helvetica", "B", 48)
    pdf.set_y(10)
    pdf.cell(0, 40, "CS50 Shirtificate", align="C")

    pdf.set_font("Helvetica", "B", 24)
    pdf.set_text_color(255, 255, 255)
    pdf.set_y(140)
    pdf.cell(0, 10, f"{name} took CS50", align="C")

    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()
