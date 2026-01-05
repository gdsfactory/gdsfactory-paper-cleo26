# LaTeXmk configuration file

# Generate pdf using pdflatex
$pdf_mode = 1;

# only PDF
$dvi_mode = $postscript_mode = 0;

# limit forced runs
$max_repeat = 5;

# Define commands to compile with pdfsync support and nonstopmode
$pdflatex = 'pdflatex -shell-escape -interaction=nonstopmode -synctex=1  -file-line-error %O %S';
$lualatex = 'lualatex -shell-escape -interaction=nonstopmode -synctex=1 -file-line-error %S';
$xelatex = 'xelatex -shell-escape -interaction=nonstopmode -synctex=1  -file-line-error %O %S';
