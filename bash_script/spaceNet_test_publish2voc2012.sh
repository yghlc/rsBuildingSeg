#!/bin/bash

spacenet_root=${HOME}/Data/aws_SpaceNet/un_gz
output_root=${HOME}/Data/aws_SpaceNet/voc_format
python_script=${HOME}/codes/PycharmProjects/rsBuildingSeg/SpaceNetChallenge/utilities/python/createDataSpaceNet.py

#${spacenet_root}
AOI_2=AOI_2_Vegas_Test_public
AOI_3=AOI_3_Paris_Test_public
AOI_4=AOI_4_Shanghai_Test_public
AOI_5=AOI_5_Khartoum_Test_public

# remove previous success_save.txt file
rm success_save.txt

#echo ${AOIs} ${AOI_3} ${AOI_4} ${AOI_5}
for AOI in ${AOI_2} ${AOI_3} ${AOI_4} ${AOI_5}
do
    echo training data dir: $spacenet_root/$AOI

test_data_root=${spacenet_root}/${AOI}/RGB-PanSharpen
outputDirectory=${output_root}/${AOI}/RGB-PanSharpen_8bit
echo ${test_data_root}
echo ${outputDirectory}

dir=${test_data_root}
for tiffile in $(ls $dir/*.tif)
do
    echo $tiffile
python /home/hlc/codes/PycharmProjects/rsBuildingSeg/basic/tif_16bit_to_8bit.py ${tiffile} ${outputDirectory}

done


done


