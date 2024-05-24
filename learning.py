vtft66tyttyvtyvytvyvy

def operations(d,e,cmnd):

    if cmnd == 's':
        return sum(d,e)
    if cmnd == 'd':
        return diff(d,e)    
    if cmnd == 'm':
        return mul(d,e)
    if cmnd == 'f':
        return div(d,e)
    


a=3
b=5
cmnd = 'f'
c = operations(a,b,cmnd)
print(c,type(a),type(b))

