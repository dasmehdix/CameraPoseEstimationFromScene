# CameraPoseEstimationFromScene
## Ön çalışma
3 adet görüntü, 1. görüntüye ait 2 boyutlu öznitelik noktaları ve aynı özniteliklere ait 3 boyutlu dünya koordinat sistemine uygun noktalar verilmiştir. Öncelikle **"img1.png"** görüntüsündeki öznitelik noktalarını, diğer görüntülerde bulabilmek için OpenCv'nin sağladığı çeşitli teknikler(feature matching & template matching) kullanılmıştır. Bu teknikler, diğer görsellerdeki 20 öznitelik noktalarının hepsini doğru bulamadığı farkedilmiştir. Bunun üzerine **"Img2"** ve **"Img3"** görsellerindeki öznitelikler manuel olarak çıkartılmıştır. Noktalar **"image2data2d.npy"** ve **"image3data2d.npy"** dosyalarında numpy array formatında kaydedilmiştir.

## Çözüm
Kameranın farklı görüntülerdeki 6 eksenli(DoF) pozunun algılanabilmesi için diğer görsellerdeki öznitelik noktaları çıkartılmıştır. Çıkarılan noktalar **"featureVisualization.py"** çalışmasında görselleştirilmiştir. Kamera pozu algılanması için "Rotation" ve "Translation" matrislerinin çıkarılması gerekmektedir. Bu matrisler OpenCV'nin sağladığı **solvePnp** fonksiyonuyla elde edilmiştir. Dünya koordinat sistemine ait 3 boyutlu noktalar, görsellere ait 2 boyutlu noktalar, kamera matrisi ve distorsiyon matrisi(sıfır kabul edilmiştir) kullanılarak hesaplama sağlanmıştır. Her bir görsele ait rotation ve translation matrisleri elde edildikten sonra, referans görsel olan 1. görselden çıkartılarak, 1. görsele göreceli olan rotation ve translation matrisleri hesaplanmıştır. Hesaplanan göreceli camera pozları rotation ve translation ayrı olarak görselleştirimiştir. Bütün bu işlemler **"cameraPoseEstimation.py"** dosyasında yer almaktadır. Görselleştirme yapılırken ilk görüntüyü referans aldığımız için ilk görüntüye ait rotation ve translation matrisleri sıfır kabul edimiştir.

### Her Bir Görsele Ait Öznitelik Noktaları 
![image1](https://github.com/dasmehdix/CameraPoseEstimationFromScene/blob/main/outputs/featuresOnImages.png)


### Translation Görselleştirmesi (1. Görsel Referans Alınmıştır)
![image2](https://github.com/dasmehdix/CameraPoseEstimationFromScene/blob/main/outputs/RelativeCameraPose.png)

### Rotation Görselleştirmesi (1. Görsel Referans Alınmıştır)
![image3](https://github.com/dasmehdix/CameraPoseEstimationFromScene/blob/main/outputs/Realative_rotation.png)

## Alternatif Linkler
Yapılan çalışmalara ait girdiler ve çıktılar alternatif olarak kaggle platformu üzerinden hem veriseti olarak hem kod parçaları olarak paylaşılmıştır. Ayrıca **translation-rotation-matrixes.ipynb** dosyası üzerinden çıktılar görülebimektedir. [Kaggle Link](https://www.kaggle.com/dasmehdixtr/translation-rotation-matrixes)

## Alternatif Çalışmalar
Öncelikle öznitelik noktaları manuel olarak çıkarılmak yerine gürbüz çalışan bir "feature matching" modeliyle diğer görsellerdeki noktalar elde edilebilir. Ben bu çalışmada pozu elde etmek için sadece **solvePnp** fonksiyonunu kullandım. Bu fonksiyon aldığı parametrelere göre farklı algoritmaları kullanabilmektedir. Ben bu çalışmada "Direct Linear Transfrom" yöntemini kullandım fakat "Levenberg-Marquardt Optimization" gibi çeşitli yöntemler de kullanılıp en uygun çözüm seçilebilirdi. Ayrıca **solvePnpRansac** ve **stereoCalibrate** fonksiyonları da aynı sonuçları farklı yöntemlerle üretebilmektedir.
