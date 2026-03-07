clc; clear; close all;


lambdas = [0 0.1 0.5 1.0 2.0];
[L_graph, L_cons] = meshgrid(lambdas, lambdas);


MAE = [
    0.122 0.115 0.108 0.112 0.120;
    0.113 0.104 0.098 0.102 0.110;
    0.106 0.097 0.091 0.095 0.103;
    0.110 0.101 0.095 0.100 0.108;
    0.118 0.109 0.103 0.107 0.115
];


fine = 120;
xq = linspace(min(lambdas), max(lambdas), fine);
yq = linspace(min(lambdas), max(lambdas), fine);
[Xq,Yq] = meshgrid(xq,yq);
Zq = interp2(L_graph, L_cons, MAE, Xq, Yq, 'spline');


cmap = flipud(jet);

figure('Color','w','Position',[100 100 1200 500])


subplot(1,2,1)

s = surf(Xq, Yq, Zq);
shading interp
colormap(cmap)



hold on

xgrid = linspace(min(lambdas), max(lambdas), 15);
ygrid = linspace(min(lambdas), max(lambdas), 15);
[Xg,Yg] = meshgrid(xgrid, ygrid);
Zg = interp2(L_graph, L_cons, MAE, Xg, Yg, 'spline');

mesh(Xg, Yg, Zg, 'EdgeColor', 'k', 'FaceAlpha', 0, 'LineWidth', 0.2);
hold off

ax = gca;
ax.FontSize = 11;
ax.LineWidth = 1;
ax.XColor = 'k';
ax.YColor = 'k';
ax.ZColor = 'k';
ax.Color = 'w';
ax.Box = 'on';

xlabel('\lambda_{graph}','FontSize',12,'Color','k')
hY = ylabel('\lambda_{consistency}','FontSize',12,'Color','k');


hY.Units = 'centimeters';

pos = hY.Position; 
pos(2) = pos(2) + 1.7;   
hY.Position = pos;

hY.Rotation = - 30;   
zlabel('MAE','FontSize',12,'Color','k')
view(135,50)
grid on


subplot(1,2,2)

levels = 15;


contf = contourf(Xq, Yq, Zq, levels);
colormap(cmap)
colorbar('Color','k')
hold on

contl = contour(Xq, Yq, Zq, levels, 'k','LineWidth',0.6);


clabel(contl, 'FontSize',11,'Color','k','LabelSpacing',300)  
hLabels = findobj(gca,'Type','text');  
for i = 1:length(hLabels)
    val = str2double(hLabels(i).String);
    if val >= 0.105
        delete(hLabels(i)) 
    end
end

ax2 = gca;
ax2.FontSize = 11;
ax2.LineWidth = 1;
ax2.XColor = 'k';
ax2.YColor = 'k';
ax2.Color = 'w';
ax2.Box = 'on';

xlabel('\lambda_{graph}','FontSize',12,'Color','k')
ylabel('\lambda_{consistency}','FontSize',12,'Color','k')
title('MAE','FontSize',12,'Color','k')
grid off
