#!/bin/bash

. lib/decoder
. lib/ledcompiler


RGB_TXT=RGB_VALS.txt


rm -rf tmp 2>/dev/null
mkdir tmp 2>/dev/null
cd tmp


split_gif pacman.gif
for F in `ls -1 | grep frame_`
do
    scale_down $F
    get_rgb_for TRIMMED_$F >> ${RGB_TXT}
done

rgb2bin ${RGB_TXT}
