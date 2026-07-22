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
  }
]
