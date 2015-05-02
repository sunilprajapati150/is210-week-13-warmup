#!/bin/bash
# -*- coding: utf-8 -*-
#
# Testrunner for this repository.

ROOT="$( cd "$( dirname "$0" )" && pwd )"
TESTDIR="${ROOT}/tests"
: ${LOGDIR="/tmp"}

# lint tests
find "${ROOT}" -path "${TESTDIR}" -prune -o -type f -iname "*.py" -print0 | while read -d $'\0' file
do
    pylint "${file}" | tee -a "${LOGDIR}/pylint.log"
done

# unit tests
nosetests --with-xunit --xunit-file="${LOGDIR}/nosetest.xml"

