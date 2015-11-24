%{
img=imload('d1.jpg');
tImg=imload('lp_full.jpg');
imLbp=LBP(img);
tLbp=LBP(tImg);
%img=double(img);
%tImg=double(tImg);
%}
%[ 251 151 205 818]
[h,w]=size(imLbp);
tHist=lbpHist(tLbp);
minDist=100000;
bBox=[0 0 0 0];
scaleStp=5
moveStp=10
for scaleF=2:scaleStp
    scaleF
    bBox
    minDist
    winW=int32(scaleF*(w/scaleStp));
    winH=int32(winW/4);
    for x=1:moveStp:w-winW
        for y=1:moveStp:h-winH
            cHist=lbpHist(imLbp(y:y+winH, x:x+winW));
            %cHist=clrHist(img(y:y+winH, x:x+winW));
            %cDist=sum(min(tHist(:), cHist(:)));
            cDist=pdist2(tHist, cHist);
            if cDist<minDist
                minDist=cDist;
                bBox=[y x winH winW];
            end
        end
    end
end