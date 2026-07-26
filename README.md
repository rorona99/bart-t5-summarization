# BART vs T5 Scientific Paper Summarization

## Project Overview
This project compares two pretrained AI summarization models, BART and T5,
on real scientific research papers from PubMed. The goal is to evaluate which model produces more accurate, readable, and useful summaries of scientific text.

## Models Used
- facebook/bart-large-cnn
- google/flan-t5-base

## Repository Structure
- src/data_loader.py          - Loads and prepares 10 real PubMed papers
- src/model_runner.py         - Runs both models and saves outputs
- utils/helpers.py            - Shared text cleaning and saving functions
- configs/model_config.yaml   - Model hyperparameter settings
- outputs/samples.txt         - Generated summaries from both models
- outputs/description.txt     - Description of what was generated
- data/processed/             - Cleaned paper text
- requirements.txt            - Python dependencies
- README.md                   - Project documentation


## How to Setup
1. Clone this repository
2. Install the dependencies: transformers torch datasets rouge-score bert-score pandas
3. Run the model pipeline: python src/model_runner.py

## How it works/How to reproduce
1. Install all dependencies listed in requirements.txt
2. Run python src/model_runner.py from the project root
3. The script will automatically load both models from HuggingFace
4. Summaries for all 10 papers will be saved to outputs/samples.txt

## Preliminary Results
After running both models on 25 real PubMed papers covering topics like mRNA vaccines, antibiotic resistance, sickle cell disease, asthma, hypertension, thyroid disorders, and sexually transmitted infections, BART came out ahead on every metric. BART averaged a ROUGE-1 of 0.388, ROUGE-2 of 0.214, and ROUGE-L of 0.332 compared to T5 which scored 0.266, 0.096, and 0.210. The biggest gap was in ROUGE-2 where BART scored more than double T5 — meaning BART did a much better job picking up on the specific phrasing and terminology from the original abstracts. Based on these results BART appears to be the stronger model for scientific and medical text. Full results for all 25 papers are in outputs/rouge_results.txt and outputs/samples.txt.

## Evaluation Metrics
- ROUGE Score: measures word and phrase overlap
- BERTScore: measures semantic similarity

## Known Limitations
- Both models have input token limits so long papers are truncated
- Models were not fine tuned on scientific text
- T5 base model is smaller than BART large which may affect comparison fairness
- Input texts are shortened abstracts and introductions not full papers


## Author
GROUP 11- RUTHIE ORONA - Generative AI
