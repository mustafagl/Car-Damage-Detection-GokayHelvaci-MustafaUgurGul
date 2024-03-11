# Araç Hasar Tespit Modeli

Bu proje, TensorFlow ve Keras kullanılarak U-Net mimarisiyle oluşturulan bir araç hasar tespit modelini içermektedir. Model, araçlardaki hasarları tespit etmek için derin öğrenme tekniklerini kullanır.

## Veri Hazırlama

- Araç hasar veri seti ve Stanford araba veri seti kullanılmıştır.
- Görüntülerin boyutları ve isimleri düzenlenmiştir.

## Ön İşleme

- Görüntüler modelin işleyebileceği formata dönüştürülmüştür.
- Görüntüler rastgele döndürülerek veri artırımı yapılmıştır.
- Veri seti eğitim, doğrulama ve test setlerine ayrılmıştır.

## Model Oluşturma

- U-Net mimarisi kullanılarak bir derin öğrenme modeli oluşturulmuştur.
- Özel bir kayıp fonksiyonu (Dice coefficient loss) tanımlanmıştır.

## Eğitim

- Model, eğitim veri seti üzerinde eğitilmiştir.
- Erken durdurma ve model kaydetme gibi teknikler kullanılmıştır.

## Test

- Model, test veri seti üzerinde değerlendirilmiştir.
- Modelin performansı, doğruluk oranı ve kayıp değeri ile ölçülmüştür.

## Görselleştirme

- Modelin eğitim ve doğrulama doğruluğu ile kaybı, epok sayısına göre grafiklerle gösterilmiştir.
- Test veri setinden örnek görüntüler ve bunların model tarafından tahmin edilen maskeleri görselleştirilmiştir.

## Sonuç

- Modelin test veri setindeki başarımı %95.40 olarak bulunmuştur.
- Confusion matrisi ile modelin hasarlı ve hasarsız sınıflandırmaları detaylı bir şekilde incelenmiştir.
