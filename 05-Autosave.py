
import streamlit as st

st.header("5. Theseus. About the Maze.")
st.image("img/05-Autosave.webp", use_container_width=True)
st.write("> **Тесей. О Лабиринте.**")
st.write("""
So here is Theseus searching for the Minotaur in the labyrinth which Dædalus constructed for King Minos back in the great days of Atlantean civilization.

> И вот Тесей ищет Минотавра в лабиринте, который Дедал построил для царя Миноса в великие дни  цивилизации атлантов.

It is a day, a featureless day, a day like so many others in the labyrinth.

> Это обычный день, безликий день, день, как и многие другие в лабиринте.

The labyrinth, or maze, is a magical creation, a testing ground for heroes, a place of simultaneous realities and repetitions. The maze is the highest achievement of Atlantean scientific alchemy, the supreme monument to a civilization already in decline and soon to be destroyed by natural cataclysm, but destined to live forever through Dædalus’ art.

> Лабиринт, это магическое творение, испытательный полигон для героев, место одновременных реальностей и повторений. Лабиринт — высшее достижение научной алхимии атлантов, величайший памятник цивилизации, уже находящейся в упадке и скоро обреченной на уничтожение природным катаклизмом, но предназначенной жить вечно благодаря искусству Дедала.

The basic situation is simple enough: Theseus has to find the Minotaur, a monstrous creature part human, part beast. Theseus must kill the Minotaur and then find his way back to the everyday world.

> Ситуация достаточно проста: Тесею нужно найти Минотавра, чудовище, наполовину человека, наполовину зверя. Тесей должен убить Минотавра, а затем найти путь обратно в обычный мир.

The situation has been played out many times, with many different outcomes, and with different people in the leading roles. I’m not the only Theseus there’s been or the only one there’ll be. I’m just the current one; the one in the narrator position, though not, actually, the narrator of the entire story. I’ll explain that a little later. Just now I’m Theseus, a professional Minotaur-killer, or rather, one of a long line of Theseuses, who have been recurring with almost sickening regularity ever since Dædalus introduced Recurrence into his scheme for the maze more complicated than the world it was modeled upon.

> Эта ситуация разыгрывалась много раз, с различными исходами и разными людьми в главных ролях. Я не единственный Тесей, который был, и не единственный, который будет. Я просто нынешний; тот, кто сейчас в роли рассказчика, хотя на самом деле не я рассказываю всю историю. Позже я это объясню. Сейчас я Тесей, профессиональный убийца Минотавра, или, скорее, один из длинной череды Тесеев, которые появляются с почти тошнотворной регулярностью с тех пор, как Дедал ввел Автосохранение в свою схему лабиринта, более сложного, чем мир, по образцу которого он был создан.


""")

st.write("---")

col1, col2, col3 = st.columns(3)

with col1:
    st.html('<div style="text-align: center"><a href="/daedalus"><img src="app/static/04-Daedalus-thumb.png" width=200><br><img src="app/static/sword-left.png" width=200></a></div>')  

with col2:
    st.html('<div style="text-align: center"><a href="/"><img src="app/static/00-Minotaur-thumb.png" width=250></a></div>')  

with col3:
    st.html('<div style="text-align: center"><a href="/maze"><img src="app/static/06-Maze-thumb.png" width=200><br><img src="app/static/sword-right.png" width=200></a></div>')    
