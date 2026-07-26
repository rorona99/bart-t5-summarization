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
    "text": "The rapid development of mRNA vaccines has contributed to the management of the current coronavirus disease 2019 (COVID-19) pandemic, suggesting that this technology 
    may be used to manage future outbreaks of infectious diseases. Because the antigens targeted by mRNA vaccines can be easily altered by simply changing the sequence present 
    in the coding region of mRNA structures, it is more appropriate to develop vaccines especially during rapidly developing outbreaks of infectious diseases. In addition to 
    allowing rapid development, mRNA vaccines have great potential in inducing successful antigen-specific immunity by expressing target antigens in cells and simultaneously 
    triggering immune responses."
  },
  {
    "id": "paper_02",
    "field": "medicine",
    "title": "SARS-CoV-2 mRNA Vaccines: Immunological Mechanism and Beyond",
    "url": "https://pubmed.ncbi.nlm.nih.gov/33673048/",
    "abstract": "To successfully protect against pathogen infection, a vaccine must elicit efficient adaptive immunity, including B and T cell responses.",
    "text": "To successfully protect against pathogen infection, a vaccine must elicit efficient adaptive immunity, including B and T cell responses.
    While B cell responses are key, as they can mediate antibody-dependent protection, T cells can modulate B cell activity and directly contribute to the elimination of pathogen-infected cells.
    mRNA vaccines represent a promising platform for infectious disease prevention due to their ability to rapidly encode any antigen of interest and stimulate both humoral and cellular 
    immune responses."
  },
  {
    "id": "paper_03",
    "field": "medicine",
    "title": "Molecular Mechanisms of Antibiotic Resistance Revisited",
    "url": "https://pubmed.ncbi.nlm.nih.gov/36411397/",
    "abstract": "Antibiotic resistance is a global health emergency, with resistance detected to all antibiotics currently in clinical use and only a few novel drugs in the pipeline.",
    "text": "Antibiotic resistance is a global health emergency, with resistance detected to all antibiotics currently in clinical use and only a few novel drugs in the pipeline. 
    Understanding the molecular mechanisms that bacteria use to resist the action of antimicrobials is critical to recognize global patterns of resistance and to improve 
    the use of current drugs, as well as for the design of new drugs less susceptible to resistance development and novel strategies to combat resistance. Recent advances in 
    understanding how resistance genes contribute to the biology of the host include new structural details of relevant molecular events underlying resistance."
  },
  {
    "id": "paper_04",
    "field": "medicine",
    "title": "Global Burden of Bacterial Antimicrobial Resistance in 2019",
    "url": "https://pubmed.ncbi.nlm.nih.gov/35065702/",
    "abstract": "Antimicrobial resistance is a major global health threat causing millions of deaths annually across bacterial pathogens and infection types worldwide.",
    "text": "Antimicrobial resistance is a major cause of death worldwide with the number of deaths attributable to bacterial antimicrobial resistance being substantial across all 
    world regions. The study estimated the global burden of antimicrobial resistance using predictive statistical modelling to produce estimates for all locations. Resistance to 
    antibiotics was found across a wide range of bacterial pathogens and infection types. These findings highlight the need for significant investment in research and development 
    of new antibiotics and alternative treatments as well as improved stewardship of existing antibiotics."
  },
  {
    "id": "paper_05",
    "field": "biology",
    "title": "CRISPR Technology: A Decade of Genome Editing",
    "url": "https://pubmed.ncbi.nlm.nih.gov/36656942/",
    "abstract": "CRISPR-Cas9 has transformed biological research and medicine over the past decade enabling precise genome editing across a wide range of organisms and applications.",
    "text": "CRISPR-Cas9 has become one of the most powerful tools in biology and medicine since its development as a genome editing platform. The technology allows scientists 
    to make precise changes to DNA sequences in virtually any organism. Applications include correcting disease-causing mutations, engineering disease-resistant crops, 
    developing new model organisms for research, and creating potential therapies for genetic diseases. The past decade has seen rapid expansion of CRISPR tools beyond 
    the original Cas9 system to include base editors, prime editors, and CRISPRi/a systems for gene regulation."
  },
  {
    "id": "paper_06",
    "field": "biology",
    "title": "CRISPR/Cas9 Gene Editing in Hematological Disorders",
    "url": "https://pubmed.ncbi.nlm.nih.gov/36610813/",
    "abstract": "CRISPR/Cas9 gene editing shows promise for treating hematological disorders by correcting disease-causing mutations in hematopoietic stem and progenitor cells.",
    "text": "Gene therapy using CRISPR/Cas9 has shown promise for treating hematological disorders including sickle cell disease and beta-thalassemia. The approach involves
    editing hematopoietic stem and progenitor cells to correct disease-causing mutations or to reactivate fetal hemoglobin expression. Clinical trials have demonstrated 
    encouraging results with some patients achieving transfusion independence following treatment. Challenges remain in optimizing editing efficiency, minimizing off-target 
    effects, and ensuring long-term engraftment of edited cells."
  },
  {
    "id": "paper_07",
    "field": "medicine",
    "title": "Memory CD8+ T Cell Diversity Following mRNA Vaccination",
    "url": "https://pubmed.ncbi.nlm.nih.gov/36138186/",
    "abstract": "High responders to mRNA vaccination showed enhanced antibody neutralizing activity and increased frequency of central memory T cells compared to low responders.",
    "text": "Understanding immune responses to SARS-CoV-2 messenger RNA vaccines is important for improving vaccine design and predicting protection. Analysis of B cell and T cell 
    memory programs showed significant variability between individuals classified as high and low responders based on the magnitude of humoral responses. High responders were 
    characterized by enhanced antibody-neutralizing activity, increased frequency of central memory T cells and durable spike-specific CD8+ T cell responses. These 
    findings have implications for personalized vaccination strategies and booster dose timing."
  },
  {
    "id": "paper_08",
    "field": "medicine",
    "title": "Multidrug-Resistant Bacteria: Mechanisms and Prophylaxis",
    "url": "https://pubmed.ncbi.nlm.nih.gov/36105930/",
    "abstract": "Multidrug resistance in bacteria has become a critical public health concern driven by overuse of antibiotics and limited development of new antimicrobial agents.",
    "text": "In the present scenario, resistance to antibiotics is one of the crucial issues related to public health. Earlier, such resistance was limited to nosocomial infections 
    but it has now become a common phenomenon across community settings. Several factors including extensive development, overexploitation of antibiotics, excessive application 
    of broad-spectrum drugs, and a shortage of target-oriented antimicrobial drugs contribute to this condition. If new drugs are not discovered or formulated, there 
    would be no effective antibiotic available to treat deadly resistant pathogens by 2050. Novel strategies including bacteriophage therapy and antimicrobial peptides are being 
    explored as alternatives."
  },
  {
    "id": "paper_09",
    "field": "medicine",
    "title": "mRNA Vaccines: Durable Immune Memory to SARS-CoV-2",
    "url": "https://pubmed.ncbi.nlm.nih.gov/34648302/",
    "abstract": "mRNA vaccines induce robust and durable cellular immune memory to SARS-CoV-2 including antibody responses that persist for months after vaccination.",
    "text": "Recall responses to vaccination in individuals with preexisting immunity primarily increased antibody levels without substantially altering antibody decay rates. These 
    findings demonstrate robust cellular immune memory to SARS-CoV-2 following mRNA vaccination. Both spike-specific CD4 and CD8 T cell responses were detectable months 
    after vaccination and memory B cells continued to mature over time. The durability of these responses suggests that mRNA vaccines can provide lasting protection 
    against severe disease even as antibody levels wane."
  },
  {
    "id": "paper_10",
    "field": "medicine",
    "title": "Antibiotic Resistance: Challenges and Emerging Strategies",
    "url": "https://pubmed.ncbi.nlm.nih.gov/35949048/",
    "abstract": "Antibiotic resistance poses a global health threat requiring new antimicrobial strategies, improved stewardship programs, and international coordination to address rising resistant infections.",
    "text": "Antibiotic resistance has emerged as a major global threat to public health with resistant infections becoming increasingly difficult to treat across all clinical 
    settings. The rise of multidrug-resistant organisms threatens to undermine decades of medical advances including routine surgeries and cancer chemotherapy. Addressing 
    this challenge requires a multifaceted approach including the development of new antimicrobial agents, improved diagnostic tools to guide appropriate antibiotic use, 
    enhanced infection prevention measures, and international coordination on surveillance and stewardship programs. Alternative therapies such as bacteriophages and 
    immunotherapy are also being investigated."
  },
  {
        "id": "paper_11",
        "field": "medicine",
        "title": "Asthma Medications and Management",
        "url": "https://pubmed.ncbi.nlm.nih.gov/30285350/",
        "abstract": "Asthma is a chronic inflammatory illness impacting millions daily treated with beta-2 agonists inhaled corticosteroids and other medications to improve symptoms and reduce exacerbations.",
        "text": "Asthma is a wide-reaching chronic inflammatory illness that impacts millions of people daily. It is frequently responsible for unscheduled healthcare usage missed school 
        and workdays. It is an inappropriate immune response to a triggering factor that induces bronchial hyperreactivity constriction with remodeling of smooth muscle and increased 
        mucous secretion into the airways. Several classifications of medications are utilized to treat and manage chronic asthma to improve symptoms and reduce exacerbations 
        including beta-2 agonists anticholinergics and inhaled corticosteroids."
    },
    {
        "id": "paper_12",
        "field": "medicine",
        "title": "Asthma Management in Adults",
        "url": "https://pubmed.ncbi.nlm.nih.gov/36283607/",
        "abstract": "Management of asthma in adults has advanced significantly with new biologics and clarification of type 2 airway inflammation mechanisms improving treatment for severe asthma.",
        "text": "Management of asthma in adults has advanced in the past 10 years. Central to these advances has been further clarification of type 2 mechanisms of 
        airway inflammation and utilization of biomarkers including eosinophils and fractional exhaled nitric oxide. Five new biologics were approved to join 
        omalizumab and revolutionize severe asthma treatment. These biologics significantly prevent exacerbations and spare systemic corticosteroids use and their 
        side effects. Guidelines support the effectiveness of inhaled corticosteroids with long-acting beta agonists for both maintenance and rescue therapy."
    },
    {
        "id": "paper_13",
        "field": "medicine",
        "title": "Advances in the Diagnosis and Treatment of Sickle Cell Disease",
        "url": "https://pubmed.ncbi.nlm.nih.gov/35241123/",
        "abstract": "Sickle cell disease affects approximately 100000 individuals in the USA and is caused by mutations in the beta globin gene resulting in chronic hemolysis vaso-occlusion and significant disease morbidity.",
        "text": "Sickle cell disease affects approximately 100000 individuals in the USA and more than 3 million worldwide and is caused by mutations in the beta globin 
        gene that result in sickle hemoglobin production. Sickle hemoglobin polymerization leads to red blood cell sickling chronic hemolysis and vaso-occlusion. Acute and 
        chronic pain as well as end-organ damage occur throughout the lifespan of individuals living with sickle cell disease resulting in significant morbidity and a median 
        life expectancy of 43 years in the USA. Recent advances in treatment include gene therapy hydroxyurea and novel disease modifying agents."
    },
    {
        "id": "paper_14",
        "field": "medicine",
        "title": "Development of Curative Therapies for Sickle Cell Disease",
        "url": "https://pubmed.ncbi.nlm.nih.gov/36507504/",
        "abstract": "Disease modifying therapies such as hydroxyurea L-glutamine voxelotor and crizanlizumab reduce pain crises while gene therapy represents an emerging curative approach for sickle cell disease.",
        "text": "Recent advances in managing sickle cell disease have significantly improved patient survival and quality of life. Disease modifying drug therapies such as 
        hydroxyurea L-glutamine voxelotor and crizanlizumab reduce pain crises and severe complications. Allogeneic hematopoietic stem cell transplantation using matched sibling
        donors is currently the only standard curative option however only a small proportion of patients have such donors. Gene therapy approaches using lentiviral vectors and CRISPR 
        gene editing are emerging as promising curative strategies for a broader population of patients."
    },
    {
        "id": "paper_15",
        "field": "medicine",
        "title": "Updates in Hypertension: New Trials and Treatment Targets",
        "url": "https://pubmed.ncbi.nlm.nih.gov/35249970/",
        "abstract": "Recent trials support intensive blood pressure lowering to 110-130 mmHg in older patients and identify new pharmacological strategies to improve hypertension management.",
        "text": "Several recent trials and observational studies have identified critical areas that can help to improve the management and measurement of blood pressure in patients 
        with hypertension. High quality trial evidence supports intensive systolic blood pressure lowering to 110-130 mmHg in older patients and potassium based salt substitution in 
        patients without chronic kidney disease. New pharmacological approaches to treat resistant hypertension are being developed and the optimal timing of antihypertensive medication 
        intake is being studied. Device based approaches including renal denervation are also being evaluated for resistant hypertension."
    },
    {
        "id": "paper_16",
        "field": "medicine",
        "title": "WHO Guideline for Pharmacological Treatment of Hypertension",
        "url": "https://pubmed.ncbi.nlm.nih.gov/34775787/",
        "abstract": "The World Health Organization guideline provides evidence based recommendations for pharmacological treatment of hypertension in adults to reduce cardiovascular disease risk globally.",
        "text": "Hypertension is one of the leading causes of cardiovascular disease morbidity and mortality worldwide. The World Health Organization guideline on pharmacological treatment 
        of hypertension in adults provides recommendations based on systematic reviews of evidence. First line antihypertensive agents include thiazide diuretics calcium channel blockers 
        ACE inhibitors and angiotensin receptor blockers. The guideline emphasizes the importance of lifestyle modifications alongside pharmacological treatment and the need for regular 
        monitoring of blood pressure control and treatment adherence."
    },
    {
        "id": "paper_17",
        "field": "medicine",
        "title": "Hypothyroidism: Diagnosis and Evidence-Based Treatment",
        "url": "https://pubmed.ncbi.nlm.nih.gov/35384263/",
        "abstract": "Hypothyroidism affects up to 5 percent of the global population and is managed primarily with levothyroxine replacement therapy guided by thyroid stimulating hormone levels.",
        "text": "Hypothyroidism affects up to 5 percent of the global population. Incidence increases with age and is more common in women. Symptoms can develop slowly and often mimic symptoms 
        of other disorders including menstrual cycle abnormalities. Diagnosis relies on testing of thyroid stimulating hormone levels and confirmation with thyroxine levels. Management of hypothyroidism 
        usually involves monotherapy with levothyroxine taken on an empty stomach. Outpatient primary care clinicians can use shared decision making to determine the best initiation method for each individual patient."
    },
    {
        "id": "paper_18",
        "field": "medicine",
        "title": "Evaluating Health Outcomes in the Treatment of Hypothyroidism",
        "url": "https://pubmed.ncbi.nlm.nih.gov/36329885/",
        "abstract": "Clinical hypothyroidism requires lifelong thyroid hormone replacement with the primary goal of restoring normal thyroid function as measured by thyrotropin levels.",
        "text": "Clinical hypothyroidism is defined by the inadequate production of thyroid hormone from the thyroid gland to maintain normal organ system functions. For nearly all patients 
        with clinical hypothyroidism lifelong treatment with thyroid hormone replacement is required. The primary goal of treatment is to provide the appropriate daily dose of thyroid hormone 
        to restore normal thyroid function for each individual patient. In current clinical practice normalization of thyrotropin level is the primary measure of effectiveness of treatment however 
        the use of a single biomarker to define adequate thyroid hormone replacement is being reevaluated."
    },
    {
        "id": "paper_19",
        "field": "medicine",
        "title": "Management and Metabolic Characterization of Hyperthyroidism and Hypothyroidism",
        "url": "https://pubmed.ncbi.nlm.nih.gov/36455479/",
        "abstract": "Hyperthyroidism and hypothyroidism are common thyroid disorders with traditional treatments including hormone replacement for hypothyroidism and antithyroid drugs radioiodine or surgery for hyperthyroidism.",
        "text": "Hyperthyroidism and hypothyroidism are common diseases resulting from thyroid dysfunction and are simple to diagnose and treat. The traditional treatment for hypothyroidism is 
        thyroid hormone replacement therapy. The traditional treatments for hyperthyroidism include antithyroid drugs iodine radiotherapy and surgery. Current statistical reference ranges used for 
        diagnosis have been debated and insufficient treatment can result in long-term thyroid hormone deficiency associated with increased risk of cardiovascular disease. Overtreatment can result 
        in heart disease and osteoporosis particularly in older people and pregnant women."
    },
    {
        "id": "paper_20",
        "field": "medicine",
        "title": "Updated Sexually Transmitted Infections Guidelines",
        "url": "https://pubmed.ncbi.nlm.nih.gov/37427972/",
        "abstract": "Growing antimicrobial resistance in gonorrhea and chlamydia has driven the need to update STI treatment guidelines particularly among adolescents and young adults to prevent treatment failure.",
        "text": "One of the most persistent public health concerns continues to be sexually transmitted infections and their consequences. A large portion of sexually transmitted infections occur in 
        adolescents and young adults with serious consequences such as infertility and systemic disease. There has been growing evidence for antimicrobial resistance in strains of gonorrhea and chlamydia 
        which has provided the need to update treatment guidelines to prevent continued resistance and decrease the rate of treatment failure. Public health and clinical level initiatives must focus on 
        prevention screening and appropriate treatment in high risk populations."
    },
    {
        "id": "paper_21",
        "field": "medicine",
        "title": "Diagnosis and Treatment of Sexually Transmitted Infections: A Review",
        "url": "https://pubmed.ncbi.nlm.nih.gov/35015033/",
        "abstract": "Sexually transmitted infections including chlamydia gonorrhea syphilis herpes and HPV require accurate diagnosis and appropriate treatment to prevent serious complications and transmission.",
        "text": "Sexually transmitted infections including chlamydia gonorrhea syphilis herpes simplex virus and human papillomavirus are among the most common infectious diseases worldwide. Accurate 
        diagnosis using nucleic acid amplification tests is the standard of care for chlamydia and gonorrhea. Treatment regimens vary by pathogen and must account for increasing antimicrobial resistance 
        patterns particularly for gonorrhea. Partner notification and treatment are essential components of sexually transmitted infection management to prevent reinfection and reduce community transmission. 
        Screening programs targeting high risk populations remain a key public health strategy."
    },
    {
        "id": "paper_22",
        "field": "medicine",
        "title": "Asthma Clinical Trials Update 2023",
        "url": "https://pubmed.ncbi.nlm.nih.gov/36243545/",
        "abstract": "Asthma is a significant worldwide health issue with biologics now available to treat severe type 2 high asthma while treatment of type 2 low asthma remains a clinical challenge.",
        "text": "Asthma is a complex heterogeneous chronic airway disease with high prevalence of uncontrolled disease. New therapies including biologics are now available to treat type 2 high asthma 
        characterized by eosinophilic inflammation. Treatment of type 2 low asthma remains a challenge with limited effective therapeutic options. Biologics have shown promising results and the potential 
        for changing the treatment of uncontrolled asthma. Optimizing standard therapy with biologics is needed to decrease asthma related morbidity and improve patient quality of life."
    },
    {
        "id": "paper_23",
        "field": "medicine",
        "title": "Sickle Cell Disease in the New Era: Advances in Drug Treatment",
        "url": "https://pubmed.ncbi.nlm.nih.gov/36096995/",
        "abstract": "Four currently approved drugs for sickle cell disease including hydroxyurea L-glutamine voxelotor and crizanlizumab are improving outcomes while new therapies are in clinical trials.",
        "text": "This review provides an overview of therapeutic strategies for sickle cell disease and discusses the four currently approved drugs in detail including hydroxyurea L-glutamine voxelotor 
        and crizanlizumab. Each of these agents targets different aspects of sickle cell disease pathophysiology including fetal hemoglobin induction oxidative stress reduction red blood cell sickling and 
        vaso-occlusion. Ongoing clinical trials are evaluating new drugs and drug combinations. Gene therapy approaches including CRISPR based editing represent the next frontier in potentially curative treatment 
        for sickle cell disease."
    },
    {
        "id": "paper_24",
        "field": "medicine",
        "title": "Arterial Hypertension Clinical Trials Update 2023",
        "url": "https://pubmed.ncbi.nlm.nih.gov/37443261/",
        "abstract": "The 2022 and 2023 hypertension clinical trials summarize new pharmacological approaches for resistant hypertension optimal blood pressure targets and device based treatment strategies.",
        "text": "Arterial hypertension is associated with increased morbidity and mortality and research in the field is highly dynamic. This summary reviews the most important clinical trials published in 2022 
        and early 2023. Findings on new pharmacological approaches to treat resistant hypertension are presented and new knowledge about the optimal timing of antihypertensive medication intake is discussed. The 
        review focuses on optimal blood pressure treatment targets and the problem of treatment inertia. Novel clinical data on device based approaches to treat hypertension including renal denervation are also summarized."
    },
    {
        "id": "paper_25",
        "field": "medicine",
        "title": "Burden of Chlamydia Gonorrhea and Syphilis in Older Adults",
        "url": "https://pubmed.ncbi.nlm.nih.gov/36626249/",
        "abstract": "Sexually transmitted infections among older adults are understudied with prevalence ranges of syphilis 0-18 percent chlamydia 0-14 percent and gonorrhea 0-15 percent highlighting a growing public health concern.",
        "text": "Increases in life expectancy the availability of sexual performance enhancing medication and changes in sexual partnering suggest that sexually transmitted infections among older persons could 
        be on the rise yet there have been relatively few studies examining sexually transmitted infections in this demographic. A systematic review aimed to further characterize the incidence and prevalence of chlamydia 
        gonorrhea and syphilis along with associated risk factors among older adults aged 45 years or older in the United States. The review found prevalence ranges of syphilis from 0 to 18 percent chlamydia from 0 to 14 
        percent and gonorrhea from 0 to 15 percent. The understudied burden of sexually transmitted infections in the older adult population substantiates the need to recognize issues surrounding sexuality in this demographic."
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

if __name__ == '__main__':
  papers_loaded = load_papers()
  for p in papers_loaded:
    print(f"{p['id']} - {p['title']} ({p['field']})")
    print(f"Source: {p['url']}\n")
