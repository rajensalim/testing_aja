import time
import math
mn = 938.277594
mp = 939.5714475
c = 299792458
for i in range(1,999): #iterasi
    atom = input('Masukkan Nama Atom:') #input data
    Aa = input('Masukkan Nomor Massa Atom :')
    Zz = input('Masukkan Nomor Atom :')
    A=int(Aa)
    Z=int(Zz)
    N = A-Z
    print('Atom',atom,'dengan nomor massa:',A,',nomor atom:',Z,',neutron:',N)
    print('Apakah benar ?(ya/tidak)')
    tes = input('')
    if tes == 'ya':
        print('Menghitung Energi Ikat') #menghitung energi ikat
        print('Persamaan : [B(A,Z)=Zmp+(A-Z)mn-M(A,Z)]c^2')
        time.sleep(3)
        Zmp = Z*mp
        Nmn = N*mn
        print('Masukkan Nilai Massa Eksperimen: (dalam amu)')
        m_az=input()
        maz = float(m_az)
        Maz = maz*931.5
        print('Nilai Zmp =',Zmp,'MeV/c^2')
        print('Nilai (A-Z)mn =',Nmn,'MeV/c^2')
        print('Nilai M(A,Z) =',Maz,'MeV/c^2')
        print('Nilai B(A,Z) adalah:')
        time.sleep(3)
        Baz=Zmp+Nmn-Maz
        print(Baz,'MeV')
        time.sleep(3)
        print('Nilai Energi Ikat per Nukleon adalah:')
        Baza=Baz/A
        print(Baza,'MeV/nukleon')
        time.sleep(3)
        print('Apakah ingin menghitung Massa SMEF ? (ya/tidak)')
        tes1=input()
        if tes1 == 'ya': #menghitung massa SMEF
            print('Oke kita lanjut ya')
            print('----------------------------------------------------------------------------------------------------------')
            #ambil data
            time.sleep(1)
            if (Z%2)==0 and (N%2)==0: #jika genap-genap
                av=14
                ass=13
                ac=0.60
                aa=19
                sigma=34/(A**(3/4))
                Baz1=(av*A)-(ass*(A**(2/3)))-(ac*(Z*(Z-1))/(A**(1/3)))-(aa*((N-Z)**2)/A)+sigma
                print('Proton dan Neutron Genap-Genap:')
                time.sleep(2)
                print('Persamaan B(A,Z)=avA-asA^2/3-asZ(Z-1)/A^1/3-ac((N-Z)^2)/A+sigma')
                time.sleep(2)
                print(Baz1,'MeV*c^2')
                Baz1c2=Baz1/(c**2)
                time.sleep(2)
                print('Maka Massa Atom',A,'-',atom,'Metode SMEF adalah:')
                time.sleep(1)
                print('Persamaan: M(A,Z)=Zmp+(A-Z)mn- B(A,Z)/c^2')
                time.sleep(2)
                Maz1=Zmp+Nmn-Baz1c2
                print(Maz1,'MeV')
                Maz1amu=Maz1/931.5
                print(Maz1amu,'u')
                selisih1=Maz1amu-maz
                print('Selisih Massa SMEF dengan Eksperimen:')
                print(selisih1,'u')
                time.sleep(2)
                print('-----------------------------------------------------------------------------------------------')
                print('Apakah ingin menghitung Energi ikat dan Massa lagi ? (ya/tidak)')
                tes2 = input()
                if tes2 == 'ya':
                    print('Oke, sebentar ya')
                    print('------------------------------------------------------------------------------------------------------')
                else:
                    print('Oke, terima kasih telah menggunakan kalkulator Energi Ikat dan Massa SMEF!')
                    break
            elif (Z%2)!=0 and (N%2)!=0: #jika ganjil-ganjil
                av = 16
                ass = 18
                ac = 0.72
                aa = 23.5
                sigma = 11/(A**(1/2))
                Baz1 = (av*A)-(ass*(A**(2/3)))-(ac*(Z*(Z-1))/(A**(1/3)))-(aa*((N-Z)**2)/A)+sigma
                print('Proton dan Neutron Ganjil-Ganjil:')
                time.sleep(2)
                print('Persamaan B(A,Z)=avA-asA^2/3-asZ(Z-1)/A^1/3-ac((N-Z)^2)/A+sigma')
                time.sleep(2)
                print(Baz1,'MeV*c^2')
                Baz1c2 = Baz1/(c**2)
                time.sleep(2)
                print('Maka Massa Atom',A,'-',atom,'Metode SMEF adalah:')
                time.sleep(1)
                print('Persamaan: M(A,Z)=Zmp+(A-Z)mn-B(A,Z)/c^2')
                time.sleep(2)
                Maz1 = Zmp+Nmn-Baz1c2
                print(Maz1,'MeV')
                Maz1amu = Maz1/931.5
                print(Maz1amu,'u')
                selisih1=Maz1amu-maz
                print('Selisih Massa SMEF dengan Eksperimen:')
                print(selisih1, 'u')
                time.sleep(2)
                print('-----------------------------------------------------------------------------------------------')
                print('Apakah ingin menghitung Energi ikat dan Massa lagi ? (ya/tidak)')
                tes2=input()
                if tes2=='ya':
                    print('Oke, sebentar ya')
                    print('------------------------------------------------------------------------------------------------------')
                else:
                    print('Oke, terima kasih telah menggunakan kalkulator Energi Ikat dan Massa SMEF!')
                    break
            else: #jika ganjil-genap
                print('Karena Ganjil-Genap, maka tidak ada perhitungannya ')
                time.sleep(2)
                print('-----------------------------------------------------------------------------------------------')
                print('Apakah ingin menghitung Energi ikat dan Massa lagi ? (ya/tidak)')
                tes3=input()
                if tes3=='ya':
                    print('Oke, sebentar ya')
                    print('------------------------------------------------------------------------------------------------------')
                else:
                    print('Oke, terima kasih telah menggunakan kalkulator Energi Ikat dan Massa SMEF!')
                    break
        elif tes1 == 'tidak':
            print('Apakah ingin menghitung Energi Ikat lagi ? (ya/tidak)')
            tes4=input()
            if tes4=='ya':
                print('Oke, sebentar ya')
                print('----------------------------------------------------------------------------------------------------------')
                time.sleep(2)
            else:
                print('Oke terima kasih telah menggunakan kalkulator Energi Ikat dan Massa SMEF!')
                break
    else:
        print('Tolong input ulang ya')
        print('------------------------------------------------------------------------------------------------------------------')
time.sleep(2)
print('--------------------------------------------------------------------------------------------------------------------------')
print('Apakah ingin menghitung energi separasi 1 proton atau 1 neutron? (ya/tidak)')
tes5=input()
print('--------------------------------------------------------------------------------------------------------------------------')
if tes5=='ya':
    time.sleep(2)
    for o in range(1,999):#iterasi
        print('Untuk separasi 1 proton maka nomor massa (A) dan nomor atom (Z) akan berubah sehingga atom ikut berubah')
        print('Untuk separasi 1 neutron maka hanya nomor massa (A) yang berubah sehingga atom tidak ikut berubah')
        print('Silahkan input lagi')
        time.sleep(1)
        atoms = input('Masukkan Nama Atom:') #input data
        Aas = input('Masukkan Nomor Massa Atom :')
        Zzs = input('Masukkan Nomor Atom :')
        As = int(Aas)
        Zs = int(Zzs)
        Ns = As - Zs
        print('Atom', atoms, 'dengan nomor massa:', As, ',nomor atom:', Zs, ',neutron:', Ns)
        print('Apakah benar ?(ya/tidak)')
        tes6 = input('')
        if tes6 == 'ya':
            if Ns==N:#untuk proton, maka nilai neutron sama antara 2 atom
                print('Anda Ingin Menghitung Energi Separasi Proton:')
                print('Menghitung Energi Ikat')
                print('Persamaan : [B(A,Z)=Zmp+(A-Z)mn-M(A,Z)]c^2')
                time.sleep(3)
                Zmps = Zs*mp
                Nmns = Ns*mn
                print('Masukkan Nilai Massa Eksperimen: (dalam amu)')
                m_azs = input()
                mazs = float(m_azs)
                Mazs = mazs * 931.5
                print('Nilai Zmp =', Zmps, 'MeV/c^2')
                print('Nilai (A-Z)mn =', Nmns, 'MeV/c^2')
                print('Nilai M(A,Z) =', Mazs, 'MeV/c^2')
                print('Nilai B(A,Z) adalah:')
                time.sleep(3)
                Bazs = Zmps+Nmns-Mazs
                print(Bazs, 'MeV')
                time.sleep(3)
                print('Nilai Energi Ikat per Nukleon adalah:')
                Bazas = Bazs/As
                print(Bazas, 'MeV/nukleon')
                time.sleep(3)
                Bazsep=math.fabs(Baz-Bazs)
                print('Sehingga Energi yang dibutuhkan untuk melepaskan 1 proton sebesar:')
                print(Bazsep,'MeV')
                time.sleep(2)
                print('-----------------------------------------------------------------------------------------------')
                print('Apakah ingin menghitung Energi Separasi lagi ? (ya/tidak)')
                tes7 = input()
                if tes7 == 'ya':
                    print('Oke, sebentar ya')
                    print('------------------------------------------------------------------------------------------------------')
                else:
                    print('Oke, terima kasih telah menggunakan kalkulator Energi Separasi!')
                    break
            else: #untuk neutron,nomor neutron tidak akan sama antara 2 atom
                print('Anda Ingin Menghitung Energi Separasi Neutron:')
                print('Menghitung Energi Ikat')
                print('Persamaan : [B(A,Z)=Zmp+(A-Z)mn-M(A,Z)]c^2')
                time.sleep(3)
                Zmps = Zs * mp
                Nmns = Ns * mn
                print('Masukkan Nilai Massa Eksperimen: (dalam amu)')
                m_azs = input()
                mazs = float(m_azs)
                Mazs = mazs * 931.5
                print('Nilai Zmp =', Zmps, 'MeV/c^2')
                print('Nilai (A-Z)mn =', Nmns, 'MeV/c^2')
                print('Nilai M(A,Z) =', Mazs, 'MeV/c^2')
                print('Nilai B(A,Z) adalah:')
                time.sleep(3)
                Bazs = Zmps + Nmns - Mazs
                print(Bazs, 'MeV')
                time.sleep(3)
                print('Nilai Energi Ikat per Nukleon adalah:')
                Bazas = Bazs / As
                print(Bazas, 'MeV/nukleon')
                time.sleep(3)
                Bazsep = math.fabs(Baz - Bazs)
                print('Sehingga Energi yang dibutuhkan untuk melepaskan 1 Neutron sebesar:')
                print(Bazsep, 'MeV')
                time.sleep(2)
                print('-----------------------------------------------------------------------------------------------')
                print('Apakah ingin menghitung Energi Separasi lagi ? (ya/tidak)')
                tes8 = input()
                if tes8 == 'ya':
                    print('Oke, sebentar ya')
                    print(
                        '------------------------------------------------------------------------------------------------------')
                else:
                    print('Oke, terima kasih telah menggunakan kalkulator Energi Separasi!')
                    break
        else:
            print('Tolong input ulang ya')
            print('------------------------------------------------------------------------------------------------------------')
else:
    print('Oke terima kasih telah menggunakan kalkulator Energi Separasi!')
    exit()









