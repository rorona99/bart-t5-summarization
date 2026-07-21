#helpers.py; utility funtions used across the project

import re
import os

def clean_text(text):
  """
  Cleans raw scientific paper text by removing citations, extra whitespace, and special characters
  """

#Removes in line numerical citions like [1], [2,3]
text = re.sub(r'\[\d+\]', '', text)

#Removes in line "full" citations like (Appleseed et al., 2020)
text = re.sub(r'\(\w+ et al\.,?\s*\d{4}\)', '', text)

#Removes extra whitespace and new lines
text = re.sub(r'\s+', ' ', text)
text = text.strip()

return text


def truncate_text(text, max_words = 800):
  """
  Truncates text to fit within model input limits
  """
  words = text.split()
  if len(words) > max_words:
    words = words[:max_words]
  return ' '.join(words)

def save_output(content, filename, output_dir = "outputs/"):
  """
  Saves generated summaries to the outputs folder
  """

#Creates output folders if they dont already exist

os.makedirs(output_dir, exist_ok=True)

filepath = os.path.join(output_dir, filename)
with open(filepath, 'w') as f:
  f.write(content)

print(f"Output saved to {filepath}")
return filepath
