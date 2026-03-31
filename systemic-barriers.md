# Systemic Barriers in Healthcare

Despite extraordinary resources (billionaire founder, dedicated team, willing researchers), Sid encountered friction at every layer of the healthcare system. These barriers affect all patients, not just those with rare cancers.

---

## 1. Tissue Access

### The Problem
Hospitals default to formalin-fixed, paraffin-embedded (FFPE) tissue processing. This preserves morphology for pathology but **destroys nucleic acid quality** — making advanced genomic analysis difficult or impossible.

### What Sid Needed
Cryopreserved (flash-frozen) tissue samples that preserve RNA and DNA integrity for:
- Single-cell RNA sequencing
- Organoid development
- Comprehensive genomic profiling

### The Barrier
- Hospital pathology labs are optimized for FFPE workflows
- No standard process for splitting samples between clinical and research use
- Transferring patient tissue to external labs involves MTA (material transfer agreements), IRB review, and institutional reluctance
- Each hospital has different procedures, none are streamlined

### Impact
Without fresh/frozen tissue, the scRNA-seq that revealed FAP overexpression would not have been possible. The breakthrough treatment would never have been discovered.

---

## 2. Genomic Data Access

### The Problem
Clinical sequencing reports (Tempus, Foundation Medicine, etc.) provide a summary: a list of mutations and potential drug matches. The raw data (FASTQ, BAM files) is locked behind the testing company or hospital.

### What Sid Needed
Raw sequencing data to run independent analysis pipelines, cross-reference with research databases, and share with external collaborators.

### The Barrier
- "Shockingly hard" to obtain comprehensive sequencing data
- Clinical red tape and IRB resistance
- Sequencing companies treat data as proprietary
- Hospitals lack infrastructure for patient-directed data sharing
- No standard format or process for data portability

### Impact
Required dedicated effort from Jacob Stern (care CEO) to navigate data access across multiple institutions and companies.

---

## 3. Hospital IRBs as Vetocracies

### The Problem
Institutional Review Boards (IRBs) at hospitals must approve access to experimental treatments. Unlike the FDA, which has clear timelines and processes, IRBs operate independently with no standardized criteria.

### The Contrast
- **FDA**: Approved every Individual Patient Expanded Access IND (Form 3926) within 48 hours
- **Hospital IRBs**: Single members could block access to experimental medicines, creating "vetocracies"

### Why This Matters
The FDA has modernized its approach to personalized medicine. Hospital IRBs often have not. The bottleneck is institutional, not regulatory.

---

## 4. Sequential Treatment Paradigm

### The Problem
Standard oncology operates on a sequential model: try one therapy, wait months, scan, if it fails try the next. This is partly driven by:
- Clinical trial design (must isolate variables)
- Reimbursement models (one treatment at a time)
- Risk aversion (combination toxicity concerns)
- Tradition

### The Alternative
Sid's parallel approach — layering compatible therapies simultaneously — is not standard practice. It requires:
- Deep diagnostic understanding to avoid interactions
- Willingness to accept unknown combinatorial effects
- A decision-maker (patient) willing to take calculated risks
- Physicians willing to support unconventional protocols

### Impact
The sequential approach loses ground to aggressive cancers. Every month waiting for one therapy to "fail" before trying the next is a month the tumor is growing.

---

## 5. Economic Misalignment

### The Numbers
- Cost to develop and approve a new oncology drug: **$4.4 billion**
- Cost to dose a single person with personalized therapy: **~$1 million**

### The Misalignment
- Pharma incentives favor blockbuster drugs that treat millions
- Personalized therapies (neoantigen vaccines, custom radioligands) treat one person at a time
- Insurance models are built around approved drugs, not expanded access
- Hospital systems are optimized for standard protocols, not bespoke treatment

### The Opportunity
Platform technologies reduce the marginal cost of personalization:
- mRNA vaccine platforms: swap the antigen payload, keep the manufacturing
- Radioligand platforms: swap the targeting ligand, keep the isotope chemistry
- CAR-T platforms: swap the receptor target, keep the cell engineering
- CRISPR: patient-specific edits on a standard delivery platform

---

## 6. Information Asymmetry

### The Problem
Patients lack access to:
- Research literature (paywalled journals)
- Clinical trial data (fragmented across registries)
- Their own data (locked in hospital systems)
- Expert interpretation (requires specialized knowledge)

### Sid's Solution
- Dedicated care team (Jacob Stern as care CEO)
- Clinical advisory board + scientific advisory board
- Concierge medical services
- AI tools (ChatGPT) for literature review and decision support
- 1,000+ page personal health document

### The Gap
This level of information access requires significant resources. Most patients have none of this infrastructure.

---

## 7. Culture of Paternalism

### The Problem
Medicine traditionally operates on a paternalistic model: the physician knows best, the patient complies. This serves most patients reasonably well for routine care but fails catastrophically when:
- Standard treatments are exhausted
- The cancer is rare (limited clinical trial data)
- The patient has resources and motivation to do more

### The Alternative
"Founder mode" healthcare: the patient drives strategy, physicians execute. This requires:
- A patient capable of understanding complex medical decisions
- Physicians willing to be advisors rather than sole decision-makers
- A system that supports patient autonomy

---

## Implications for Scaling

These barriers are not unique to Sid's case. They affect every cancer patient to varying degrees. Even One Ventures exists to fund companies that address these barriers:

| Barrier | Scalable Solution |
|---------|-------------------|
| Tissue access | Standardized cryopreservation protocols in hospitals |
| Data access | Patient-owned health data platforms |
| IRB friction | Standardized expanded access workflows |
| Sequential treatment | AI-guided combination therapy design |
| Economic misalignment | Platform technology business models |
| Information asymmetry | AI-powered patient decision support |
| Paternalism | Concierge oncology platforms |
