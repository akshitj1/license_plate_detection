function [ LBP ] = LBP( I2)
    m=size(I2,1);
    n=size(I2,2);
    for i=2:m-2
        for j=2:n-2
            center=I2(i,j);
            I3(i-1,j-1)=I2(i-1,j-1)>center;
            I3(i-1,j)=I2(i-1,j)>center;
            I3(i-1,j+1)=I2(i-1,j+1)>center; 
            I3(i,j+1)=I2(i,j+1)>center;
            I3(i+1,j+1)=I2(i+1,j+1)>center; 
            I3(i+1,j)=I2(i+1,j)>center; 
            I3(i+1,j-1)=I2(i+1,j-1)>center; 
            I3(i,j-1)=I2(i,j-1)>center;
            LBP(i,j)=I3(i-1,j-1)*2^7+I3(i-1,j)*2^6+I3(i-1,j+1)*2^5+I3(i,j+1)*2^4+I3(i+1,j+1)*2^3+I3(i+1,j)*2^2+I3(i+1,j-1)*2^1+I3(i,j-1)*2^0;
        end
    end
end