import os
import platform
import subprocess
import sys

def make_file(suffix, *args):
    sys.stderr.write("generating %s file ...\n" % (suffix))
    args = ['pandoc', '--output=artefact/Inframodel_DRAFT.' + suffix] + list(args)
    # sys.stderr.write(" \\\n    ".join(args) + "\n")
    subprocess.call(args)

common_args = ['--from=markdown+escaped_line_breaks+hard_line_breaks', '--filter=pandoc-xnos', '--number-sections', '--table-of-contents' ]

latex_args = ['--variable=block-headings']
for latex_file in ["default", "disable_float", "fignos"]:
    latex_args.append("--include-in-header=%s.latex" % (latex_file))

template_file = 'template.latex'
if os.path.exists(template_file):
    latex_args.append("--template=%s" % (template_file))

word_args = ['--reference-doc=word-template.docx']

make_file("pdf" , *common_args, *latex_args, 'staging/InfraModel.md')
make_file("docx", *common_args, *word_args , 'staging/InfraModel.md')