#This script will load and clean scientific paper text before feeding it into BART and T5 for summarization

import re 
import pandas as pd 

def clean_text(text):
  """
  Cleans raw scientific paper text by removing citations, extra whitespace,
  and special characters
  """

  #Remove the citations like [1], [2,3], (Appleseed et al., 2020)
  text = re.sub(r'\[\d+\]', '', text)
  text = re.sub(r'\(\w+ et al\.,?\s*\d{4}\)', '', text)

  return text

def truncate_text(text, max_words=800):
  """
  Truncates text to fit within model input limits
  """
  words = text.split()
  if len(words) > max_words:
      words =words[:max_words]
  return ' '.join(words)

def prepare_paper(title, abstract, body_text):
  """
  Takes a paper's title, abstract, and body text and returns a cleaned, ready-to-summarize version
  """
  # Clean the text
  cleaned = clean_text(body_text)

  #Truncate to fit model limits 
  truncated = truncate_text(cleaned)

  return{
    "title": title,
    "abstact": abstract,
    "input_text": truncated
  }

#Example usage 
if __name__ = "__main__": 
    sample_title = "Sample Paper Title"
    sample_abstract = "This is the abstract of the paper"
    sample_body = "This is the body text of the paper [1]. It contains citations (Appleseed et al., 2020) and extra   spaces."

    result = prepare_paper(sample_title, sample_abstract, sample_body)
    print('Title:', result['title'])
    print('Input text preview:', result['input_text'][:200])
