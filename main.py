import csv
from PyPDF2 import PdfFileWriter, PdfFileReader
import os


page_num_off = 0
page_num_agreement = 0

offer_letter = open('new_rc_offer.pdf','rb')
agreement_letter = open('new_rc_agree.pdf','rb')

offer_reader = PdfFileReader(offer_letter)
agreement_reader = PdfFileReader(agreement_letter)

applicants = open('./rc.csv',encoding="utf-8")
read_applicants = csv.reader(applicants)
# might implement a generator later
data = list(read_applicants)

print(data.pop(0))
print(len(data))


def create_offer(n, c):
    global page_num_off

    pdf_writer = PdfFileWriter()
    page = offer_reader.getPage(page_num_off)
    pdf_writer.addPage(page)
    page_num_off += 1
    return pdf_writer


def create_agreement(n, c):
    global page_num_agreement

    pdf_writer = PdfFileWriter()
    for i in range(0, 3):
        page = agreement_reader.getPage(page_num_agreement)
        pdf_writer.addPage(page)
        page_num_agreement += 1
    return pdf_writer


def create_dir(name, country):
    ofile_name = "Offer Letter for "
    afile_name = "Agreement for "

    os.mkdir(name)
    os.chdir('./'+name)

    offer = create_offer(name, country)
    agreement = create_agreement(name, country)
    output_offer = open(ofile_name+name+".pdf",'wb')
    output_agreement = open(afile_name+name+".pdf","wb")
    offer.write(output_offer)
    agreement.write(output_agreement)
    os.chdir('..')


os.chdir('a')
for n, country in data:
    # take that name extract three pages of the pdf and save the pdf using the name file
    create_dir(n, country)

offer_letter.close()
agreement_letter.close()
applicants.close()

