class Questions:
    """
    Class responsible for holding and returning all the questions
    Currently no functionality of appending questions, but adding
    additional difficulty or additional tests will not break the system
    """
    def __init__(self):
        self._questions = {
            "easy": [
                "What is a metagenome?",
                "What is the central dogma of molecular biology?",
                "What is a genome?",
                "What is a protein?",
                "What is a gene?",
                "What is DNA sequencing?",
                "What is the difference between DNA and RNA?",
                "What is a nucleotide?",
                "What is a codon?",
                "What is an amino acid?",
                "What is a BLAST search?",
                "What is a multiple sequence alignment?",
                "What is a phylogenetic tree?",
                "What is a gene ontology?",
                "What is a protein domain?",
                "What is a protein family?",
                "What is a conserved sequence?",
                "What is a gene expression profile?",
                "What is a microarray?",
                "What is a single nucleotide polymorphism (SNP)?",
                "What is a haplotype?",
                "What is a genome assembly?",
                "What is a metagenome?",
                "What is a functional annotation?",
                "What is a proteome?"
            ],
            "medium": [
                "What is a hidden Markov model (HMM) and how is it used in bioinformatics?           ",
                "What is the significance of the p-value in sequence alignment?                      ",
                "What is a position-specific scoring matrix (PSSM)?                                  ",
                "What is a Gibbs sampler and how is it used in bioinformatics?                       ",
                "What is a motif and how is it identified in DNA or protein sequences?               ",
                "What is a protein-protein interaction network and how is it constructed?            ",
                "What is a homology modeling and how is it used to predict protein structures?       ",
                "What is a support vector machine (SVM) and how is it used in bioinformatics?        ",
                "What is a neural network and how is it used in bioinformatics?                      ",
                "What is a protein fold and how is it determined?                                    ",
                "What is RNA splicing and how is it regulated?                                       ",
                "What is a transcriptome and how is it analyzed?                                     ",
                "What is a ChIP-seq experiment and how is it used to study protein-DNA interactions? ",
                "What is a gene regulatory network and how is it constructed?                        ",
                "What is a genome-wide association study (GWAS) and how is it used to identify "
                "genetic variants associated with diseases?  ",
                "What is a principal component analysis (PCA) and how is it used in analyzing high-throughput data?",
                "What is a protein structure prediction and what are the different methods used for it?            ",
                "What is a gene ontology enrichment analysis and how is it performed?                              ",
                "What is a co-expression network and how is it constructed?                                        ",
                "What is a BLAST score and how is it calculated?                                                   ",
                "What is a reciprocal best hit and how is it used in sequence similarity searches?                 ",
                "What is a consensus sequence and how is it calculated?                                            ",
                "What is a multiple testing correction and why is it important in high-throughput data analysis?   ",
                "What is a genome annotation and how is it performed?                                              ",
                "What is a protein-ligand interaction and how is it predicted?                                     ",
            ],
            "hard": [
                "What is a de novo assembly and what are the challenges in performing it?                                 ",
                "What is a metatranscriptome and how is it analyzed?                                                      ",
                "What is a proteogenomics approach and how is it used to improve genome annotation?                       ",
                "What is a metaproteomics approach and how is it used to study microbial communities?                     ",
                "What is a transcript isoform and how is it identified and quantified?                                    ",
                "What is a single-cell transcriptome and how is it analyzed?                                              ",
                "What is a CRISPR-Cas system and how is it used for genome editing and engineering?                       ",
                "What is a nanopore sequencing technology and how is it different from other sequencing technologies?     ",
                "What is a long-read sequencing technology and how is it used for genome assembly and analysis?           ",
                "What is a gene fusion and how is it detected?                                                            ",
                "What is a structural variant and how is it identified?                                                   ",
                "What is a transcript quantification and what are the different methods used for it?                      ",
                "What is a protein function prediction and what are the different methods used for it?                    ",
                "What is a protein-protein docking and how is it used to predict protein-protein interactions?            ",
                "What is a protein-ligand docking and how is it used to predict protein-ligand interactions?              ",
                "What is a protein interaction domain and how is it identified and characterized?                         ",
                "What is a protein interaction interface and how is it identified and characterized?                      ",
                "What is a gene expression heterogeneity and how is it analyzed?                                          ",
                "What is a multi-omics integration and how is it used to study biological systems?                        ",
                "What is a network analysis and how is it used to study biological systems?                               ",
                "What is a transcriptome-wide association study (TWAS) and how is it used to identify disease-associated "
                "genes?",
                "What is a metagenome-wide association study (MWAS) and how is it used to identify microbial taxa "
                "associated with diseases?  ",
                "What is a gene set enrichment analysis (GSEA) and how is it used to identify pathways or functions "
                "enriched in a gene list? ",
                "What is a gene regulatory motif and how is it identified and characterized?                              ",
                "What is a protein post-translational modification and how is it identified and characterized?            ",
            ],
            "very hard": [
                "What is a genome-wide epigenetic analysis and how is it performed?                                       ",
                "What is a genome-wide CRISPR screen and how is it used to study gene function?                           ",
                "What is a phylogenomic analysis and how is it used to reconstruct evolutionary relationships?            ",
                "What is a multi-scale modeling and how is it used to study biological systems?                           ",
                "What is a single-molecule imaging and how is it used to study biological processes?                      ",
                "What is a topological analysis and how is it used to study biological networks?                          ",
                "What is a quantum biology and how is it related to bioinformatics?                                       ",
                "What is a high-dimensional data analysis and what are the challenges in analyzing such data?             ",
                "What is a spatio-temporal modeling and how is it used to study dynamic biological processes?             ",
                "What is a single-cell multi-omics integration and how is it used to study cellular heterogeneity?        ",
                "What is a systems pharmacology and how is it used to predict drug efficacy and toxicity?                 ",
                "What is a protein-protein interaction network alignment and how is it used to study conserved pathways and"
                "functions?",
                "What is a protein complex structure prediction and how is it used to study protein interactions?         ",
                "What is a protein structure refinement and how is it used to improve protein structure accuracy?         ",
                "What is a protein folding simulation and how is it used to study protein folding mechanisms?             ",
                "What is a protein dynamics simulation and how is it used to study protein function and interactions?     ",
                "What is a protein-protein interaction energy landscape and how is it used to study protein binding "
                "specificity?",
                "What is a gene expression dynamics modeling and how is it used to study gene regulatory networks?        ",
                "What is a stochastic gene expression and how is it modeled and analyzed?                                 ",
                "What is a single-cell epigenomics and how is it used to study epigenetic regulation in individual cells  ",
                "What is a single-cell proteomics and how is it used to study protein expression in individual cells?     ",
                "What is a single-molecule sequencing and how is it used for high-resolution genome analysis?             ",
                "What is a haplotype phasing and how is it used to study genetic variation?                               ",
                "What is a multi-locus sequence typing and how is it used to study bacterial populations and evolution?   ",
                "What is a coevolution analysis and how is it used to study protein interactions and functional "
                "relationships?",
            ]
        }

    @property
    def questions(self):
        """
        :return: a list of all the questions
        """
        all_questions = []
        for difficulty in self._questions:
            all_questions = all_questions + self._questions[difficulty]
        return all_questions

    def return_dict_questions(self):
        return self._questions

    def return_specific_questions(self, dificulty: str, start_index = 0, finishing_index = 25) -> list:
        """
        Used for testing with a small array of questions. Currently no catching logic so make sure the appropriate
        key is given
        :param dificulty: A key in dictionary
        :param start_index: index to specify of skipping first questions
        :param finishing_index: index to specify of skipping first questions
        :return:
        """
        return self._questions[dificulty][start_index:finishing_index]