gan = [9,0,1,2,3,4,5,6,7,8]
ji =['F','G','H','I','J','K','L','A','B','C','D','E']

# 2013 = F9

year = int(input())
gap = year -2013

year_gan = gan[gap%10]
year_ji = ji[gap%12]
print(f'{year_ji}{year_gan}')