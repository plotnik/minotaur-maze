
import streamlit as st

st.header("MINOTAUR MAZE")
st.image("img/00-Minotaur.webp", use_container_width=True)
st.write("""
By [Robert Sheckley](https://en.wikipedia.org/wiki/Robert_Sheckley?wprov=sfla1)

> **ЛАБИРИНТ МИНОТАВРА**

""") 

st.write("---")
col1, col2 = st.columns([1,3], vertical_alignment="center")  
label = """
**1. How Theseus got his first Minotauring job.**

Как Тесей получил свою первую работу с минотаврами.
"""

with col1:
    st.html('<div style="text-align: center"><a href="/theseus"><img src="app/static/01-Theseus-thumb.png" width=150></a></div>') 
    #st.image("static/01-Theseus-thumb.png", width=300)
with col2:
    st.page_link("01-Theseus.py", label=label)  

st.write("---")
col1, col2 = st.columns([1,3], vertical_alignment="center")  
label = """
**2. Mann. T. goes forth after the Minotaur.**

Некто Т. отправляется за Минотавром
"""

with col1:
    st.html('<div style="text-align: center"><a href="/t"><img src="app/static/02-T-thumb.png" width=150></a></div>') 
    #st.image("static/02-T-thumb.png", width=300)
with col2:
    st.page_link("02-T.py", label=label)  

st.write("---")
col1, col2 = st.columns([1,3], vertical_alignment="center")  
label = """
**3. I hate to blame Dædalus for everything**

Конечно не хотелось бы во всём винить Дедала
"""

with col1:
    st.html('<div style="text-align: center"><a href="/blame"><img src="app/static/03-Blame-thumb.png" width=150></a></div>') 
    #st.image("static/03-Blame-thumb.png", width=300)
with col2:
    st.page_link("03-Blame.py", label=label)  

st.write("---")
col1, col2 = st.columns([1,3], vertical_alignment="center")  
label = """
**4. Dædalus.**

Дедал
"""

with col1:
    st.html('<div style="text-align: center"><a href="/daedalus"><img src="app/static/04-Daedalus-thumb.png" width=150></a></div>') 
    #st.image("static/04-Daedalus-thumb.png", width=300)
with col2:
    st.page_link("04-Daedalus.py", label=label)  

st.write("---")
col1, col2 = st.columns([1,3], vertical_alignment="center")  
label = """
**5. Theseus. About the Maze.**

Тесей. О Лабиринте.
"""

with col1:
    st.html('<div style="text-align: center"><a href="/autosave"><img src="app/static/05-Autosave-thumb.png" width=150></a></div>') 
    #st.image("static/05-Autosave-thumb.png", width=300)
with col2:
    st.page_link("05-Autosave.py", label=label)  

st.write("---")
col1, col2 = st.columns([1,3], vertical_alignment="center")  
label = """
**6. The Maze. Dædalus’ Achievement.**

Лабиринт. Достижение Дедала.
"""

with col1:
    st.html('<div style="text-align: center"><a href="/maze"><img src="app/static/06-Maze-thumb.png" width=150></a></div>') 
    #st.image("static/06-Maze-thumb.png", width=300)
with col2:
    st.page_link("06-Maze.py", label=label)  

st.write("---")
col1, col2 = st.columns([1,3], vertical_alignment="center")  
label = """
**7. Ariadne Telephones.**

Ариадна звонит по телефону.
"""

with col1:
    st.html('<div style="text-align: center"><a href="/ariadne"><img src="app/static/07-Ariadne-thumb.png" width=150></a></div>') 
    #st.image("static/07-Ariadne-thumb.png", width=300)
with col2:
    st.page_link("07-Ariadne.py", label=label)  

st.write("---")
col1, col2 = st.columns([1,3], vertical_alignment="center")  
label = """
**8. The Minotaur.**

Минотавр
"""

with col1:
    st.html('<div style="text-align: center"><a href="/minotaur"><img src="app/static/08-Minotaur-thumb.png" width=150></a></div>') 
    #st.image("static/08-Minotaur-thumb.png", width=300)
with col2:
    st.page_link("08-Minotaur.py", label=label)  

st.write("---")
col1, col2 = st.columns([1,3], vertical_alignment="center")  
label = """
**9. The Maze Larger than the World.**

Лабиринт больше чем мир
"""

with col1:
    st.html('<div style="text-align: center"><a href="/world"><img src="app/static/09-Maze-thumb.png" width=150></a></div>') 
    #st.image("static/09-Maze-thumb.png", width=300)
with col2:
    st.page_link("09-Maze.py", label=label)  

st.write("---")
col1, col2 = st.columns([1,3], vertical_alignment="center")  
label = """
**10. The Spool of Thread.**

Клубок ниток
"""

with col1:
    st.html('<div style="text-align: center"><a href="/spool"><img src="app/static/10-Spool-thumb.png" width=150></a></div>') 
    #st.image("static/10-Spool-thumb.png", width=300)
with col2:
    st.page_link("10-Spool.py", label=label)  

st.write("---")
col1, col2 = st.columns([1,3], vertical_alignment="center")  
label = """
**11. Theobombus, leading cybernetician**

Теобомбас, ведущий кибернетик
"""

with col1:
    st.html('<div style="text-align: center"><a href="/theobombus"><img src="app/static/11-Theobombus-thumb.png" width=150></a></div>') 
    #st.image("static/11-Theobombus-thumb.png", width=300)
with col2:
    st.page_link("11-Theobombus.py", label=label)  

st.write("---")
col1, col2 = st.columns([1,3], vertical_alignment="center")  
label = """
**12. King Minos.**

Царь Минос
"""

with col1:
    st.html('<div style="text-align: center"><a href="/minos"><img src="app/static/12-Minos-thumb.png" width=150></a></div>') 
    #st.image("static/12-Minos-thumb.png", width=300)
with col2:
    st.page_link("12-Minos.py", label=label)  

st.write("---")
col1, col2 = st.columns([1,3], vertical_alignment="center")  
label = """
**13. How Knossos was Peopled.**

Как был заселен Кносс
"""

with col1:
    st.html('<div style="text-align: center"><a href="/knossos"><img src="app/static/13-Knossos-thumb.png" width=150></a></div>') 
    #st.image("static/13-Knossos-thumb.png", width=300)
with col2:
    st.page_link("13-Knossos.py", label=label)  

st.write("---")
col1, col2 = st.columns([1,3], vertical_alignment="center")  
label = """
**14. In the Maze of Juxtapositions.**

В Лабиринте Противоположностей
"""

with col1:
    st.html('<div style="text-align: center"><a href="/juxtapositions"><img src="app/static/14-Juxtapositions-thumb.png" width=150></a></div>') 
    #st.image("static/14-Juxtapositions-thumb.png", width=300)
with col2:
    st.page_link("14-Juxtapositions.py", label=label)  

st.write("---")
col1, col2 = st.columns([1,3], vertical_alignment="center")  
label = """
**15. Sorrows of the Minotaur.**

Печали Минотавра
"""

with col1:
    st.html('<div style="text-align: center"><a href="/unicorn"><img src="app/static/15-Unicorn-thumb.png" width=150></a></div>') 
    #st.image("static/15-Unicorn-thumb.png", width=300)
with col2:
    st.page_link("15-Unicorn.py", label=label)  

st.write("---")
col1, col2 = st.columns([1,3], vertical_alignment="center")  
label = """
**16. Although Minos is king, Dædalus**

Хоть Минос и царь, но Дедал
"""

with col1:
    st.html('<div style="text-align: center"><a href="/theory"><img src="app/static/16-Daedalus-thumb.png" width=150></a></div>') 
    #st.image("static/16-Daedalus-thumb.png", width=300)
with col2:
    st.page_link("16-Daedalus.py", label=label)  

st.write("---")
col1, col2 = st.columns([1,3], vertical_alignment="center")  
label = """
**17. The Hornectomy.**

Роготомия
"""

with col1:
    st.html('<div style="text-align: center"><a href="/hornectomy"><img src="app/static/17-Hornectomy-thumb.png" width=150></a></div>') 
    #st.image("static/17-Hornectomy-thumb.png", width=300)
with col2:
    st.page_link("17-Hornectomy.py", label=label)  

st.write("---")
col1, col2 = st.columns([1,3], vertical_alignment="center")  
label = """
**18. The Midas Touch.**

Прикосновение Мидаса
"""

with col1:
    st.html('<div style="text-align: center"><a href="/touch"><img src="app/static/18-Midas-thumb.png" width=150></a></div>') 
    #st.image("static/18-Midas-thumb.png", width=300)
with col2:
    st.page_link("18-Midas.py", label=label)  

st.write("---")
col1, col2 = st.columns([1,3], vertical_alignment="center")  
label = """
**19. The Profit Motive.**

Корыстные мотивы
"""

with col1:
    st.html('<div style="text-align: center"><a href="/profit"><img src="app/static/19-Profit-thumb.png" width=150></a></div>') 
    #st.image("static/19-Profit-thumb.png", width=300)
with col2:
    st.page_link("19-Profit.py", label=label)  

st.write("---")
col1, col2 = st.columns([1,3], vertical_alignment="center")  
label = """
**20. The Attack of the Self Pity Plant.**

Нападение Растения Самосожаления
"""

with col1:
    st.html('<div style="text-align: center"><a href="/selfpity"><img src="app/static/20-Self-Pity-Plant-thumb.png" width=150></a></div>') 
    #st.image("static/20-Self-Pity-Plant-thumb.png", width=300)
with col2:
    st.page_link("20-Self-Pity-Plant.py", label=label)  

st.write("---")
col1, col2 = st.columns([1,3], vertical_alignment="center")  
label = """
**21. Minotaur & Midas.**

Минотавр и Мидас
"""

with col1:
    st.html('<div style="text-align: center"><a href="/mm"><img src="app/static/21-Minotaur-Midas-thumb.png" width=150></a></div>') 
    #st.image("static/21-Minotaur-Midas-thumb.png", width=300)
with col2:
    st.page_link("21-Minotaur-Midas.py", label=label)  

st.write("---")
col1, col2 = st.columns([1,3], vertical_alignment="center")  
label = """
**22. Dædalus Dispenses with Causality.**

Дедал отменяет причинно-следственную связь
"""

with col1:
    st.html('<div style="text-align: center"><a href="/causality"><img src="app/static/22-Causality-thumb.png" width=150></a></div>') 
    #st.image("static/22-Causality-thumb.png", width=300)
with col2:
    st.page_link("22-Causality.py", label=label)  

st.write("---")
col1, col2 = st.columns([1,3], vertical_alignment="center")  
label = """
**23. The Chinese Waiter—Theseus & Minotaur.**

Китайский официант. Тесей и Минотавр
"""

with col1:
    st.html('<div style="text-align: center"><a href="/chinese"><img src="app/static/23-Chinese-Waiter-thumb.png" width=150></a></div>') 
    #st.image("static/23-Chinese-Waiter-thumb.png", width=300)
with col2:
    st.page_link("23-Chinese-Waiter.py", label=label)  

st.write("---")
col1, col2 = st.columns([1,3], vertical_alignment="center")  
label = """
**24. Minotaur Meets Minerva.**

Минотавр встречает Минерву
"""

with col1:
    st.html('<div style="text-align: center"><a href="/minerva"><img src="app/static/24-Minerva-thumb.png" width=150></a></div>') 
    #st.image("static/24-Minerva-thumb.png", width=300)
with col2:
    st.page_link("24-Minerva.py", label=label)  

st.write("---")
col1, col2 = st.columns([1,3], vertical_alignment="center")  
label = """
**25. The Alien Observer.**

Инопланетный Агент
"""

with col1:
    st.html('<div style="text-align: center"><a href="/alien"><img src="app/static/25-Alien-thumb.png" width=150></a></div>') 
    #st.image("static/25-Alien-thumb.png", width=300)
with col2:
    st.page_link("25-Alien.py", label=label)  

st.write("---")
col1, col2 = st.columns([1,3], vertical_alignment="center")  
label = """
**26. The Telephone Booth.**

Телефонная будка
"""

with col1:
    st.html('<div style="text-align: center"><a href="/telephone"><img src="app/static/26-Telephone-thumb.png" width=150></a></div>') 
    #st.image("static/26-Telephone-thumb.png", width=300)
with col2:
    st.page_link("26-Telephone.py", label=label)  

st.write("---")
col1, col2 = st.columns([1,3], vertical_alignment="center")  
label = """
**27. Girl Named Phædra.**

Девушка по имени Федра
"""

with col1:
    st.html('<div style="text-align: center"><a href="/phaedra"><img src="app/static/27-Phaedra-thumb.png" width=150></a></div>') 
    #st.image("static/27-Phaedra-thumb.png", width=300)
with col2:
    st.page_link("27-Phaedra.py", label=label)  

st.write("---")
col1, col2 = st.columns([1,3], vertical_alignment="center")  
label = """
**28. Modalities of the Reclinational.**

Модальности релаксационного.
"""

with col1:
    st.html('<div style="text-align: center"><a href="/reclination"><img src="app/static/28-Reclination-thumb.png" width=150></a></div>') 
    #st.image("static/28-Reclination-thumb.png", width=300)
with col2:
    st.page_link("28-Reclination.py", label=label)  

st.write("---")
col1, col2 = st.columns([1,3], vertical_alignment="center")  
label = """
**29. Phone Call to Naxos.**

Звонок на Наксос
"""

with col1:
    st.html('<div style="text-align: center"><a href="/naxos"><img src="app/static/29-Naxos-thumb.png" width=150></a></div>') 
    #st.image("static/29-Naxos-thumb.png", width=300)
with col2:
    st.page_link("29-Naxos.py", label=label)  

st.write("---")
col1, col2 = st.columns([1,3], vertical_alignment="center")  
label = """
**30. Falling Through the Story.**

Провалившись в историю
"""

with col1:
    st.html('<div style="text-align: center"><a href="/falling"><img src="app/static/30-Falling-thumb.png" width=150></a></div>') 
    #st.image("static/30-Falling-thumb.png", width=300)
with col2:
    st.page_link("30-Falling.py", label=label)  
