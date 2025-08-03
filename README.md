# QuizAI - Otomatik Çoktan Seçmeli Quiz Oluşturucu

![Streamlit](https://img.shields.io/badge/Streamlit-%23000?style=for-the-badge&logo=streamlit&logoColor=white)  
![OpenAI](https://img.shields.io/badge/OpenAI-%23000?style=for-the-badge&logo=openai&logoColor=white)

---

## Proje Hakkında

QuizAI, **Streamlit** ile oluşturulmuş basit ve kullanımı kolay bir web uygulamasıdır.  
OpenAI GPT-4 modeli kullanılarak verilen konu başlığına göre otomatik olarak 5 adet çoktan seçmeli sınav sorusu oluşturur.  

Eğitimciler, öğrenciler veya quiz hazırlamak isteyen herkes için hızlıca test soruları üretmek için tasarlanmıştır.

---

## Özellikler

- Kullanıcıdan konu başlığı alır.
- OpenAI GPT-4 API ile ilgili konu hakkında 5 soru üretir.
- Her soru 4 seçenekli ve doğru cevabı içerir.
- Kullanımı kolay ve sade arayüz.
- Sorular textarea içinde gösterilir, kopyalanmaya hazır.

---

## Kurulum ve Kullanım

### Gereksinimler

- Python 3.7 ve üzeri  
- OpenAI API anahtarı (https://platform.openai.com/account/api-keys)  
- Gerekli kütüphaneler:

```bash
pip install streamlit openai
API Anahtarının Ayarlanması
Projenizde API anahtarını doğrudan kod içine yazmak yerine, güvenlik için çevresel değişken olarak ayarlayın.

Örneğin:

Windows (PowerShell):

powershell
Kopyala
Düzenle
$env:OPENAI_API_KEY="your_api_key_here"
Mac/Linux (bash):

bash
Kopyala
Düzenle
export OPENAI_API_KEY="your_api_key_here"
Uygulamayı Çalıştırma
Terminalden proje klasörüne gidip:

bash
Kopyala
Düzenle
streamlit run app.py
Komutunu çalıştırın. Tarayıcınızda açılan sayfada konu başlığını girip quiz oluşturabilirsiniz.

Kod Yapısı
app.py: Streamlit uygulaması ana dosyası.

generate_quiz(topic): OpenAI API çağrısı yaparak quiz soruları üretir.

Kullanıcı arayüzü, Streamlit bileşenleri ile oluşturulmuştur.

Dikkat Edilmesi Gerekenler
OpenAI API anahtarınızı gizli tutun.

Ücretsiz kullanım kotalarınıza dikkat edin.

Kodda try-except blokları ile API hatalarına karşı koruma sağlanmıştır.

Katkıda Bulunma
Bu proje açık kaynaklıdır. İyileştirme önerileri için pull request veya issue açabilirsiniz.

Lisans
MIT Lisansı
