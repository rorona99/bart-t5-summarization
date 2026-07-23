# BART vs T5 Scientific Paper Summarization

## Project Overview
This project compares two pretrained AI summarization models, BART and T5,
on real scientific research papers from PubMed. The goal is to evaluate which model produces more accurate, readable, and useful summaries of scientific text.

## Models Used
- facebook/bart-larg-cnn
- google/flan-t5-base

## Repository Structure
- src/data_loader.py          - Loads and prepares 10 real PubMed papers
- src/model_runner.py         - Runs both models and saves outputs
- utils/helpers.py            - Shared text cleaning and saving functions
- configs/model_config.yaml   - Model hyperparameter settings
- outputs/samples.txt         - Generated summaries from both models
- data/processed/             - Cleaned paper text
- requirements.txt            - Python dependencies
- README.md                   - Project documentatio


## How to Run
1. Clone this repository
2. Install the dependencies: transformers torch datasets rouge-score bert-score pandas
3. Run the model pipeline: python src/model_runner.py

## How it works
1. data_loader.py loads 10 real scientific papers from PubMed across different medicine and biology topics
2. Both BART and T5 summarize eacch paper under identical conditions
3. Outputs are saved to outputs/samples.txt for comparison

## Preliminary Results
During an initial test run on a medical text about mRNA vaccines, BART produced a longer more complete summary capturing 3 key points while T5 produced a shorter summary that cut off early and missed important details. BART appeared to be stronger on medical text in this preliminary test. Full results across all 10 papers are saved in outputs/samples.txt

## Evaluation Metrics
- ROGUE Score: measures word and phrase overlap
- BERTScore: measures semantic similarity

## Known Limiations
- Both models have input token limits so long papers are truncated
- Models were not fine tuned on scientific text
- T5 base model is msaaller than BART large which may affect comparison fairness

## Author
GROUP 11- RUTHIE ORONA - Generative AI
