import requests
import re
from lxml import html
from bs4 import BeautifulSoup as bs

nim = []
prodi = []
with open('KodeProdiITB','r') as f:
    for line in f:
        kode = re.split(r'[\s]\t',line.rstrip('\t\n'))
        nim.append(kode[0])
        prodi.append(kode)
result = []
notFound = 0
# print(nim)

def scrap(uid):
    global notFound
    url = 'https://nic.itb.ac.id/manajemen-akun/pengecekan-user'
    PAYLOAD = {
        'uid': uid
    }
    COOKIES = {
        'SSESS3a3aca27d869446c6564e6eba553c0d3': 'jTpyXKV0nzVKdzXAFdef5Ea6jKiZLbw5k3dC_5G_YlY'
    }
    s = requests.session()
    login_req = s.post(url, data = PAYLOAD, cookies = COOKIES)

    if('tidak ditemukan' in login_req.text):
        print("UID :", uid, "tidak ditemukan")
        notFound += 1
    else:
        soup = bs(login_req.text, 'lxml')
        tbody = soup.find('table', id = 'tabel')
        rows = tbody.findAll('tr')
        arruser = []
        for tr in rows:
            cols = tr.findAll('td')
            content = cols[0].string
            if('NIM' in content):
                nim = cols[2].string.split(', ')
                if (not len(nim)>1):
                    nim.append('00000000')
                arruser.append(nim)
            if('Nama Lengkap' in content):
                name = (str) (cols[2].string)
                arruser.append(name)
        result.append(arruser)
        notFound = 0

def main():
    global notFound
    global result
    for code in nim :
        if(int(code) > 168 and int(code) < 200):
            result = []
            for i in range(7,10):
                for j in range(1,601):
                    if(j<10):
                        scrap(f'{code}1{i}00{j}')
                    elif(j>=10 and j<100):
                        scrap(f'{code}1{i}0{j}')
                    else:
                        scrap(f'{code}1{i}{j}')
                    if notFound >= 10:
                        notFound = 0
                        break
            print(result)
            with open(f'{code}', 'w') as f:
                for user in result:
                    for data in user:
                        if isinstance(data, list):
                            for usernim in data:
                                f.write(usernim)
                                f.write(' ')    
                        else:
                            f.write(data)
                    f.write('\n')

if __name__ == '__main__':
    main()