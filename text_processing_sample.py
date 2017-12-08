"""
Illusstate how to easily debug texfile processing issues.

Problem: You have and issue when processing a file.

Solution: Extract the content that causes the issue to a triple-quotes string
(these are very long string such as the one you are reading)
fix the issue and reuse the exact same instruction
to process your file's content.

Tools : argparse, sys.stdin, generator expression




"""

import argparse
import sys

parser = argparse.ArgumentParser('Process text content or get '
                                 'it from source file')
parser.add_argument('--stdin',
                    help='Fetches input from stdin',
                    action='store_true',
                    )

args = parser.parse_args()
# This allowes us to `cat filepath | python program.py --stdin `

sample_content = """ Hi
Hello
Bonjour
"""

content = sys.stdin.read() if args.stdin else sample_content
'''
 cat  | python text_processing_sample.py --stdin
     end input with ^D (press Control D)
    So that you can copy paste output from file

'''
def strip_lines(input_):
    return (line.strip() for line in input_.split('\n'))

def content_lines(stripped_lines):
    content_lines = (line for line in stripped_lines if line)
    return content_lines

stripped = strip_lines(content)
lines = content_lines(stripped)

# now we do some processing

def process_line(line):
    return line.upper() if line.startswith('Hello') else line

for line in lines:
    print process_line(line)

