#!/bin/bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null && pwd )"
DATA_DIR="$DIR/../example_data/1/"
set -euxo pipefail
chmod +x marvel

./marvel -i "$DATA_DIR" -o test_output -t 2 -f  --debug --verbose

rm -rf test_output
