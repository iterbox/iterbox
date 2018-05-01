#!/bin/bash

set -e

if [[ "$DISTRIB" == "ubuntu" ]]; then
    # Use standard ubuntu packages in their default version
    echo $DISTRIB
fi

if [[ "$COVERAGE" == "true" ]]; then
    pip install coverage coveralls
fi