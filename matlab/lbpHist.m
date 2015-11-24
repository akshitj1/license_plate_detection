function [ h ] = lbpHist( lbp)
    [m, n]=size(lbp);
    lbp=reshape(lbp, [1, m*n]);
    h=hist(lbp, 69);
    h= h ./sum(h);  %normalize
end