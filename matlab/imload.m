function [img]= imload(fName)
    img=imread(fName);
    img=rgb2gray(img);
end