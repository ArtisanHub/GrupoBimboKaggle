
import matplotlib.pyplot as plt
import pandas as pd
semana = list()
agencia_id = list()
canal_id = list()
ruta_sak = list()
cliente_id = list()
producto_id = list()
venta_uni_hoy = list()
dev_uni_proxima = list()
dev_proxima = list()
demand_uni_equil = list()
venta_hoy = list()

dataset_path = 'D:/FYP-Developments/Dataset-Kaggale/MedianRejectionSamplingData/train.csv'


for df in pd.read_csv(dataset_path,sep=',', header = None, chunksize=1):# split line into df
    demand_uni_equil.append(df[10][0])
    agencia_id.append(df[1][0])
    canal_id.append(df[2][0])
    ruta_sak.append(df[3][0])
    cliente_id.append(df[4][0])
    producto_id.append(df[5][0])
    venta_uni_hoy.append(df[6][0])
    venta_hoy.append(df[7][0])
    dev_uni_proxima.append(df[8][0])
    dev_proxima.append(df[9][0])
    semana.append(df[0][0])

figureoutfolderpath = 'D:/FYP-Developments/Dataset-Kaggale'
plt.scatter(demand_uni_equil, semana)#, s=5, c=4, alpha=0.5)
plt.ylabel('Semana')
plt.xlabel('Demand_Uni_Equil')
plt.savefig(figureoutfolderpath+'/semana.png')
# plt.show()
plt.clf()

plt.scatter(demand_uni_equil, agencia_id)#, s=5, c=4, alpha=0.5)
plt.ylabel('Agencia_ID')
plt.xlabel('Demand_Uni_Equil')
plt.savefig(figureoutfolderpath+'/agencia_id.png')
# plt.show()
plt.clf()

plt.scatter(demand_uni_equil, canal_id)#, s=5, c=4, alpha=0.5)
plt.ylabel('Canal_ID')
plt.xlabel('Demand_Uni_Equil')
plt.savefig(figureoutfolderpath+'/canal_id.png')
# plt.show()
plt.clf()

plt.scatter(demand_uni_equil, ruta_sak)#, s=5, c=4, alpha=0.5)
plt.ylabel('Ruta_Sak')
plt.xlabel('Demand_Uni_Equil')
plt.savefig(figureoutfolderpath+'/ruta_sak.png')
# plt.show()
plt.clf()

plt.scatter(demand_uni_equil, cliente_id)#, s=5, c=4, alpha=0.5)
plt.ylabel('Cliente_ID')
plt.xlabel('Demand_Uni_Equil')
plt.savefig(figureoutfolderpath+'/cliente.png')
# plt.show()
plt.clf()

plt.scatter(demand_uni_equil, producto_id)#, s=5, c=4, alpha=0.5)
plt.ylabel('Producto_ID')
plt.xlabel('Demand_Uni_Equil')
plt.savefig(figureoutfolderpath+'/producto.png')
# plt.show()
plt.clf()

plt.scatter(demand_uni_equil, venta_uni_hoy)#, s=5, c=4, alpha=0.5)
plt.ylabel('Venta_uni_hoy')
plt.xlabel('Demand_Uni_Equil')
plt.savefig(figureoutfolderpath+'/venta_uni_hoy.png')
# plt.show()
plt.clf()

plt.scatter(demand_uni_equil, venta_hoy)#, s=5, c=4, alpha=0.5)
plt.ylabel('Venta_hoy')
plt.xlabel('Demand_Uni_Equil')
plt.savefig(figureoutfolderpath+'/venta_hoy.png')
# plt.show()
plt.clf()

plt.scatter(demand_uni_equil, dev_uni_proxima)#, s=5, c=4, alpha=0.5)
plt.ylabel('Dev_uni_proxima')
plt.xlabel('Demand_Uni_Equil')
plt.savefig(figureoutfolderpath+'/dev_unit_proxima.png')
# plt.show()
plt.clf()

plt.scatter(demand_uni_equil, dev_proxima)#, s=5, c=4, alpha=0.5)
plt.ylabel('Dev_proxima')
plt.xlabel('Demand_Uni_Equil')
plt.savefig(figureoutfolderpath+'/dev_proxima.png')
# plt.show()
plt.clf()

print("All the plotted Figures are saved in the Out Folder")
