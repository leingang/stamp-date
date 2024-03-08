# Stamp Class Dates on Files

I print a class roster every day and use it to take attendance and record small todos.

It seemed like a nice idea to stamp the class date on the PDF. And then it
snowballed into this package.

## Installation

    pipx ensurepath
    pipx install --editable .

## Usage

    stamp-date --calendar <iCal source> input.pdf

## Printing

I do this by lpr so that I can get them stapled at the same time.

But because of spaces in file names this can be tricky.

See https://stackoverflow.com/questions/1806868/linux-replacing-spaces-in-the-file-names