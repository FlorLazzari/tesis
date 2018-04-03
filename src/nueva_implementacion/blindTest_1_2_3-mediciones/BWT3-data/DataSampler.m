function DataSampler(f,XIm,YIm,XScl,YScl)
%__________________________________________________________________________
% DESCRIPTION:
%
%  DataSampler helps digitalizing data from graphical charts into Matlab.
%
%  The function will upload a gray-scale JPG file identified by "f".
%  The parameters XIm and YIm are vectors containing the actual limits of
%  the figure. XScl and YScl are the type of axis of the figure 'linear' or
%  'log'.
%
% How to use DataSampler:
%
% 1	Once the image is loaded, adjust the zoom window to see all the data
%   you will pick-up. Once you finish, press ENTER.
%
% 2	The zoom tool will turn into a cursor, start clicking the points you
%   want to sample. Once you finish, press ENTER.
%
% 3 If you need to re-adjust the zoom in the picture, press ENTER, then
%   rigth-click with the mouse and this will activate the zoom tool again.
%   Proceed as before to adjust zoom, once you are ready to keep collecting
%   data, press ENTER again.
%
% 4	When you finish collecting all the data, press ENTER two times (first 
%   time will allow you to adjust zoom, second time will indicate that you
%   are done with the sampling). DataSampler will superimpose the original 
%   image with the information you just sampled. Use this step to verify 
%   that all the points you picked coincide with the original data. Once 
%   you finish checking, press ENTER to save the sampled data into a file.
%
% DataSampler will save a �.mat� file with the same name as the image 
% containing the data on a variable call "SmpData".
%
% VARIABLES:
%
% f    = Identifier of the file to be loaded and of the .mat file to save.
% XIm  = X limits of the figure.
% YIm  = Y limits of the figure.
% XScl = Scale type of X axis: 'linear' or 'log'.
% YScl = Scale type of Y axis: 'linear' or 'log'.
%__________________________________________________________________________


%Upload & Display Image:
I = imread([f '.jpeg']);
A=rgb2gray(I);
%A=imread([f '.jpg']);     % file MUST be gray-scale
figure(1)
clf
image(XIm,YIm,flipud(A));
colormap(bone(256));
set(gca,'YDir','normal','XScale',XScl,'YScale',YScl);
hold on


% Data Sampling:
SmpData=[];
k1=0;
while k1==0
   k=0;
   zoom on
   while k==0
      k=waitforbuttonpress;
      if k==1
         zoom off
      end
   end
   [Xx,Yy]=ginput;
   SmpData=[SmpData [Xx Yy]'];   
   k1=waitforbuttonpress;
end


% Save & Plot:
% plot(Cm(1,:),Cm(2,:),'-ok','MarkerEdgeColor','r','MarkerSize',4);
save([f '.mat'],'SmpData');
plot(SmpData(1,:),SmpData(2,:),'ro','MarkerSize',3);
axis([XIm,YIm])
hold off