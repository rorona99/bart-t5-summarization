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
- outputs/description.txt     - Description of what was generated
- data/processed/             - Cleaned paper text
- requirements.txt            - Python dependencies
- README.md                   - Project documentatio


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
In an initial test on a medical text about mRNA vaccines, BART produced a 
longer and more complete summary that captured 3 key points from the original. 
T5 produced a shorter summary that cut off early and missed important details 
like the immune response and how mRNA breaks down. Based on this early test 
BART appears stronger on medical and scientific text. Full results for all 
10 papers are saved in outputs/samples.txt.

## Evaluation Metrics
- ROGUE Score: measures word and phrase overlap
- BERTScore: measures semantic similarity

## Known Limiations
- Both models have input token limits so long papers are truncated
- Models were not fine tuned on scientific text
- T5 base model is smaller than BART large which may affect comparison fairness
- Input texts are shortened abstracts and introductions not full papers


## Author
GROUP 11- RUTHIE ORONA - Generative AI
