#!/bin/bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null && pwd )"
DATA_DIR="$DIR/../example_data/1/"
set -euxo pipefail
chmod +x marvel  download_and_set_models.py

echo 'CHECK HMMPRESS'
hmmpress -h

echo 'DOWNLOAD DATABASE'

./download_and_set_models.py

echo 'TEST PROKKA'

prokka --kingdom Viruses --centre X --compliant --gcode 11 --force --quiet --fast --norrna --notrna --cdsrnaolap --noanno --cpus 2 --prefix test --outdir test_prokka/custom_test "$DATA_DIR"/Negative_CP011125.fasta

echo 'TEST CUSTOM PROKKA'

perl "$DIR"/../marvel_prokka --kingdom Viruses --centre X --compliant --gcode 11 --force --quiet --fast --norrna --notrna --cdsrnaolap --noanno --cpus 2 --prefix test --outdir test_prokka/custom_test "$DATA_DIR"/Negative_CP011125.fasta




./marvel -i "$DATA_DIR" -o test_output -t 2 -f  --debug --verbose

rm -rf test_output
