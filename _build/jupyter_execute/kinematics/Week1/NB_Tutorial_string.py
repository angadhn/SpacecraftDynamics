#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Strings" data-toc-modified-id="Strings-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Strings</a></span><ul class="toc-item"><li><span><a href="#Conceptual-Definition" data-toc-modified-id="Conceptual-Definition-1.1"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>Conceptual Definition</a></span></li><li><span><a href="#Basics-of-strings" data-toc-modified-id="Basics-of-strings-1.2"><span class="toc-item-num">1.2&nbsp;&nbsp;</span>Basics of strings</a></span></li><li><span><a href="#Basics-of-strings-(contd.)" data-toc-modified-id="Basics-of-strings-(contd.)-1.3"><span class="toc-item-num">1.3&nbsp;&nbsp;</span>Basics of strings (contd.)</a></span></li></ul></li></ul></div>

# # Strings
# 
# ## Conceptual Definition
# Though we usually turn to computers to work with numbers, we can also use them
# to work with alphabets, symbols, and/or numbers- in other words, a sequence of
# various characters that are are formally called _strings_.
# 
# ## Basics of strings
# Python, like most programming languages, can manipulate strings. Strings can
# be enclosed in single quotes (`'...'`) or double quotes (`"..."`) with the
# same result. For example:

# In[1]:


'spam eggs'  # Single quotes.


# If you need to use a quote within the string itself, (e.g., to write words
# involving apostrophes), then do one of the following:

# In[2]:


'doesn\'t'  # Use \' to escape the single quote...


# or

# In[3]:


"doesn't"  # ...or use double quotes instead.


# This use of backslash (`\`) allows one to *escape quotes* for all special
# characters.
# This is sufficient for us to work with [the Vectors Tutorial](NB_Tutorial_Vectors_ReferenceFrames.ipynb).
# 
# ## Basics of strings (contd.)
# In the Jupyter notebooks, the output string is enclosed in quotes. The string is
# enclosed in double quotes
# if the string contains a single quote and no double quotes, otherwise it's
# enclosed in single quotes. The
# [`print()`](https://docs.python.org/3.6/library/functions.html#print) function
# produces a more readable output by omitting the enclosing quotes and by printing
# escaped and special characters:

# In[4]:


'"Isn\'t," she said.'


# In[5]:


print('"Isn\'t," she said.')


# In[6]:


s = 'First line.\nSecond line.'  # \n means newline.
s  # Without print(), \n is included in the output.


# In[7]:


print(s)  # With print(), \n produces a new line.


# If you don't want escaped characters (prefaced by `\`) to be interpreted as
# special characters, use *raw strings* by adding an `r` before the first quote:

# In[8]:


print('C:\some\name')  # Here \n means newline!


# In[9]:


print(r'C:\some\name')  # Note the r before the quote.


# <!--
# String literals can span multiple lines and are delineated by triple-quotes:
# `"""..."""` or `'''...'''`. End of lines are automatically included in the
# string, but it's possible to prevent this by adding a `\` at the end of the
# line. For example, without a `\`, the following example includes an extra line
# at the beginning of the output:

# In[10]:


print("""
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")


# Adding a `\` removes that extra line:

# In[11]:


print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")


# Because Python doesn't provide a means for creating multi-line comments,
# developers often just use triple quotes for this purpose. In a Jupyter notebook,
# however, such quotes define a string literal which appears as the output of a
# code cell:

# In[12]:


"""
Everything between the first three quotes, including new lines,
is part of the multi-line comment. Technically, the Python interpreter
simply sees the comment as a string, and because it's not otherwise
used in code, the string is ignored. Convenient, eh?
"""


# For this reason, it's best in notebooks to use the `#` comment character at the
# beginning of each line, or better still, just use a Markdown cell!
# 
# Strings can be *concatenated* (glued together) with the `+` operator, and
# repeated with `*`:

# In[13]:


# 3 times 'un', followed by 'ium'
3 * 'un' + 'ium'


# Two or more *string literals* (that is, the values enclosed in quotes) placed
# next to each other are automatically concatenated:

# In[14]:


'Py' 'thon'


# Automatic concatenation works only with two literals; it does not work with
# variables or expressions, so the following cell produces an error:

# In[15]:


prefix = 'Py'
prefix 'thon'  # Can't concatenate a variable and a string literal.


# The following cell likewise produces an error:

# In[ ]:


('un' * 3) 'ium'


# To concatenate variables, or a variable and a literal, use `+`:

# In[ ]:


prefix = 'Py'
prefix + 'thon'


# Automatic concatenation is particularly useful when you want to break up long
# strings:

# In[ ]:


text = ('Put several strings within parentheses '
            'to have them joined together.')
text


# Strings can be *indexed* (subscripted), with the first character having index 0.
# There is no separate character type; a character is simply a string of size one:

# In[ ]:


word = 'Python'
word[0]  # Character in position 0.


# In[ ]:


word[5]  # Character in position 5.


# Indices may also be negative numbers, which means to start counting from the end
# of the string. Note that because -0 is the same as 0, negative indices start
# from -1:

# In[ ]:


word[-1]  # Last character.


# In[ ]:


word[-2]  # Second-last character.


# In[ ]:


word[-6]


# In addition to indexing, which extracts individual characters, Python also
# supports *slicing*, which extracts a substring. To slide, you indicate a *range*
# in the format `start:end`, where the start position is included but the end
# position is excluded:

# In[ ]:


word[0:2]  # Characters from position 0 (included) to 2 (excluded).


# In[ ]:


word[2:5]  # Characters from position 2 (included) to 5 (excluded).


# If you omit either position, the default start position is 0 and the default end
# is the length of the string:

# In[ ]:


word[:2]   # Character from the beginning to position 2 (excluded).


# In[ ]:


word[4:]  # Characters from position 4 (included) to the end.


# In[ ]:


word[-2:] # Characters from the second-last (included) to the end.


# This characteristic means that `s[:i] + s[i:]` is always equal to `s`:

# In[ ]:


word[:2] + word[2:]


# In[ ]:


word[:4] + word[4:]


# One way to remember how slices work is to think of the indices as pointing
# between characters, with the left edge of the first character numbered 0. Then
# the right edge of the last character of a string of *n* characters has index
# *n*. For example:
#  +---+---+---+---+---+---+
#  | P | y | t | h | o | n |
#  +---+---+---+---+---+---+
#  0   1   2   3   4   5   6
# -6  -5  -4  -3  -2  -1
# The first row of numbers gives the position of the indices 0...6 in the string;
# the second row gives the corresponding negative indices. The slice from *i* to
# *j* consists of all characters between the edges labeled *i* and *j*,
# respectively.
# 
# For non-negative indices, the length of a slice is the difference of the
# indices, if both are within bounds. For example, the length of `word[1:3]` is 2.
# 
# Attempting to use an index that is too large results in an error:

# In[ ]:


word[42]  # The word only has 6 characters.


# However, when used in a range, an index that's too large defaults to the size of
# the string and does not give an error. This characteristic is useful when you
# always want to slice at a particular index regardless of the length of a string:

# In[ ]:


word[4:42]


# In[ ]:


word[42:]


# Python strings are [immutable](https://docs.python.org/3.5/glossary.html#term-
# immutable), which means they cannot be changed. Therefore, assigning a value to
# an indexed position in a string results in an error:

# In[ ]:


word[0] = 'J'


# The following cell also produces an error:

# In[ ]:


word[2:] = 'py'


# A slice it itself a value that you can concatenate with other values using `+`:

# In[ ]:


'J' + word[1:]


# In[ ]:


word[:2] + 'Py'


# A slice, however, is not a string literal and cannot be used with automatic
# concatenation. The following code produces an error:

# In[ ]:


word[:2] 'Py'    # Slice is not a literal; produces an error


# The built-in function
# [`len()`](https://docs.python.org/3.5/library/functions.html#len) returns the
# length of a string:

# In[ ]:


s = 'supercalifragilisticexpialidocious'
len(s)


# -->
