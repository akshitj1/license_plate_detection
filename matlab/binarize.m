function [ bImg ] = binarize(img)
    bImg=im2bw(img, 0.5);
    bImg=~bImg;
end