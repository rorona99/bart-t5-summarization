import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.helpers import load_papers
from utils.helpers import clean_text, save_output
from transformers import BartForConditionalGeneration, BartTokenizer
from transfromers import T5ForConditionalGeneration, T5Tokenizer

def load_models():
  """
  Loads both BART and T5 pretrained models
  """
  print("Loading BART...")
  bart_tokenizer = BartTokenizer.from_pretrained("facebook/bart-large-cnn")
  bart_model = BartForConditionalGeneration.from_pretrained("facebook/bart-large-cnn")
  print("BART loaded!")

  print("Loading T5...")
  t5_tokenizer = T5Tokenizer.from_pretrained("google/flan-t5-base")
  t5_model = T5ForConditionalGeneration.from_pretrained("google/flan-t5-base")
  print("T5 loaded!")

  return bart_tokenizer, bart_model, t5_tokenizer, t5_model

def summarize_bart(text, tokenizer, model):
  """
  Generates a summary using BART
  """
  inputs = tokenizer(
    text,
    return_tensors="pt",
    max_length=1024,
    truncation=True
  )
  output = model.generate(
    **inputs,
    max_length = 150,
    min_length = 30 
  )
  return tokenzier.decode(output[0], skip_special_tokens = True)

def summarize_t5(text, tokenizer, model):
  """
  Generates a summary using T5
  """
  input_text = 'summarize: ' + text
  inputs = tokenizer(
    input_text,
    return_tensors = 'pt',
    max_length = 512,
    truncation = True
  )
  output = model.generate(
    **inputs, 
    max_length = 150,
    min_length = 30
  )
  return tokenizer.decode(output[0], skip_special_tokens = True)

def run_pipeline():
  """
  Main pipeline loads models, runs on all papers, saves outputs
  """

#load the models
bart_tokenizer, bart_model, t5_tokenizer, t5_model = load_models()

#load the papers
papers = load_papers()

#store the results
results = []
output_text = 'BART vs T5 Summarization Results\n'
output_text += '=' * 60 + '\n\n'


for paper in papers:
  print(f'\nProcessing: {paper['title']}...')

#generate summaries
  bart_summary = summarize_bart(
    paper["input_text"],
    bart_tokenizer,
    bart_model
    )
  t5_summary = summarize_t5(
    paper["input_text"],
    t5_tokenizer,
    t5_model
    )

#store the result
  results.append({
    "id": paper["id"],
    "title": paper["title"],
    "field": paper["field"],
    "url": paper["url"],
    "reference_abstract": paper["abstract"],
    "bart_summary": bart_summary,
    "t5_summary": t5_summary
  })

#add to output text 
  output_text += f"Paper: {paper['title']}\n"
  output_text += f"Field: {paper['field']}\n"
  output_text += f"Source: {paper['url']}\n"
  output_text += f"Reference Abstract: {paper['abstract']}\n"
  output_text += f"BART Summary: {bart_summary}\n"
  output_text += f"T5 Summary: {t5_summary}\n"
  output_text += "-" * 60 + "\n\n"

    print(f"BART: {bart_summary[:100]}...")
    print(f"T5:   {t5_summary[:100]}...")

#save outputs to file 
  save_output(output_text, "samples.txt")
  print("\nAll done! Results saved to outputs/samples.txt")

  return results

if __name__ == "__main__":
    run_pipeline()
