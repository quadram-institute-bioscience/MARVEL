#!/usr/bin/env python3
# coding: utf-8
#
#
## This is the MARVEL Pipeline for analysis and retrieaval of Viral Long sequences
## This is an auxiliary script to download and set models
# Developed by Deyvid Amgarten

# Libraries
import os
import re
import sys
import subprocess

script_dir = os.getcwd()
repository = 'https://github.com/quadram-institute-bioscience/MARVEL/raw/master/models/'


# Print to STDERR [proch]
def print_msg(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def fix_path(dir):
    if not re.search('/$', dir):
        return dir + '/'
    else:
        return dir

print_msg("Usage: [Dest_Dir] [Tmp_Dir]")

if len(sys.argv) >= 2:
    db_dir = fix_path(sys.argv[1])
else:
    db_dir = fix_path(script_dir + '/models/')


if len(sys.argv) == 3:
    tmp_dir = fix_path(sys.argv[2] + '/')
else:
    tmp_dir = fix_path('/tmp/')

print_msg("Destination directory: {}\nTemp directory: {}".format(db_dir, tmp_dir) )

models = [ 'pickle_model_rfc_trained_bins8k_refseq_all_3features_den_stran_prophitshmm.pkl', 
 'pickle_model_rfc_trained_bins_refseq_until2015_3features_den_stran_prophitshmm.pkl',
 'pickle_model_rfc_trained_bins_refseq_until2015_4features_wt_outliers_even2.pkl']

# Verify databases
if not os.path.isfile(db_dir + 'all_vogs_hmm_profiles_feb2018.hmm.h3m') or not os.path.isfile(db_dir + models[0]):
    print_msg('[1] Downloading flat file database...')
    os.system('wget --quiet -O "{}" http://projetos.lbi.iq.usp.br/metazoo/deyvid/datasets/AllvogHMMprofiles.tar.gz'.format(tmp_dir + 'AllvogHMMprofiles.tar.gz') )
    
    print_msg('[2] Extracting database file...')
    extract_cmd = 'tar -xzf "{}"  -C "{}"'.format(tmp_dir + 'AllvogHMMprofiles.tar.gz', tmp_dir)
   
    if subprocess.call(extract_cmd, shell=True) != 0:
        print('FATAL ERROR: Unable to extract database\n')
        quit()

    subprocess.run('cat "{}"/* > "{}"/all_vogs_hmm_profiles_feb2018.hmm'.format(tmp_dir + 'AllvogHMMprofiles', db_dir), shell=True)

    print_msg('[3] Downloading models')
    for file in models:
        print_msg(' - {}'.format(file))
        wget_cmd = 'wget --quiet -O "{}/{}" "{}{}"'.format(db_dir, file, repository, file)
        os.system( wget_cmd )
    
    print_msg('[4] Compressing hmm database...')
    if subprocess.call('hmmpress "{}"/all_vogs_hmm_profiles_feb2018.hmm'.format(db_dir), shell=True) != 0:
        print_msg('Error using hmmer tools (hmmpress). Verify if it is installed!\n')
        print_msg('hmmpress "{}"/all_vogs_hmm_profiles_feb2018.hmm'.format(db_dir))
        quit()

    subprocess.run('rm -r "{}"/AllvogHMMprofiles/ "{}"/AllvogHMMprofiles.tar.gz'.format(tmp_dir, tmp_dir), shell=True)

    print_msg('Done.')
else:
    print('INFO: HMM Database found.\n')
