function [bxs]= blobDetect(img)
    imbw=binarize(img);
    [m, n]=size(imbw);
    area=m*n;
    %img=im2bw(img);
    %imshow(img);
    hblob=vision.BlobAnalysis;
    hblob.CentroidOutputPort=false;
    hblob.MinimumBlobArea=int32(area/100);
    hblob.MaximumBlobArea=int32(area/20);
    hblob.Connectivity=4;
    hblob.AreaOutputPort=false;
    bxs=step(hblob, imbw);
    shapeInserter = vision.ShapeInserter;
    oimg=step(shapeInserter, img, bxs);
    imshow(oimg);
end