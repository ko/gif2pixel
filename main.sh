#!/bin/bash

. lib/decoder

BASEDIR=`pwd`

RGB_TXT=${BASEDIR}/RGB_VALS.txt
BIN_OUT=${BASEDIR}/outfile.bin

LIB_DIR=${BASEDIR}/lib

rm -rf tmp 2>/dev/null
mkdir tmp 2>/dev/null
cd ${BASEDIR}/tmp


split_gif pacman.gif
for F in `ls -1 | grep frame_`
do
    scale_down $F
    get_rgb_for TRIMMED_$F >> ${RGB_TXT}
done

cd $LIB_DIR

python -c 'import ledcompiler; \
    ledcompiler.rgb2bin(\
        "../RGB_VALS.txt", \
        "../outfile.bin"\
    )'
