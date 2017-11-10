
# Getting help when debugging text processing.

This will help you getting help when debugging and maybe you'll learn some
cool python features

## Please provide self contained example

In many cases I can see such question on stackoveflow or other websites:

    Hey i have a problem with the following code which does not work:

    file = open('somefile')
    for line in file:
        if foo:
            if bar:
                do_something(line)

In most cases the corresponding file is not provided. This lead other users to read
the code and guessing why this would not work.

```python

rawfile_content = """
Python easyly supports muttiline string
This is pretty cool  isn't it ?
"""

lines = rawfile_content.split()
#lines = open('somefile').readlines() # Others will comment this line

# Strip empty lines

lines = [line.strip() for line in lines if line.strip()]

```

so then you can simply do the following:

```python
for line in lines:
    do_stuff(line)
```

This may look superfluous but your code is processing the file's content
not the file's name.
