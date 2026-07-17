# Model Documentation

## TASK
Abstractive sccientific paper summarization using pretrained transformer models

## Models Selected

### BART (facebook/bart-larg-cnn)
- Architecture: Encoder-decoder transformer
- Training approach: Denoising pretraining - learns to reconstruct text from corrupted input
- Why selected: Strong at generating fluent, cohernt summaries of longer documents
- Used as pretrained model, no fine-tuning

### T5 (google/flan-t5-base)
- Architecture: Text-to-Text transformer
- Training approach: Treats every NLP task as text-to-text
- Why selected: Flexible across summarization tasks, good for comparison against BART
- Used as pretrained model, no fine-tuning

## Framework
HuggingFace Transformers library - chosen because it provides easy access to both pretrained models under identical conditions

## Hyperparameters
- max_length: 150 tokens for output
- min_length: 30 tokens for output
- Input truncation: 1024 tokens for BART, 512 for T5

## Evaluation Metrics
- ROGUE Score: measures word and phrase overlap
- BERTScore: measures semantic similarity
