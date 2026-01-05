# gdsfactory CLEO 2026 invited paper

![LaTeX](https://img.shields.io/badge/latex-%23008080.svg?style=for-the-badge&logo=latex&logoColor=white)
[![CI/CD](https://github.com/gdsfactory/gdsfactory-paper-cleo26/actions/workflows/latex.yaml/badge.svg)](https://github.com/gdsfactory/gdsfactory-paper-cleo26/actions/workflows/latex.yaml)
[![PDF Shield](https://img.shields.io/badge/click-for%20PDF%20%F0%9F%93%92-lightgrey)](https://github.com/gdsfactory/gdsfactory-paper-cleo26/raw/gh-pages/gdsfactory.pdf)

This repository contains the gdsfactory paper manuscript.
Current template is the one used for Optica Publishing Group.

## Prerequisites

On Debian-based systems:
```bash
sudo apt-get install -y texlive-fonts-extra latexmk
```

## Compilation

Compile using `latexmk`, this should read the config from `.latexmkrc`:
```bash
latexmk
```
