if exist('LastFolder','var')
    GetFileName=sprintf('%s/*.csv',LastFolder);
else
    GetFileName='*.csv';
end

[Filename,PathName] = uigetfile(GetFileName,'Select the csv file for PAINT data');
LastFolder=PathName;

FullFileName=sprintf('%s%s',PathName,Filename);

Filehead=Filename(1:end-4);

PixArray=load(FullFileName);
% PixArray=round(PixArray/5);

if exist('LastFolder','var')
    GetFileName=sprintf('%s/*.spe',LastFolder);
else
    GetFileName='*.spe';
end

[Filename,PathName] = uigetfile(GetFileName,'Select the spe file PAINT data');
LastFolder=PathName;

FullFileName=sprintf('%s%s',PathName,Filename);

Filehead=Filename(1:end-4);

Input=readSPE(FullFileName);

[XSize,YSize,NumFrames]=size(Input);

Counter_index_On_Array = [];

Count = 0;

for n=1:size(PixArray,1)
    
    if PixArray(n,1)>=4 && PixArray(n,1)<=253 && PixArray(n,2)>=4 && PixArray(n,2)<=253 
        Count = Count +1;
        PixArray(Count,:) = [PixArray(n,1),PixArray(n,2),PixArray(n,3)];
    end

end

for m = 1:size(PixArray,1)
    
    OutputName=sprintf('%sc%d-trace.png',PathName,m);  
    
    expoTime = 0.033;
    yStart=PixArray(m,1);
    xStart=PixArray(m,2);

    x = xStart-3:xStart+3;
    y = yStart-3:yStart+3;
    Steps = 1:NumFrames;

    mol = Input(y,x,:);

    mol_Int = sum(mol,[1 2]);
    mol_Sq = squeeze(mol_Int);

    xTimeMax = expoTime*(NumFrames-1);
    xTime = 0:expoTime:xTimeMax;
    xTime=xTime';

%     mol_Sq_noBG = msbackadj(xTime, mol_Sq,'RegressionMethod','pchip','WindowSize',10,'StepSize',10);

%     %------------Smooth----------
%     XSpan1=3;
%     XSpan2=3;
%     mol_Smo1=smooth(xTime,mol_Sq_noBG,XSpan1,'sgolay',1);
%     mol_Smo2=smooth(xTime,mol_Smo1,XSpan2,'sgolay',1);
%     %----------------------------
% 
%     mol_array_smo = [xTime mol_Smo2];
%     mol_array = [xTime mol_Sq];
%     mol_array_noBG = [xTime mol_Sq_noBG];
% 
%     binsize = 150;
%     [histy,histx] = hist(mol_Smo2,binsize);
%     histf = fit(histx.',histy.','Gauss2');
%     baseline = histf.b1+ 6*(histf.c1/sqrt(2));
% 
%     baseline_array = repelem(baseline,NumFrames);
%     baseline_array = baseline_array';
% 
%     mol_array_On = [];
%     mol_array_Off = [];
% 
%     for n=1:length(mol_Sq_noBG)
%         if mol_array_smo(n,2)-baseline_array(n) > 0
%             mol_array_On = [mol_array_On;mol_array_smo(n,:)];
%         else
%             mol_array_Off = [mol_array_Off;mol_array_smo(n,:)];
%         end
%     end
% 
%     Counter_index_On = [];
%     Counter = 1;
% 
%     for n = 1:length(mol_array_On)    
%         if n+1 <= length(mol_array_On)        
%             if mol_array_On(n+1,1) == mol_array_On(n,1) + expoTime
%                Counter = Counter + 1;
%             else
%                Counter_index_On = [Counter_index_On;Counter];
%                Counter = 1; 
%             end
%         end
% 
%     end
% 
%     Counter_index_Off = [];
%     Counter = 1;
% 
%     for n = 1:length(mol_array_Off)    
%         if n+1 <= length(mol_array_Off)        
%             if mol_array_Off(n+1,1) == mol_array_Off(n,1) + expoTime
%                Counter = Counter + 1;
%             else
%                Counter_index_Off = [Counter_index_Off;Counter];
%                Counter = 1; 
%             end
%         end
% 
%     end
%     
%     Counter_index_On_Array = [Counter_index_On_Array; Counter_index_On];

    figure(2)
    myplot = plot(xTime,mol_Sq);
    saveas(myplot,OutputName) 
    
%     figure(3)
%     plot(xTime,mol_Sq_noBG)
%     
%     figure(4)
%     plot(histf,histx,histy)
%     
%     figure(5)
%     myplot1 = plot(xTime,mol_Sq_noBG,xTime,mol_Smo2,mol_array_On(:,1),mol_array_On(:,2),'o',xTime,baseline_array);
%     saveas(myplot,OutputNameNoBG) 
    
%     close all
end
