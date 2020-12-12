liste = [[1,'“İtiqovan”, “Bayraktar” və “Harop” PUA-ları Zəfər paradında ','Vətən müharibəsində qələbəyə həsr olunan Zəfər paradında pilotsuz uçuş aparatları (PUA) nümayiş etdirilib.','BAKU.WS xəbər verir ki, PUA-ları daşıyan avtomobillər Azadlıq meydanında tribunanın önündən keçib.Paradda Azərbaycanın istehsal etdiyi “İtiqovan” zərbə PUA-ları nümayiş olunub.Daha sonra Vətən müharibəsində düşməni lərzəyə salan, düşmənə sarsıdıcı, dağıdıcı zərbələr vuran ən müasir PUA-lar olan “Bayraktar” və “Harop” Azadlıq meydanına daxil olub.'],
[2,'Prezident İlham Əliyev xalqa müraciət edib','Azərbaycan Respublikasının Prezidenti İlham Əliyev xalqa müraciət edib.','BAKU.WS müraciəti təqdim edir.Prezident İlham Əliyevin xalqa müraciəti - Əziz həmvətənlər,Böyük sevinc hissi ilə bildirirəm ki, Laçın rayonu işğaldan azad olundu. Bütün Azərbaycan xalqını bu münasibətlə ürəkdən təbrik edirəm. Laçın rayonunun işğaldan azad olunması tarixi hadisədir. Özü də bir güllə atmadan biz Laçın rayonunu qaytardıq. Düşməni buna məcbur etdik. Döyüş meydanında əldə edilmiş parlaq qələbə bu gözəl nəticəyə gətirib çıxardı ki, üç rayonumuz – Ağdam, Kəlbəcər və Laçın bizə qaytarıldı. Biz bu rayonları bir güllə atmadan, bir şəhid vermədən qaytarmışıq.'],
[3,'İlham Əliyev ümummilli lider Heydər Əliyevin anım günü ilə bağlı paylaşım edib','Prezident İlham Əliyev ümummilli lider Heydər Əliyevin anım günü ilə bağlı paylaşım edib.',"Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."],
[4,'Mehriban Əliyevadan Heydər Əliyevin anım günü ilə bağlı paylaşım','Mehriban Əliyevadan Heydər Əliyevin anım günü ilə bağlı paylaşım','It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using Content here, content here, making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for lorem ipsum will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like).'],
[5,'Xocalıda “Xocalı soyqırımı” muzeyi yaradılacaq','Şuşada Milli Azərbaycan Tarixi Muzeyinin Qarabağ tarixi filialının açılması, Xocalıda "Xocalı soyqırımı" muzeyinin yaradılması nəzərdə tutulur.','BAKU.WS Trend-ə istinadən bildirir ki, bu, AMEA tərəfindən hazırlanan Azərbaycanın işğaldan azad olunmuş ərazilərinə dair elmi tədqiqat işləri ilə bağlı Tədbirlər planında öz əksini tapıb. Tədbirlər planına əsasən, Qarabağ Geoloji Fondu Muzeyi yaradılacaq.Tədbirlər Planında Azıx mağarası bölgəsində turizmin təşkili üçün infrastrukturun hazırlanması, işğaldan azad edilmiş ərazilərdə Azərbaycan Respublikasının "Qırmızı kitab"ının hazırlanması ilə bağlı tədqiqatların aparılması, qoruq və yasaqlıqların bərpası üzrə təkliflərin hazırlanaraq müvafiq qurumlara təqdim edilməsi, Qarabağ Elmi Bölməsinin Bioresurslar İnstitutunun, Qarabağ regionuna aid bitkilərin toplandığı Nəbatat Bağının yaradılması alimlərimizin qarşısına qoyulan vəzifələrdəndir.Həmçinin Suqovuşan, Xudafərin və Qızqalası su anbarlarının, Oxçuçay, Həkəri və Bərgüşad çaylarının hidrofaunasının tədqiqi, ermənilər tərəfindən talan edilən, saxtalaşdırılan tarixi-mədəni abidələr, muzeylər, onlara daxil olan eksponat və artefaktların sənədləşdirilməsi, zərərgörmüş, dağıdılmış abidə və itmiş əşyalar haqqında məlumatların sistemləşdirilərək nümayiş etdirilməsi, arxeobioloji qalıqların müvafiq analizi də Tədbirlər planında öz əksini tapıb.Eyni zamanda M.Füzuli adına Əlyazmalar İnstitutunda mühafizə olunan Xurşidbanu Natəvanın "Gül dəftəri" əlyazmasının YUNESKO-nun "Dünya yaddaşı" reyestrinə daxil edilməsinin, Milli Azərbaycan Ədəbiyyatı Muzeyinin vaxtilə Şuşa şəhərində fəaliyyət göstərmiş Xurşidbanu Natəvan adına Qarabağ filialının bərpasının, Arxeologiya və Etnoqrafiya İnstitutunda Qarabağ arxeoloji mərkəzinin yaradılması planlaşdırılır.Qeyd edək ki, Tədbirlər planı ümumilikdə 2021-2035-ci illəri əhatə edir.'],
[6,'title3','subtitle3','content3']
]

from flask import Flask, render_template,request, redirect,url_for
app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return render_template('news.html', news = liste)

@app.route('/search',methods=['GET','POST'])
def search():
    if request.method == 'POST':
        data = list()
        searched = request.form.get('search')
        for i in liste:
            if searched in i[1]:
                data.append(i)
        return render_template('search.html',searched = searched, data = data)
    else:
        return redirect('/')



@app.route('/detail/<string:id>')
def detail(id):
    data = list()
    for i in liste:
        if i[0] == int(id):
            data = i
    return render_template('detail.html', data = data)

if __name__ == '__main__':
    app.run(debug = True)