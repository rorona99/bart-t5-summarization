#data_loader.py loads and prepares the scientific papers for summarization 

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.helpers import clean_text, truncate_text

papers=[
  {
    "id": "paper_01",
    "field": "medicine",
    "title": "Development of mRNA Vaccines and Their Delivery System",
    "url": "https://pubmed.ncbi.nlm.nih.gov/36697236/",
    "abstract": "The rapid development of mRNA vaccines has contributed to the management of the COVID-19 pandemic,suggesting this technology may be used to manage future outbreaks of infectious diseases.",
    "text": """The rapid development of mRNA vaccines has contributed to the management of the current coronavirus disease 2019 (COVID-19) pandemic, suggesting that this technology 
    may be used to manage future outbreaks of infectious diseases. Because the antigens targeted by mRNA vaccines can be easily altered by simply changing the sequence present 
    in the coding region of mRNA structures, it is more appropriate to develop vaccines especially during rapidly developing outbreaks of infectious diseases. In addition to 
    allowing rapid development, mRNA vaccines have great potential in inducing successful antigen-specific immunity by expressing target antigens in cells and simultaneously 
    triggering immune responses."""
  },
  {
    "id": "paper_02",
    "field": "medicine",
    "title": "SARS-CoV-2 mRNA Vaccines: Immunological Mechanism and Beyond",
    "url": "https://pubmed.ncbi.nlm.nih.gov/33673048/",
    "abstract": "To successfully protect against pathogen infection, a vaccine must elicit efficient adaptive immunity, including B and T
    "text": """To successfully protect against pathogen infection, a vaccine must elicit efficient adaptive immunity, including B and T cell responses.
    While B cell responses are key, as they can mediate antibody-dependent protection, T cells can modulate B cell activity and directly contribute to the elimination of pathogen-infected cells.
    mRNA vaccines represent a promising platform for infectious disease prevention due to their ability to rapidly encode any antigen of interest and stimulate both humoral and cellular 
    immune responses."""
  },
  {
    "id": "paper_03",
    "field": "medicine",
    "title": "Molecular Mechanisms of Antibiotic Resistance Revisited",
    "url": "https://pubmed.ncbi.nlm.nih.gov/36411397/",
    "abstract": "Antibiotic resistance is a global health emergency, with resistance detected to all antibiotics currently in clinical use and only a few novel drugs in the pipeline.",
    "text": """Antibiotic resistance is a global health emergency, with resistance detected to all antibiotics currently in clinical use and only a few novel drugs in the pipeline. 
    Understanding the molecular mechanisms that bacteria use to resist the action of antimicrobials is critical to recognize global patterns of resistance and to improve 
    the use of current drugs, as well as for the design of new drugs less susceptible to resistance development and novel strategies to combat resistance. Recent advances in 
    understanding how resistance genes contribute to the biology of the host include new structural details of relevant molecular events underlying resistance."""
  },
  {
    "id": "paper_04",
    "field": "medicine",
    "title": "Global Burden of Bacterial Antimicrobial Resistance in 2019",
    "url": "https://pubmed.ncbi.nlm.nih.gov/35065702/",
    "abstract": "Antimicrobial resistance is a major global health threat causing millions of deaths annually across bacterial pathogens and infection types worldwide.",
    "text": """Antimicrobial resistance is a major cause of death worldwide with the number of deaths attributable to bacterial antimicrobial resistance being substantial across all 
    world regions. The study estimated the global burden of antimicrobial resistance using predictive statistical modelling to produce estimates for all locations. Resistance to 
    antibiotics was found across a wide range of bacterial pathogens and infection types. These findings highlight the need for significant investment in research and development 
    of new antibiotics and alternative treatments as well as improved stewardship of existing antibiotics."""
  },
  {
    "id": "paper_05",
    "field": "biology",
    "title": "CRISPR Technology: A Decade of Genome Editing",
    "url": "https://pubmed.ncbi.nlm.nih.gov/36656942/",
    "abstract": "CRISPR-Cas9 has transformed biological research and medicine over the past decade enabling precise genome editing across a wide range of organisms and applications.",
    "text": """CRISPR-Cas9 has become one of the most powerful tools in biology and medicine since its development as a genome editing platform. The technology allows scientists 
    to make precise changes to DNA sequences in virtually any organism. Applications include correcting disease-causing mutations, engineering disease-resistant crops, 
    developing new model organisms for research, and creating potential therapies for genetic diseases. The past decade has seen rapid expansion of CRISPR tools beyond 
    the original Cas9 system to include base editors, prime editors, and CRISPRi/a systems for gene regulation."""
  },
  {
    "id": "paper_06",
    "field": "biology",
    "title": "CRISPR/Cas9 Gene Editing in Hematological Disorders",
    "url": "https://pubmed.ncbi.nlm.nih.gov/36610813/",
    "abstract": "CRISPR/Cas9 gene editing shows promise for treating hematological disorders by correcting disease-causing mutations in hematopoietic stem and progenitor cells.",
    "text": """Gene therapy using CRISPR/Cas9 has shown promise for treating hematological disorders including sickle cell disease and beta-thalassemia. The approach involves
    editing hematopoietic stem and progenitor cells to correct disease-causing mutations or to reactivate fetal hemoglobin expression. Clinical trials have demonstrated 
    encouraging results with some patients achieving transfusion independence following treatment. Challenges remain in optimizing editing efficiency, minimizing off-target 
    effects, and ensuring long-term engraftment of edited cells."""
  },
  {
    "id": "paper_07",
    "field": "medicine",
    "title": "Memory CD8+ T Cell Diversity Following mRNA Vaccination",
    "url": "https://pubmed.ncbi.nlm.nih.gov/36138186/",
    "abstract": "High responders to mRNA vaccination showed enhanced antibody neutralizing activity and increased frequency of central memory T cells compared to low responders.",
    "text": """Understanding immune responses to SARS-CoV-2 messenger RNA vaccines is important for improving vaccine design and predicting protection. Analysis of B cell and T cell 
    memory programs showed significant variability between individuals classified as high and low responders based on the magnitude of humoral responses. High responders were 
    characterized by enhanced antibody-neutralizing activity, increased frequency of central memory T cells and durable spike-specific CD8+ T cell responses. These 
    findings have implications for personalized vaccination strategies and booster dose timing."""
  },
  {
    "id": "paper_08",
    "field": "medicine",
    "title": "Multidrug-Resistant Bacteria: Mechanisms and Prophylaxis",
    "url": "https://pubmed.ncbi.nlm.nih.gov/36105930/",
    "abstract": "Multidrug resistance in bacteria has become a critical public health concern driven by overuse of antibiotics and limited development of new antimicrobial agents.",
    "text": """In the present scenario, resistance to antibiotics is one of the crucial issues related to public health. Earlier, such resistance was limited to nosocomial infections 
    but it has now become a common phenomenon across community settings. Several factors including extensive development, overexploitation of antibiotics, excessive application 
    of broad-spectrum drugs, and a shortage of target-oriented antimicrobial drugs contribute to this condition. If new drugs are not discovered or formulated, there 
    would be no effective antibiotic available to treat deadly resistant pathogens by 2050. Novel strategies including bacteriophage therapy and antimicrobial peptides are being 
    explored as alternatives."""
  },
  {
    "id": "paper_09",
    "field": "medicine",
    "title": "mRNA Vaccines: Durable Immune Memory to SARS-CoV-2",
    "url": "https://pubmed.ncbi.nlm.nih.gov/34648302/",
    "abstract": "mRNA vaccines induce robust and durable cellular immune memory to SARS-CoV-2 including antibody responses that persist for months after vaccination.",
    "text": """Recall responses to vaccination in individuals with preexisting immunity primarily increased antibody levels without substantially altering antibody decay rates. These 
    findings demonstrate robust cellular immune memory to SARS-CoV-2 following mRNA vaccination. Both spike-specific CD4 and CD8 T cell responses were detectable months 
    after vaccination and memory B cells continued to mature over time. The durability of these responses suggests that mRNA vaccines can provide lasting protection 
    against severe disease even as antibody levels wane."""
  },
  {
    "id": "paper_10",
    "field": "medicine",
    "title": "Antibiotic Resistance: Challenges and Emerging Strategies",
    "url": "https://pubmed.ncbi.nlm.nih.gov/35949048/",
    "abstract": "Antibiotic resistance poses a global health threat requiring new antimicrobial strategies, improved stewardship programs, and international coordination to address rising resistant infections.",
    "text": """Antibiotic resistance has emerged as a major global threat to public health with resistant infections becoming increasingly difficult to treat across all clinical 
    settings. The rise of multidrug-resistant organisms threatens to undermine decades of medical advances including routine surgeries and cancer chemotherapy. Addressing 
    this challenge requires a multifaceted approach including the development of new antimicrobial agents, improved diagnostic tools to guide appropriate antibiotic use, 
    enhanced infection prevention measures, and international coordination on surveillance and stewardship programs. Alternative therapies such as bacteriophages and 
    immunotherapy are also being investigated."""
  }
]

def load_papers():
  """
  Returns the list of clean and prepared papers
  """
  prepared = []
  for paper in papers:
    cleaned = clean_text(paper['text'])
    truncated = truncate_text(cleaned)
    prepared.append({
      'id': paper['id'],
      'field': paper['field'],
      'title': paper['title'],
      'url': paper['url'],
      'abstract': paper['abstract'],
      'input_text': truncated
    })
  print(f'Loaded {len(prepared)} papers successfully!')
  return prepared

if__name__ == '__main__':
  papers_loaded - load_papers()
  for p in papers_loaded:
    print(f'{p['id']} - {p['title']} ({p['field']})')
    print(f'Source: {p['url']}\n')
