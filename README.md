Görüntü İşleme (Image Processing) Nedir?

Temel olarak Görüntü işleme (Image Processing) bir resmi ya da videoyu analiz ederek karakteristik özelliklerini tespit etmeye verilen bir isim. Karakteristik özelliği tespit etme unsuru elbette ki ayırt edici nitelik kazandırmaya dayanıyor. Günümüzde kullanılan yüz tanıma sistemlerinin tümü Görüntü işleme ile gerçekleşiyor.


PILLOW
Açılımı Python görüntü kütüphanesi olarak geçen bu kütüphane yorumlayıcının(interpreter) kapasitesini arttırmak amaçlanmıştır.
	Bu kütüphane geniş bir dosya format desteği sunar. Verimli ve güçlü görüntü işleme sunar. Kütüphanenin özü hızlı görüntü işlemeyi basit piksel formatta yapmayı amaçlar. Ayrıca genel görüntü işleme araçlarınada sahiptir.
Resim Depolama
	Pillow depolanmış ve yığın haline getirilmiş veriler(görüntüler) için idealdir.Kütüphaneyi thumbnail oluşturmak ve dosya formatları arasında geçiş yapmak için kullanabilirsiniz.
Görüntü Gösterme
	Show() metodu ile görüntüyü diske yazabilir ve harici ekran yardımıyla ekrana basılır.
Görüntü İşleme
	Nokta-nokta işlemleri gibi temel görüntü işleme fonksiyonlarını barındırır. Ayrıca görüntü boyutlandırma, çevirme ve keyfi dönüşümler yapabilmektedir. Görüntüden histogram methodu ile istatistik çıkarmayı da sağlar.


fotoNegatif Fonksiyonu : 
	Fotoğrafın datasını liste şeklinde alıp her pikseldeki r,g,b değerlerini 255’den çıkararak güncellendi. Orijinal fotoğrafın negatifi elde edilmiş oldu.

fotoGri Fonksiyonu : 
	Fotoğrafın her pikseldeki r,g,b değerlerini alıp 3’e bölündüğünde ki değeri o piksele geri atandığında elde edilen görüntü fotoğrafının gri halidir.

foto90derece Fonksiyonu :
	Fotoğrafın her pikselini alıp yeni oluşturduğum fotoğrafın ilk satırdan başlayıp sağdan yazmaya başladım. Bu şekilde matrisin transpozunu alarak fotoğrafı döndürdüm.
yeni.putpixel((j,((foto.size[0]-1)-i)), (r, g, b))

fotoTersCevir Fonksiyonu : 
	Fotoğrafın ilk pikselini alıp yeni oluşturduğum fotoğrafın en son satırına yazarak fotoğrafın tersini elde etmiş oldum.

fotoOteleme Fonksiyonu : 
	100px ötelemek için 100’e kadar olan piksellere siyah değeri atadım. 100’den sonra ise fotoğrafın ilk pikselinden itibaren yazmaya başladım.

fotoYakinlastir Fonksiyonu : 
	Fotoğrafın width ve height değerlerini 1.1 ile çarparak fotoğrafın genişliğini ve yüksekliğini değiştirdim. 

fotoUzaklastir Fonksiyonu : 
	Fotoğrafın width ve height değerlerini 0.9 ile çarparak fotoğrafın genişliğini ve yüksekliğini değiştirdim. 

fotoParlaklikArtir Fonksiyonu : 
	Fotoğrafın her pikseldeki r,g,b değerlerine belirli bir değer ekleyerek yaptım.


fotoParlaklikAzalt Fonksiyonu : 
	Fotoğrafın her pikseldeki r,g,b değerlerine belirli bir değer eksilterek yaptım.

fotoEsikleme Fonksiyonu : 
	Belirli bir eşikteki piksel değerine bakarak diğer piksellere 0 veya 1 vererek görüntüyü elde ettim.

fotoHistogram Fonksiyonu : 
	Pillow kütüphanesinin ImageOps.equalize methodunu kullanarak fotoğrafın histogramını eşitledim.

