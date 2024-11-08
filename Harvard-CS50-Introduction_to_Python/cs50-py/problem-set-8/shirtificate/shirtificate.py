
#description: Prompt user for name and create shirt with specific parameters using fpdf2 in an outputfile called "shirtificate.pdf"



#pip install fpdf2

from fpdf import FPDF

def main():

    name = input("Name: ")

    shirt(name)


















#create a shirt using given classes (FPDF) of fpdf2 library
def shirt(name):
    pdf = FPDF()    #orientation by default is portray and format by default is A4 --> could have been specified
    pdf.add_page()
    pdf.set_font("helvetica", "B", 32)
    pdf.cell(0, 40, "CS50 Shirtificate", new_x="LMARGIN", new_y="NEXT", align="C") #in black
    pdf.image("https://cs50.harvard.edu/python/2022/psets/8/shirtificate/shirtificate.png", 30, 60, 150) #insert path for shirt image
    pdf.set_text_color(255) #set text color to white
    pdf.cell(0, 150, f"{name} took CS50", align="C") #in white

    return pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
