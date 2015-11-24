function [ h ] = clrHist(img)
    [m, n]=size(img);
    img=reshape(img, [1, m*n]);
    h=hist(img, 20);
    h= h ./sum(h);  %normalize
end