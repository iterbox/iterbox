#!/bin/bash

set -e

echo 'List files from cached directories'
echo 'pip:'
ls $HOME/.cache/pip
ls $HOME/.ccache

if [[ "$DISTRIB" == "conda" ]]; then
    # Deactivate the travis-provided virtual environment and setup a
    # conda-based environment instead
    deactivate

    # Use the miniconda installer for faster download / install of conda
    # itself
    DOWNLOAD_DIR=${DOWNLOAD_DIR:-$HOME/.tmp/miniconda}
    mkdir -p $DOWNLOAD_DIR
    wget http://repo.continuum.io/miniconda/Miniconda-latest-Linux-x86_64.sh \
        -O $DOWNLOAD_DIR/miniconda.sh
    chmod +x $DOWNLOAD_DIR/miniconda.sh && \
        bash $DOWNLOAD_DIR/miniconda.sh -b -p $HOME/miniconda && \
        rm -r -d -f $DOWNLOAD_DIR
    export PATH=$HOME/miniconda/bin:$PATH
    conda update --yes conda

    # Configure the conda environment and put it in the path using the
    # provided versions
    conda create -n testenv --yes python=$PYTHON_VERSION pip
    source activate testenv
elif [[ "$DISTRIB" == "ubuntu" ]]; then
    # Use standard ubuntu packages in their default version
    echo $DISTRIB
    echo 'Using the travis-provided virtual environment'

fi

if [[ "$COVERAGE" == "true" ]]; then
    pip install coverage coveralls
fi