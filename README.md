# Stamp Class Dates on PDFs

I print a class roster every day and use it to take attendance and record small todos.

It seemed like a nice idea to stamp the class date on the PDF. And then it
snowballed into this package.

## Installation

[pipx](https://pipx.pypa.io/) installs its own virtual environment, but also a
script in the user's `PATH`.

    pipx ensurepath
    pipx install --editable .

The virtual environment is created in `~/Library/Application Support/pipx/venvs/stamp-date`. 
An alias to the script is placed in `~/.local/bin`.

## Usage

    stamp-date --calendar <iCal source> input.pdf

Use `stamp-date --help` for more information.

## Printing

To avoid the Pharos system, I normally pipe a file via ssh to the `cims` server
and run `lpr`. But with several files that would require me to login/do
multifactor authentication each time.

To workaround the first, I `scp` the files to `cims`. But looping over many
files in `tcsh` with spaces in their names was tricky. I suggest to myself to
[rename the files](https://stackoverflow.com/q/1806868/297797) before printing.