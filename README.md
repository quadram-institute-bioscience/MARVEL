
# MARVEL Fork
**Metagenomic Analysis and Retrieval of Viral Elements**

[![Build Status](https://travis-ci.org/quadram-institute-bioscience/MARVEL.svg?branch=master)](https://travis-ci.org/quadram-institute-bioscience/MARVEL)

### Usage

```
usage: marvel [-h] [-i INPUT_FOLDER] [-t THREADS] [-o OUTDIR] [-m CTGMINLEN]
              [-c CONFIDENCE] [-d DATABASEDIR] [-f] [-v] [--debug] [--keep]
              [--cite]

Predic phage draft genomes in metagenomic bins.

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT_FOLDER, --input-dir INPUT_FOLDER
                        Path to a folder containing metagenomic bins in .fa or
                        .fasta format
  -t THREADS, --threads THREADS
                        Number of CPU threads to be used by Prokka and hmmscan
                        (default=1)
  -o OUTDIR, --output-dir OUTDIR
                        Output directory
  -m CTGMINLEN, --min-len CTGMINLEN
                        Bin minimum size (default=2000)
  -c CONFIDENCE, --confidence CONFIDENCE
                        Confidence threshold (default=0.7)
  -d DATABASEDIR, --db DATABASEDIR
                        Database directory (default: install_dir)
  -f, --force           Force overwrite
  -v, --verbose         Print verbose output
  --debug               Enable debug mode
  --keep                Keep all intermediate files
  --cite                Show citations
```

### Author

Original release by:

* [Deyvid Amgarten](https://sites.google.com/view/deyvid/english)  
This pipeline was written as part of my PhD thesis by the [Bioinformatics Graduate Program](https://www.ime.usp.br/en/bioinformatics/graduate) from the University of Sao Paulo, Brazil.

Fork maintained and updated by:

* Andrea Telatin, Quadram Institute Bioscience, Norwich, UK
### License

This project is licensed under GNU license. Codes here may be used for any purposed or modified.  
This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

