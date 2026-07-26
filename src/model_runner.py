import os

def save_output(content, filename, output_dir="outputs/"):
    os.makedirs(output_dir, exist_ok=True)
    filepath = os.path.join(output_dir, filename)
    with open(filepath, 'w') as f:
        f.write(content)
    print(f"Output saved to {filepath}")
    return filepath

def summarize_bart(text, tokenizer, model):
    inputs = tokenizer(text, return_tensors="pt", max_length=1024, truncation=True)
    output = model.generate(**inputs, max_length=150, min_length=30)
    return tokenizer.decode(output[0], skip_special_tokens=True)

def summarize_t5(text, tokenizer, model):
    input_text = "summarize: " + text
    inputs = tokenizer(input_text, return_tensors="pt", max_length=512, truncation=True)
    output = model.generate(**inputs, max_length=150, min_length=30)
    return tokenizer.decode(output[0], skip_special_tokens=True)

def run_pipeline(bart_tokenizer, bart_model, t5_tokenizer, t5_model, papers):
    results = []
    output_text = "BART vs T5 Summarization Results\n"
    output_text += "=" * 60 + "\n\n"

    for paper in papers:
        print(f"\nProcessing: {paper['title']}...")
        bart_summary = summarize_bart(paper["input_text"], bart_tokenizer, bart_model)
        t5_summary = summarize_t5(paper["input_text"], t5_tokenizer, t5_model)

        results.append({
            "id": paper["id"],
            "title": paper["title"],
            "field": paper["field"],
            "url": paper["url"],
            "reference_abstract": paper["abstract"],
            "bart_summary": bart_summary,
            "t5_summary": t5_summary
        })

        output_text += f"Paper: {paper['title']}\n"
        output_text += f"Field: {paper['field']}\n"
        output_text += f"Source: {paper['url']}\n"
        output_text += f"Reference Abstract: {paper['abstract']}\n"
        output_text += f"BART Summary: {bart_summary}\n"
        output_text += f"T5 Summary: {t5_summary}\n"
        output_text += "-" * 60 + "\n\n"

        print(f"BART: {bart_summary[:100]}...")
        print(f"T5:   {t5_summary[:100]}...")

    save_output(output_text, "samples.txt")
    print("\nAll done! Results saved to outputs/samples.txt")
    return results

#Run the pipline
run_pipeline(bart_tokenizer, bart_model, t5_tokenizer, t5_model, papers_loaded)

if __name__ == "__main__":
    run_pipeline()
