
# MARVEL
**Metagenomic Analysis and Retrieval of Viral Elements**

MARVEL is a pipeline for recovery of complete phage genomes from whole community shotgun metagenomic sequencing data.  

Main script:
   * **marvel_bins.py** - Machine learning prediction of phage bins
  
Auxiliary script:
   * **generate_bins_from_reads.py** - Generates metagenomic bins, given Illumina sequencing reads


### Dependencies

To create a conda environment: 
```
conda create -n marvel numpy scikit-learn prokka
```

### Installing

Getting MARVEL ready to run is as simple as clone this Github project or dowload and extract it to a directory inside you computer:

```
git clone https://github.com/LaboratorioBioinformatica/MARVEL
```

### Getting Started

Inside the directory where MARVEL was extracted (or cloned), you will need to download and set the models. 
This is required only once and it is simple. Just run:
```
python3 download_and_set_models.py [Destination_directory] [Temporary_Directory]
```

Now, to run MARVEL type:
```
python3 marvel_bins.py -i input_directory -o output_directory [-d database_directory] [-t num_threads]
```

Change 'input_directory' for the folder where bins are stored in fasta format and 'num_threads' for the number of CPU cores to be used. Several threads should be used for speed up prokka and hmm searches.  


### Additional scripts

MARVEL's main script receives metagenomic bins as input. However, we additionally provide a simple scrip which receives
metagenomic reads (Illumina sequencing) and generates bins.
[metaSpades](http://bioinf.spbau.ru/spades), [Bowtie2]() and [Metabat2](https://bitbucket.org/berkeleylab/metabat) are used for assembling, mapping and binning, respectively.  

In case you want to generate the bins by yourself, we recommend two special parameters in the binning process: -m 1500 -s 10000. These parameters tell metabat to generate bins with contigs of at least 1500 bp and with a minimum total size of 10 kbp, which makes more sense when one is trying to retrieve viral genomes.  
We can't stress enough that there are several tools for assembly and binning, which should be well-chosen according to
the researcher's purposes. Our intention here is to facilitate the use of our tool.  

```
python3 generate_bins_from_reads.py -1 reads-R1.fastq -2 reads-R2.fastq -t num_threads
```

### Simulated RefSeq datasets for training and testing

All the simulated datasets used for training and testing the Random Forest classifier, as well as predicted bins from composting samples were made available through this link:

[Browse and Download datasets](http://projetos.lbi.iq.usp.br/metazoo/deyvid/datasets/) 

### Author
[Deyvid Amgarten](https://sites.google.com/view/deyvid/english)  
This pipeline was written as part of my PhD thesis by the [Bioinformatics Graduate Program](https://www.ime.usp.br/en/bioinformatics/graduate) from the University of Sao Paulo, Brazil.


### License

This project is licensed under GNU license. Codes here may be used for any purposed or modified.  
This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

