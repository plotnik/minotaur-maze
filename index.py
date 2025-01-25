
import streamlit as st

with open("minotaur.css", "r", encoding="utf-8") as file:
    css = file.read()

st.html(f"<style>{css}</style>")

pg = st.navigation([
  st.Page("00-Minotaur.py", title="MINOTAUR MAZE"),
  st.Page("01-Theseus.py", title="1. How Theseus got his first Minotauring job.", url_path="theseus"),
  st.Page("02-T.py", title="2. Mann. T. goes forth after the Minotaur.", url_path="t"),
  st.Page("03-Blame.py", title="3. I hate to blame Dædalus for everything", url_path="blame"),
  st.Page("04-Daedalus.py", title="4. Dædalus.", url_path="daedalus"),
  st.Page("05-Autosave.py", title="5. Theseus. About the Maze.", url_path="autosave"),
  st.Page("06-Maze.py", title="6. The Maze. Dædalus’ Achievement.", url_path="maze"),
  st.Page("07-Ariadne.py", title="7. Ariadne Telephones.", url_path="ariadne"),
  st.Page("08-Minotaur.py", title="8. The Minotaur.", url_path="minotaur"),
  st.Page("09-Maze.py", title="9. The Maze Larger than the World.", url_path="world"),
  st.Page("10-Spool.py", title="10. The Spool of Thread.", url_path="spool"),
  st.Page("11-Theobombus.py", title="11. Theobombus, leading cybernetician", url_path="theobombus"),
  st.Page("12-Minos.py", title="12. King Minos.", url_path="minos"),
  st.Page("13-Knossos.py", title="13. How Knossos was Peopled.", url_path="knossos"),
  st.Page("14-Juxtapositions.py", title="14. In the Maze of Juxtapositions.", url_path="juxtapositions"),
  st.Page("15-Unicorn.py", title="15. Sorrows of the Minotaur.", url_path="unicorn"),
  st.Page("16-Daedalus.py", title="16. Although Minos is king, Dædalus", url_path="theory"),
  st.Page("17-Hornectomy.py", title="17. The Hornectomy.", url_path="hornectomy"),
  st.Page("18-Midas.py", title="18. The Midas Touch.", url_path="touch"),
  st.Page("19-Profit.py", title="19. The Profit Motive.", url_path="profit"),
  st.Page("20-Self-Pity-Plant.py", title="20. The Attack of the Self Pity Plant.", url_path="selfpity"),
  st.Page("21-Minotaur-Midas.py", title="21. Minotaur & Midas.", url_path="mm"),
  st.Page("22-Causality.py", title="22. Dædalus Dispenses with Causality.", url_path="causality"),
  st.Page("23-Chinese-Waiter.py", title="23. The Chinese Waiter—Theseus & Minotaur.", url_path="chinese"),
  st.Page("24-Minerva.py", title="24. Minotaur Meets Minerva.", url_path="minerva"),
  st.Page("25-Alien.py", title="25. The Alien Observer.", url_path="alien"),
  st.Page("26-Telephone.py", title="26. The Telephone Booth.", url_path="telephone"),
  st.Page("27-Phaedra.py", title="27. Girl Named Phædra.", url_path="phaedra"),
  st.Page("28-Reclination.py", title="28. Modalities of the Reclinational.", url_path="reclination"),
  st.Page("29-Naxos.py", title="29. Phone Call to Naxos.", url_path="naxos"),
  st.Page("30-Falling.py", title="30. Falling Through the Story.", url_path="falling"),

])
pg.run()
