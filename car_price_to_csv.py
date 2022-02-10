from bs4 import BeautifulSoup
import csv

html_source = ""

with open("/Users/onurkskc/Documents/beautifulsoup/sahibindencom/7_mercedes.html", "r") as f:
    html_source = f.read()

soup = BeautifulSoup(html_source, "html.parser")

araba_modeli = soup.find_all("td", attrs={"class": "searchResultsTagAttributeValue"})
ilan_ozellikler = soup.find_all("td", attrs={"class": "searchResultsAttributeValue"})
fiyat = soup.find_all("td", attrs={"class": "searchResultsPriceValue"})
ilan_tarih = soup.find_all("td", attrs={"class": "searchResultsDateValue", })
konum_verisi = soup.find_all("td", attrs={"class": "searchResultsLocationValue"})


model_list = []
#print(len(ilan_ozellikler))
for model in araba_modeli:
    model_list.append(model.get_text().strip())

ilan_list = []
km_list = []
renk_list = []
for yil in range(0, len(ilan_ozellikler), 3):
    ilan_list.append(ilan_ozellikler[yil].get_text().strip())
    km_list.append(ilan_ozellikler[yil+1].get_text().strip())
    renk_list.append(ilan_ozellikler[yil+2].get_text().strip())

fiyat_list = []
for f in fiyat:
    fiyat_list.append(f.get_text().strip())

tarih_list = []
for tarih in ilan_tarih:
    tarih_text = tarih.get_text().strip()
    tarih_text = tarih_text.replace("\n", "")
    tarih_text = tarih_text[:-4] + " " + tarih_text[-4:]
    tarih_list.append(tarih_text)

konum_list = []
for konum in konum_verisi:
    konum_text = konum.get_text().strip()
    caps = 1
    #print(konum_text)
    for letter in konum_text[1:]:
        if letter.isupper() == True:
            break
        else:
            caps += 1
    #print(caps)
    konum_text_space = konum_text[:caps] + " " + konum_text[caps:]
    konum_list.append(konum_text_space)       

#print(konum_list)
#print(tarih_list)
#print(fiyat_list)
#print(model_list)
#print(ilan_list)
zipped_lists = zip(model_list, ilan_list, km_list, renk_list, tarih_list, fiyat_list, konum_list)
#print(list(zipped_lists)[0])

field_names = ["Model Adi", "Ilan List", "KM", "Renk", "Tarih", "Fiyat", "Konum"]


with open("sahibinden.com_data.csv", "a+", encoding="utf-8") as f:
    writer_obj = csv.writer(f, delimiter=";")

    writer_obj.writerow("\n")
    writer_obj.writerows(zipped_lists)
    

