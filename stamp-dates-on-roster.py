import PyPDF2

def stamp_text(input_pdf, output_pdf, stamp_text):
    # Open the input PDF file
    with open(input_pdf, 'rb') as file:
        # Create a PDF reader object
        pdf_reader = PyPDF2.PdfFileReader(file)
        
        # Create a PDF writer object
        pdf_writer = PyPDF2.PdfFileWriter()
        
        # Iterate through each page in the input PDF
        for page_num in range(pdf_reader.numPages):
            # Get the page
            page = pdf_reader.getPage(page_num)
            
            # Create a watermark object
            watermark = PyPDF2.PageObject.createBlankPage(width=page.mediaBox.getWidth(), height=page.mediaBox.getHeight())
            
            # Create a PDF font object for the watermark text
            font = PyPDF2.pdf.ContentStream([font.encode('latin1') for font in '/F1 12 Tf 0 g 0 0 Td']).getObject()
            
            # Set the font and text for the watermark
            watermark._content.append(font)
            watermark._content.append(PyPDF2.pdf.TextStringObject(stamp_text))
            
            # Merge the page and watermark
            stamped_page = page.mergePage(watermark)
            
            # Add the stamped page to the PDF writer
            pdf_writer.addPage(stamped_page)
        
        # Write the output PDF file
        with open(output_pdf, 'wb') as output_file:
            pdf_writer.write(output_file)

if __name__ == "__main__":
    # Replace 'input.pdf' with the path to your input PDF file
    input_pdf_path = 'input.pdf'
    
    # Replace 'output.pdf' with the desired output PDF file path
    output_pdf_path = 'output.pdf'
    
    # Replace 'Your Text Here' with the text you want to stamp on each page
    stamp_text_value = 'Your Text Here'
    
    # Call the stamp_text function
    stamp_text(input_pdf_path, output_pdf_path, stamp_text_value)

    print(f"Text stamped successfully. Output PDF saved at: {output_pdf_path}")
