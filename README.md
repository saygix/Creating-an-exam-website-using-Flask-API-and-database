# **CREATING AN EXAM WEBSITE USING FLASK API AND DATABASE** 

### **Proje Açıklaması**
Bu proje, Flask web framework'ü kullanarak geliştirilen bir dinamik quiz uygulamasıdır. Kullanıcılar rastgele yapay zeka konularında sorularla bir sınava girebilir ve sonuçları anında görüntüleyebilir. Flask, SQLite veritabanı, HTML, CSS ve PythonAnywhere dağıtımı ile geliştirilmiştir.

### **Özellikler**
- Yapay zeka konularında rastgele sorular içeren quiz.
- Soru ve cevaplar veritabanından çekilir.
- Kullanıcı yanıtlarını değerlendirir ve sonuçları anında gösterir.
- Kullanıcı arayüzü: HTML, CSS.
- API entegrasyonu için hazır.

---

## **İçindekiler**
- [Kurulum](#kurulum)
- [Kullanım](#kullanım)
- [Proje Yapısı](#proje-yapısı)
- [Yapılandırma](#yapılandırma)
- [Veritabanı](#veritabanı)
- [Dağıtım](#dağıtım)
- [Katkı Sağlama](#katkı-sağlama)

---

## **Kurulum**

### **Gereksinimler**
Bu projeyi çalıştırmak için aşağıdaki yazılımların bilgisayarınızda kurulu olması gerekir:
- Python 3.11.5
- Flask
- SQLite

### **Adım Adım Kurulum**
1. Bu repository'yi klonlayın:
    ```bash
    git clone https://github.com/kullanıcı_adınız/proje_ismi.git
    cd proje_ismi
    ```

2. Sanal ortam oluşturun ve etkinleştirin:
    ```bash
    python -m venv venv
    source venv/bin/activate  # Windows: venv\Scripts\activate
    ```

3. Gerekli bağımlılıkları yükleyin:
    ```bash
    pip install -r requirements.txt
    ```

4. Veritabanını oluşturun:
    ```bash
    flask shell
    from app import db
    db.create_all()
    exit()
    ```

5. Uygulamayı başlatın:
    ```bash
    flask run
    ```

---

## **Kullanım**

1. Web tarayıcınızda şu adrese gidin: `http://127.0.0.1:5000/`
2. Quiz uygulamasında soruları cevaplayın.
3. Sonuçları anında görün.

---

## **Proje Yapısı**
```python
proje_ismi/
│
├── app.py               # Ana Flask uygulama dosyası
├── instance/
│   └── config.py        # Yapılandırma dosyası (opsiyonel)
├── static/
│   └── style.css        # Stil dosyası (CSS)
├── templates/
│   ├── base.html        # Ana HTML şablonu
│   ├── quiz.html        # Quiz sayfası şablonu
│   └── result.html      # Sonuç sayfası şablonu
├── README.md            # Proje açıklaması
├── requirements.txt     # Gerekli bağımlılıklar
└── database.db          # SQLite veritabanı (oluşturduktan sonra)
```
---

## **Yapılandırma**

- **config.py** dosyasında yapılandırma ayarlarını düzenleyebilirsiniz. Örneğin, DEBUG modunu aktif hale getirebilirsiniz:
    ```python
    DEBUG = True
    ```

---

## **Veritabanı**
Bu proje SQLite kullanır. `app.py` içinde veritabanı ayarlarını yapabilir ve yeni tablolar ekleyebilirsiniz. Veritabanı modeli aşağıdaki gibidir:

```python
class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_text = db.Column(db.String(200), nullable=False)
    answer_a = db.Column(db.String(100), nullable=False)
    answer_b = db.Column(db.String(100), nullable=False)
    answer_c = db.Column(db.String(100), nullable=False)
    correct_answer = db.Column(db.String(1), nullable=False)
 ```
---

## Dağıtım

Proje PythonAnywhere gibi bir platformda dağıtılmak üzere hazırlanmıştır. Dağıtım adımları şunlardır:

1. PythonAnywhere'de bir hesap oluşturun.
2. Yeni bir web uygulaması oluşturun ve "Flask" framework'ünü seçin.
3. Proje dosyalarınızı yükleyin (örneğin: `app.py`, `templates/`, `static/`).
> **Not:** PythonAnywhere'de klasör yüklemesi yapılamamaktadır. Bu nedenle, klasörlerinizi **zipleyerek** yükleyin. Yükledikten sonra, terminal üzerinden zip dosyasını çıkartmak için aşağıdaki komutu kullanın:
```bash
unzip dosya_adi.zip
``` 
4. WSGI yapılandırmasını güncelleyin:

    ```python
    import sys
    sys.path.insert(0, '/home/kullanıcı_adı/myflaskapp')

    from app import app as application
    ```

5. Web uygulamanızı yeniden başlatın ve test edin.

---

## Katkı Sağlama

Katkıda bulunmak için lütfen bir pull request gönderin. Katkıda bulunmak isteyenler için kurulum ve test sürecini kolaylaştırmak amacıyla daha fazla bilgi sağlanabilir.

---
> **Yayınlanan siteyi ziyaret edin**: [https://saygix.pythonanywhere.com](https://saygix.pythonanywhere.com) 
