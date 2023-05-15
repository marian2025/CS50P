from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        # Rendering logo:
        self.image("shirtificate.png", x=10, y=70, w=190)
        # Setting font:
        self.set_font("helvetica", "B", 40)
        # Printing title:
        self.cell(0, 60, "CS50 Shirtificate", align="C")
        # Performing a line break:
        self.ln(20)


def main():
    name = input("Name: ")
    generate(name)


def generate(name):
    pdf = PDF()
    pdf.add_page()
    pdf.set_font("helvetica", "", 27)
    pdf.set_text_color(255,255,255)
    pdf.cell(0, 213, f"{name} took CS50", align="C")
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()