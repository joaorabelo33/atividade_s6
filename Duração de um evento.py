def tempo_seg(a):
    horas=a//3600
    minutos= (a % 3600)//60
    segundos= a - (horas *3600 + minutos * 60)
    return horas,minutos,segundos

a=int(input())
h,m,s=tempo_seg(a)
print(f'{h}:{m}:{s}')
