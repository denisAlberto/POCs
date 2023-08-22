coord1 = input('Entre com a primeira coordenada X Y Z. Ex.: -123, 60, 655\n')
coord2 = input('Entre com a segunda coordenada X Y Z. Ex.: -123, 60, 655\n')
coord3 = input('Entre com a coordenada onde deseja clonar os blocos X Y Z. Ex.: -123, 60, 655\n')

coord1 = [int(v) for v in coord1.split(',')]
coord2 = [int(v) for v in coord2.split(',')]
coord3 = [int(v) for v in coord3.split(',')]

a = abs(coord1[0] - coord2[0])
b = abs(coord1[1] - coord2[1])
c = abs(coord1[2] - coord2[2])

n_blocks = a * b * c
if n_blocks >= 32768:
    cmd_divisions = 1

initial_coord = [min(a,b) for a, b in zip(coord1, coord2)]
final_coord = [max(a,b) for a, b in zip(coord1, coord2)]

print(f'/clone {initial_coord[0]} {initial_coord[1]} {initial_coord[2]} {final_coord[0]} {final_coord[1]} {final_coord[2]} {coord3[0]} {coord3[1]} {coord3[2]}')