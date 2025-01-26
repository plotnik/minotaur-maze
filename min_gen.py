# Minotaur Site Generator
# -----------------------
#
# Read YAML file and generate Streamlit pages and index according to template.
#
# .. csv-table:: Useful Links
#    :header: "Name", "URL"
#    :widths: 10 30
#   
#    "Overview of multipage apps", https://docs.streamlit.io/develop/concepts/multipage-apps/overview
#    "Define multipage apps with st.Page and st.navigation", https://docs.streamlit.io/develop/concepts/multipage-apps/page-and-navigation
#   
# ::

import yaml
import os
import textwrap

# Read YAML file
#
# ::

yaml_file = "min_gen.yml"
with open(yaml_file, 'r') as file:
    pages = yaml.safe_load(file)

#print(pages)
print("--------------------------------------------------")

# Generate ``st.Page`` objects
#
# ::

def generate_page_objects():
    result = '  st.Page("00-Minotaur.py", title="MINOTAUR MAZE"),\n'
    for page in pages:
        name = page['name']
        title = page['title']
        url = page['url']
        result += f"""  st.Page("{name}.py", title="{title}", url_path="{url}"),\n"""
    return result
  
# Generate python pages
#
# ::

for i, page in enumerate(pages):
    name = page['name']
    title = page['title']
    ru = page['ru']
    url = page['url']
    print(title)
    
    # Determine previous and next pages
    prev_page = pages[i - 1] if i > 0 else None
    next_page = pages[i + 1] if i < len(pages) - 1 else None
    
    body_name = os.path.join("content", title + ".md")
    with open(body_name, 'r', encoding='utf-8') as file:
        body = file.read()
  
    source = textwrap.dedent(f'''
        import streamlit as st

        st.header("{title}")
        st.image("img/{name}.webp", use_container_width=True)
        st.write("> **{ru}**")
        st.write("""
        ''')
    source += body
    source += '\n""")\n'
    source += '\nst.write("---")\n'
        
    # source += '\ncol1, col2, col3 = st.columns(3)\n'
    nav = '<div class="flex-container">'                     

    if prev_page != None:
        prev_name = prev_page['name']
        prev_url = prev_page['url']
        # source += textwrap.dedent(f'''
        #     with col1:
        #         st.html('<div style="text-align: center"><a href="/{prev_url}"><img src="app/static/{prev_name}-thumb.png" class="responsive-img-200"><br><img src="app/static/sword-left.png" class="responsive-img-200"></a></div>')  
        #     ''')
        nav += textwrap.dedent(f'''                 
            <div class="flex-column">
                <a href="/{prev_url}">
                    <img class="responsive-img-200" src="app/static/{prev_name}-thumb.png"><br>
                    <img class="responsive-img-200" src="app/static/sword-left.png">
                </a>                                  
            </div>                    
            ''')
    # source += textwrap.dedent(f'''
    #     with col2:
    #         st.html('<div style="text-align: center"><a href="/"><img src="app/static/00-Minotaur-thumb.png" class="responsive-img-250"></a></div>')  
    #     ''')     
    nav += textwrap.dedent(f'''                       
        <div class="flex-column">
            <a href="/">
                <img class="responsive-img-200" src="app/static/00-Minotaur-thumb.png"><br>
            </a>                                  
        </div>                                       
        ''')   
    if next_page != None:
        next_name = next_page['name']
        next_url = next_page['url']
        # source += textwrap.dedent(f'''
        #     with col3:
        #         st.html('<div style="text-align: center"><a href="/{next_url}"><img src="app/static/{next_name}-thumb.png" class="responsive-img-200"><br><img src="app/static/sword-right.png" class="responsive-img-200"></a></div>')    
        #     ''')
        nav += textwrap.dedent(f'''                   
            <div class="flex-column">
                <a href="/{next_url}">
                    <img class="responsive-img-200" src="app/static/{next_name}-thumb.png"><br>
                    <img class="responsive-img-200" src="app/static/sword-right.png">
                </a>                                  
            </div>                  
            ''')
    nav += '</div>'

    source += '\nst.html("""\n'
    source += nav
    source += '\n""")\n'
                     
    with open(name + ".py", "w", encoding="utf-8") as fout:
        fout.write(source)
  
# Generate index
#
# ::

index = f"""
import streamlit as st

with open("minotaur.css", "r", encoding="utf-8") as file:
    css = file.read()

st.html(f"<style>{{css}}</style>")

pg = st.navigation([
{generate_page_objects()}
])
pg.run()
"""

with open("index.py", "w", encoding="utf-8") as fout:
    fout.write(index)
    
# Generate TOC
#
# ::    

toc = f'''
import streamlit as st

st.header("MINOTAUR MAZE")
st.image("img/00-Minotaur.webp", use_container_width=True)
st.write("""
By [Robert Sheckley](https://en.wikipedia.org/wiki/Robert_Sheckley?wprov=sfla1)

> **ЛАБИРИНТ МИНОТАВРА**

""") 
'''

for page in pages:
    name = page['name']
    title = page['title']
    ru = page['ru']
    url = page['url']
    
    toc += textwrap.dedent(f'''
        st.write("---")
        col1, col2 = st.columns([1,3], vertical_alignment="center")  
        label = """
        **{title}**
        
        {ru}
        """

        with col1:
            st.html('<div style="text-align: center"><a href="/{url}"><img src="app/static/{name}-thumb.png" class="responsive-img-200"></a></div>') 
            #st.image("static/{name}-thumb.png", width=300)
        with col2:
            st.page_link("{name}.py", label=label, use_container_width=True)  
        ''')
    
with open("00-Minotaur.py", "w", encoding="utf-8") as fout:
    fout.write(toc)