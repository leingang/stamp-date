from pathlib import Path
from typing import List, Union

from pypdf import PdfReader, PdfWriter, Transformation

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib.units import inch
from reportlab.lib import colors


def make_stamp(text: str, path: str):
    c = canvas.Canvas(path, pagesize=landscape(letter))
    c.translate(inch, inch)
    c.setFillColorRGB(137, 0, 225)
    c.setFont("Helvetica", 12)
    # c.rotate(45)
    c.drawString(-0.5 * inch, 0, text)
    c.save()


def stamp(
    content_pdf: Union[Path, str],
    stamp_pdf: Union[Path, str],
    pdf_result: Union[Path, str],
    page_indices: Union[None, List[int]] = None,
):
    stamp_page = PdfReader(stamp_pdf).pages[0]

    writer = PdfWriter()
    # page_indices can be a List(array) of page, tuples are for range definition
    reader = PdfReader(content_pdf)
    writer.append(reader, pages=page_indices)

    for content_page in writer.pages:
        content_page.merge_transformed_page(
            stamp_page,
            Transformation().scale(1),
        )

    writer.write(pdf_result)
