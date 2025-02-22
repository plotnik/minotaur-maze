
import streamlit as st

st.header("17. The Hornectomy.")
st.image("img/17-Hornectomy.webp", use_container_width=True)
st.write("> **Роготомия**")
st.write("""
The Minotaur has decided to take the big step and get the hornectomy that will transform him from a Minotaur into a unicorn. He will go to Asclepius, the master surgeon of the maze, and have one horn surgically removed. The remaining horn will be off center, but he will still be able to pass himself off as an Asymmetrical or Lopsided Unicorn.

> Минотавр решил сделать решительный шаг и пройти роготомию[^1], которая превратит его из Минотавра в единорога. Он пойдёт к Асклепию, главному хирургу лабиринта, и удалит один рог. Оставшийся рог будет не по центру, но он всё равно сможет выдавать себя за асимметричного или кривого единорога.

[^1]: Роготомия: операция по удалению рога.

But there’s a difficulty. The Minotaur doesn’t have the sizable fee that Asclepius charges for cosmetic surgery. Where will he get the money? None of his friends have any. And there are no jobs in the maze, only roles, which pay only in non-negotiable units of fame or in the small change of notoriety.

> Но тут есть трудность. У Минотавра нет достаточной суммы, которую Асклепий берёт за косметическую операцию. Где он достанет деньги? У его друзей тоже их нет. А в лабиринте нет работы, только роли, за которые платят лишь ненастоящими единицами славы или мелочью скандальной известности.


""")

st.write("---")

st.html("""
<div class="flex-container">
<div class="flex-column">
    <a href="/theory">
        <img class="responsive-img-200" src="app/static/16-Daedalus-thumb.png"><br>
        <img class="responsive-img-200" src="app/static/sword-left.png">
    </a>                                  
</div>                    

<div class="flex-column">
    <a href="/">
        <img class="responsive-img-200" src="app/static/00-Minotaur-thumb.png"><br>
    </a>                                  
</div>                                       

<div class="flex-column">
    <a href="/touch">
        <img class="responsive-img-200" src="app/static/18-Midas-thumb.png"><br>
        <img class="responsive-img-200" src="app/static/sword-right.png">
    </a>                                  
</div>                  
</div>
""")
