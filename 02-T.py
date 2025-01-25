
import streamlit as st

st.header("2. Mann. T. goes forth after the Minotaur.")
st.image("img/02-T.webp", use_container_width=True)
st.write("> **Некто Т. отправляется за Минотавром**")
st.write("""
After lunch they went straight to the command post. The redheaded woman did not go with them. Between chapters, she received a telegram telling her that she had won the Miss Abilene beauty contest and that oil had been discovered on the family estate in Sulk City, Florida. So departs a sulky and uncooperative character. Let it stand as a warning to others.

> После обеда они сразу отправились на командный пункт. Рыжеволосая женщина не пошла с ними. Когда предыдущая глава закончилась, а эта еще не началась, она получила телеграмму, в которой сообщалось, что она выиграла конкурс красоты "Мисс Абилин", и что на семейном участке в Салк-Сити, Флорида, обнаружили нефть. Так уходит мрачный и несговорчивый персонаж. Пусть это будет предупреждением для других.

The Command Post was filled with that air of tension and imminent disaster that accompanies so many bestsellers. Updates on the location and predilections of the Minotaur were flashed on television screens. Technicians hurried back and forth with equation-laden clipboards, making science fiction possible. 

> Командный пункт был наполнен той атмосферой напряжения и надвигающейся катастрофы, которая сопутствует многим бестселлерам. Обновления о местонахождении и намерениях Минотавра мелькали на экранах телевизоров. Техники спешили туда-сюда с планшетами, заполненными уравнениями, делая научную фантастику реальностью.

There was a low hum of electricity, and the odd stuttering sound of the Phase Two Synthesizer, sending forth its mood forecasts. 

> Слышался низкий электрический гул  и странное постукивание  Синтезатора Второй Фазы, передающего свои прогнозы настроений. 

In spite of all this, Theseus did not fail to notice the dark-haired girl carrying a small stack of computer printouts, which were created for the sole purpose of giving her something to do with her hands. She was adorable, the short skirt, the high heels, the pertness, and a look passed between them, not even an entire look, more of a looklet, or even a glancelet, and yet what future spells of sexual discombobulation were revealed in that stomach-twisting glance that tells you that she has noticed you and is considering thinking about you.

> Несмотря на всё это, Тесей не смог не заметить темноволосую девушку с небольшой стопкой компьютерных распечаток, созданных исключительно для того, чтобы занять её руки. Она была очаровательна — короткая юбка, высокие каблуки, задорность, и между ними пролетел взгляд, даже не весь взгляд, а скорее взглядик, или даже полувзгляд, и всё же какие будущие заклинания сексуальной растерянности были раскрыты в этом щемящем сердце взгляде, говорящем о том, что она заметила его и, возможно, подумывает о нём.

Theseus didn’t know that now. He had just noticed that the green and red indicators on the Minotaur sweep search indicator had crossed and locked. The Minotaur had been located!

> Тесей ещё не знал об этом. Он только что заметил, что зелёные и красные индикаторы на устройстве поиска Минотавра пересеклись и зафиксировались. Минотавр был найден!

The high priest of the Technical Scribes, in his green and orange uniform, with the flared gloves and pleated cape, wrote the numbers on a piece of paper and gave it to him.

> Верховный жрец Технических Писцов, в своей зелено-оранжевой униформе с расширяющимися перчатками и плиссированным плащом, записал цифры на листке бумаги и передал его ему.

“Coordinates these the,” he said, his odd construction and sibilant delivery marking him as an Asper Futile from Gnagi Prime.

> "Координаты это есть," - сказал он, его странная фраза и шипящий голос выдавали в нём аспера-футиля с Гнаги Прайм.

Theseus studied the numbers, committing them to memory. Theseus didn’t really have a very good memory. Things never stayed in it for long. Theseus shouldered his knapsack, filled with Minotaur finding and killing equipment, and headed for the outskirts of town where the trail of the Minotaur began, stopping only at a grocery store on his way out of town to cash his Monster Advance. It was a Greek grocery store, as you might imagine.

> Тесей изучил цифры, запоминая их. Память у Тесея была не очень хорошая; вещи редко задерживались в ней надолго. Он взвалил на плечи рюкзак, наполненный снаряжением для поиска и уничтожения Минотавра, и направился к окраинам города, где начинался след Минотавра. По пути он остановился только в продуктовом магазине, чтобы обналичить свой аванс на охоту за чудовищем. Как можно догадаться, это был греческий магазин.
""")

st.write("---")

col1, col2, col3 = st.columns(3)

with col1:
    st.html('<div style="text-align: center"><a href="/theseus"><img src="app/static/01-Theseus-thumb.png" width=200><br><img src="app/static/sword-left.png" width=200></a></div>')  

with col2:
    st.html('<div style="text-align: center"><a href="/"><img src="app/static/00-Minotaur-thumb.png" width=250></a></div>')  

with col3:
    st.html('<div style="text-align: center"><a href="/blame"><img src="app/static/03-Blame-thumb.png" width=200><br><img src="app/static/sword-right.png" width=200></a></div>')    
