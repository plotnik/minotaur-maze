
import streamlit as st

st.header("9. The Maze Larger than the World.")
st.image("img/09-Maze.webp", use_container_width=True)
st.write("> **Лабиринт больше чем мир**")
st.write("""
For a long time it was impossible to be sure of anything. That was because indeterminacy ruled the maze world, and nobody liked it but Dædalus. The inhabitants detested it. Dædalus, they said, you have gone too far. No good will come of this, you’re letting yourself be seduced by a mere proposition. Come, be reasonable, lay down a few hard facts, promulgate some operating instructions; at least give us some defaults. We need a little order around here. A little order is all we ask for, Dædalus; it keeps things nice, please, just for us, okay?

> Долгое время ни в чем нельзя было быть уверенным. Это происходило потому, что миром лабиринта правил [принцип неопределенности](https://ru.wikipedia.org/wiki/%D0%9F%D1%80%D0%B8%D0%BD%D1%86%D0%B8%D0%BF_%D0%BD%D0%B5%D0%BE%D0%BF%D1%80%D0%B5%D0%B4%D0%B5%D0%BB%D1%91%D0%BD%D0%BD%D0%BE%D1%81%D1%82%D0%B8?wprov=sfla1), и никто, кроме Дедала, этому не радовался. Жители этот принцип ненавидели. «Дедал, — говорили они, — ты зашел слишком далеко. Из этого ничего хорошего не выйдет, ты позволяешь себе соблазниться простой гипотезой. Будь благоразумен, задай несколько твердых фактов, издай какие-то инструкции; хотя бы дай нам несколько стандартов. Нам нужно немного порядка. Немного порядка — это все, о чем мы просим, Дедал; это делает жизнь лучше, пожалуйста, только для нас, хорошо?»


Dædalus wouldn’t listen. He considers his critics negligible, old-world sentimentalists in love with obsolete ideas. The old order that they dream of never was, and will not be again.

> Дедал не хотел слушать. Он считал своих критиков не стоящими внимания, старомодными романтиками, влюбленными в устаревшие идеи. Тот старый порядок, о котором они мечтают, никогда не существовал и никогда не вернется.

The people in the maze, despite Dædalus, despite the rule of uncertainty, have set up some rules for themselves, just to avoid the chaos, and in order that a few things could be planned.

> Люди в лабиринте, несмотря на Дедала и принцип неопределенности, установили для себя некоторые правила, чтобы избежать хаоса и чтобы хоть что-то можно было планировать.

This matter of the Minotaur, for example. Many Theseuses came through these parts looking for the fabulous beast. A regular industry had sprung up to supply all of them. You could stop at any newsstand and buy a Standard Guide to Minotauronics, with thumb index and handy chart. You could try Hermes’ adaptation of Pythagoras’ Negative Inference System. There were many other methods and all of them worked to some extent, not through their intrinsic merit but because, for reasons not yet fully understood, the maze shaped its interminable topology to the intentions of the players within it, so that, although you cannot plan to find what you are looking for, you also cannot hope to escape it.

> Возьмем, например, эту историю с Минотавром. Множество Тесеев проходило через эти места в поисках мифического зверя. Возникла целая индустрия, обслуживающая их всех. В любом киоске можно было купить «Стандартное руководство по Минотавронике» с алфавитным указателем и удобной схемой. Можно было попробовать адаптацию Гермеса «Системы отрицательных выводов» Пифагора. Существовали и многие другие методы, и все они работали в какой-то степени не благодаря своей внутренней ценности, а потому что, по причинам, еще не до конца понятным, лабиринт приспосабливал свою бесконечную топологию к намерениям игроков внутри него. Таким образом, хотя нельзя планировать найти то, что ищешь, нельзя также надеяться избежать этого.
""")

st.write("---")

st.html("""
<div class="flex-container">
<div class="flex-column">
    <a href="/minotaur">
        <img class="responsive-img-200" src="app/static/08-Minotaur-thumb.png"><br>
        <img class="responsive-img-200" src="app/static/sword-left.png">
    </a>                                  
</div>                    

<div class="flex-column">
    <a href="/">
        <img class="responsive-img-200" src="app/static/00-Minotaur-thumb.png"><br>
    </a>                                  
</div>                                       

<div class="flex-column">
    <a href="/spool">
        <img class="responsive-img-200" src="app/static/10-Spool-thumb.png"><br>
        <img class="responsive-img-200" src="app/static/sword-right.png">
    </a>                                  
</div>                  
</div>
""")
