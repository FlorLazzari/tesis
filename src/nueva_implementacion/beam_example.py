# Beam . py : s o l v e s Navier−−Stokes equation f o r flow around beam
i m p o rt m a t p l o t l i b . p y l a b as p ;
from m p l _ t o o l k i t s . mplot3d i m p o rt Axes3D ;
from numpy i m p o rt * ;
p r i n t ( " Working , wait f o r the f i g u r e a f t e r 100 i t e r a t i o n s " )
Nxmax = 7 0 ;
Nymax = 2 0 ;
IL = 1 0 ;
u = z e r o s ( ( Nxmax+1 , Nymax+1) , f l o a t )
w = z e r o s ( ( Nxmax+1 , Nymax+1) , f l o a t )
V0 = 1 . 0 ;
omega = 0 . 1 ;
nu = 1 . ;
H = 8;
iter = 0;
T = 8;
h = 1.
# Stream
# Vorticity
R = V0 * h / nu
587588
25 Fluid Dynamics
def borders ( ) :
f o r i i n r an g e ( 0 , Nxmax+1) :
f o r j i n r an g e ( 0 , Nymax+1) :
w[ i , j ] = 0 .
u [ i , j ] = j * V0
f o r i i n r an g e ( 0 , Nxmax+1 ) :
u [ i , Nymax ] = u [ i , Nymax−1] + V0 * h
w[ i , Nymax−1] = 0 .
f o r j i n r an g e ( 0 , Nymax+1) :
u[1 , j ] = u[0 , j ]
w[ 0 , j ] = 0 .
for
i i n r an g e ( 0 , Nxmax+1) :
i f i <= IL and i >= IL+T :
u [ i , 0] = 0.
w[ i , 0 ] = 0 .
f o r j i n r an g e ( 1 , Nymax ) :
w[ Nxmax , j ] = w[ Nxmax−1 , j ]
u [ Nxmax , j ] = u [ Nxmax−1 , j ]
# I n i t stream
# Init vorticity
# Fluid s u r f a c e
# Inlet
# C ent e rline
# Outlet
d e f beam ( ) :
# BC f o r beam
for
j i n r an g e ( 0 , H+1) :
# S id e s
w[ IL , j ] = − 2 * u [ IL −1 , j ] / ( h * h )
# Front
w[ IL+T , j ] = − 2 * u [ IL + T + 1 , j ] / ( h * h )
# Back
for
i i n r an g e ( IL , IL+T + 1 ) : w[ i , H − 1 ] = − 2 * u [ i , H ] / ( h * h ) ;
f o r i i n r an g e ( IL , IL+T+1) :
f o r j i n r an g e ( 0 , H+1) :
u [ IL , j ] = 0 .
# Front
u [ IL+T , j ] = 0 .
# Back
u [ i , H] = 0 ;
# Top
def relax ( ) :
# Relax
beam ( )
# Reset
f o r i i n r an g e ( 1 , Nxmax ) :
# Relax
for
j i n r an g e ( 1 , Nymax ) :
r1 = omega * ( ( u [ i +1 , j ]+ u [ i −1 , j ]+ u [ i , j +1]+u [ i , j −1] +
h * h *w[ i , j ] ) /4 −u [ i , j ] )
u [ i , j ] += r1
for
i i n r an g e ( 1 , Nxmax ) :
# Relax
f o r j i n r an g e ( 1 , Nymax ) :
a1 = w[ i +1 , j ] + w[ i −1 , j ] + w[ i , j +1] + w[ i , j −1]
a2 = ( u [ i , j +1] − u [ i , j − 1 ]) * ( w[ i +1 , j ] − w[ i − 1 , j ] )
a3 = ( u [ i +1 , j ] − u [ i −1 , j ] ) * ( w[ i , j +1] − w[ i , j − 1 ] )
r2 = omega * ( ( a1 − ( R / 4 . ) * ( a2 − a3 ) ) / 4 . − w[ i , j ] )
w[ i , j ] += r2
borders ( )
w h i l e ( i t e r <= 1 0 0 ) :
i t e r += 1
i f i t e r %10 == 0 : p r i n t ( i t e r )
relax ()
f o r i i n r an g e ( 0 , Nxmax+1) :
for
j i n r an g e ( 0 , Nymax+ 1 ) : u [ i , j ] = u [ i , j ] / V0 / h
x = r a n g e ( 0 , Nxmax−1) ;
y = r a n g e ( 0 , Nymax−1)
X, Y = p . meshgrid ( x , y )
def functz (u ) :
z = u [X, Y ]
return z
Z = functz (u )
fig = p . figure ()
ax = Axes3D ( f i g )
ax . p l o t _ w i r e f r a m e (X, Y , Z , c o l o r = ’ r ’ )
ax . s e t _ x l a b e l ( ’X ’ )
ax . s e t _ y l a b e l ( ’Y ’ )
ax . s e t _ z l a b e l ( ’ Stream Function ’ )
p . show ( )
