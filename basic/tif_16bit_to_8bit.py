#!/usr/bin/env python
from osgeo import gdal, osr, ogr

import subprocess,os

from optparse import OptionParser
import io_function

def tif_16bit_to_8bit(rasterImageName,
                           ouptput_dir,
                           convertTo8Bit=True,
                           outputPixType='Byte',
                           outputFormat='GTiff'):

    srcRaster = gdal.Open(rasterImageName)

    if convertTo8Bit:
        cmd = ['gdal_translate', '-ot', outputPixType, '-of', outputFormat, '-co', '"PHOTOMETRIC=rgb"']
        scaleList = []
        for bandId in range(srcRaster.RasterCount):
            bandId = bandId+1
            band=srcRaster.GetRasterBand(bandId)
            min = band.GetMinimum()
            max = band.GetMaximum()

            # if not exist minimum and maximum values
            if min is None or max is None:
                (min, max) = band.ComputeRasterMinMax(1)
            cmd.append('-scale_{}'.format(bandId))
            cmd.append('{}'.format(0))
            cmd.append('{}'.format(max))
            cmd.append('{}'.format(0))
            cmd.append('{}'.format(255))

        cmd.append(rasterImageName)

        outputRaster = os.path.join(ouptput_dir,os.path.basename(rasterImageName))
        if outputFormat == 'JPEG':
            outputRaster = outputRaster.replace('.tif', '.jpg')

        outputRaster = outputRaster.replace('_img', '_8bit_img')
        cmd.append(outputRaster)
        print(cmd)
        subprocess.call(cmd)

def main(options, args):
    # matpath = 'RGB-PanSharpen_AOI_2_Vegas_8bit_img4_blob_0.mat'

    #list file
    tif_path = args[0]
    save_dir = args[1]
    if os.path.isdir(save_dir) is False:
        io_function.mkdir(save_dir)

    tif_16bit_to_8bit(tif_path,save_dir)


if __name__=='__main__':
    usage = "usage: %prog [options] intput_tif save_dir"
    parser = OptionParser(usage=usage, version="1.0 2017-4-23")

    (options, args) = parser.parse_args()
    main(options, args)