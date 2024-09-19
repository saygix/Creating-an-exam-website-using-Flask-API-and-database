from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Blog gönderileri için sahte veri
posts = [
    {
        "id": 1,
        "title": "Flask API ile Dinamik Quiz Web Sitesi Oluşturma",
        "content": """
        Flask nedir ve neden kullanılır? Dinamik web siteleri oluşturmanın avantajları.
        Proje Planlaması: Projenizin hedefleri ve kapsamı. Gerekli araçlar ve teknolojiler.
        Flask API Kurulumu: Flask'ı kurma ve yapılandırma. Basit bir API endpoint oluşturma.
        Veritabanı Entegrasyonu: SQLAlchemy ile veritabanı bağlantısı. CRUD işlemleri için API endpoints oluşturma.
        Dinamik Quiz Oluşturma: Quiz sorularını veritabanında nasıl saklayabilirsiniz? Soruları ve cevapları rastgele nasıl getirebilirsiniz?
        Web Arayüzü: HTML ve CSS ile kullanıcı arayüzü tasarımı. Flask ile HTML şablonlarını nasıl render edersiniz?
        Elde edilen sonuçlar ve kullanıcı geri bildirimleri. Karşılaşılan zorluklar ve çözüm önerileri.
        """,
        "image": "/static/images/quiz_web_site.jpg"
    },
    {
        "id": 2,
        "title": "Yapay Zeka ile Görüntü Sınıflandırma",
        "content": """
        Görüntü sınıflandırmanın önemi ve uygulama alanları. CNN ve LSTM nedir?
        Veri Setleri: Malaria ve MNIST veri setlerinin tanıtımı. Veri ön işleme adımları.
        Model Mimarisi: CNN ile özellik çıkarımı. LSTM ile zaman serisi veya uzun vadeli bağımlılıkların analizi.
        Model Eğitimi ve Testi: Eğitim süreci ve hiperparametre ayarları. Sonuçların değerlendirilmesi ve performans metrikleri.
        Sonuçlar ve Performans Karşılaştırması: CNN ve LSTM'nin kombinasyonunun etkileri. Sonuçların analizi ve grafiklerle gösterimi.
        Elde edilen sonuçların özeti. Gelecek çalışmalar ve iyileştirme önerileri.
        """,
        "image": "/static/images/ai_image_classification.jpg"
    },
    {
        "id": 3,
        "title": "Flask ile RESTful API Tasarımı",
        "content": """
        RESTful API nedir ve neden önemlidir? Flask ile RESTful API oluşturmanın avantajları.
        Temel Kavramlar: REST mimarisi ve HTTP metodları. JSON veri formatı.
        Flask ile API Geliştirme: Temel API endpoint'leri oluşturma. Veri doğrulama ve hata yönetimi.
        İyi Uygulamalar: API belgeleri oluşturma. API güvenliği ve kimlik doğrulama.
        Test ve Dağıtım: API'nizi test etme yöntemleri. Flask uygulamanızı nasıl dağıtırsınız?
        API tasarımı için genel öneriler ve ipuçları. Karşılaşılan sorunlar ve çözüm önerileri.
        """,
        "image": "/static/images/restful_api.jpg"
    }
]

# Ana sayfa rotası
@app.route('/post/<int:post_id>', methods=['GET', 'POST'])
def post(post_id):
    post = next((p for p in posts if p["id"] == post_id), None)
    if request.method == 'POST':
        comment = request.form.get('comment')
        # Burada yorumları işleyebilirsiniz (veritabanına kaydedebilir veya bellekte tutabilirsiniz)
        # Bu örnekte sadece POST işlemini işliyoruz, yorumları depolamak için ek kod gerekebilir
        print(f"New comment: {comment}")
        return redirect(url_for('post', post_id=post_id))
    if post:
        return render_template('post.html', post=post)
    else:
        return "Post not found", 404

if __name__ == "__main__":
    app.run(debug=True)
@app.route('/blog1')
def blog1():
    return render_template('blog1.html')

@app.route('/blog2')
def blog2():
    return render_template('blog2.html')

@app.route('/blog3')
def blog3():
    return render_template('blog3.html')

