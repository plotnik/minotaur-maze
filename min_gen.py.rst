Minotaur Site Generator
-----------------------

Read YAML file and generate Streamlit pages and index according to template.

.. csv-table:: Useful Links
   :header: "Name", "URL"
   :widths: 10 30
   
   "Overview of multipage apps", https://docs.streamlit.io/develop/concepts/multipage-apps/overview
   "Define multipage apps with st.Page and st.navigation", https://docs.streamlit.io/develop/concepts/multipage-apps/page-and-navigation
   
::

  # import streamlit as st
  import yaml
  import os
  import textwrap

  home_directory = "minotaur-maze"

Read YAML file

::

  yaml_file = "min_gen.yml"
  with open(yaml_file, 'r') as file:
      pages = yaml.safe_load(file)

  #print(pages)
  print("--------------------------------------------------")

Get list of pages

::
    
  def get_page_list():
      names = [page['name'] for page in pages]
      # Prepend None to the list
      return [None] + names

  def init_pages():
      result = ""
      for page in pages:
          name = page['name']
          title = page['title']
          result += f"""  st.Page("{name}.py", title="{title}"),\n"""
      return result
    
Generate pages

::

  for page in pages:
      name = page['name']
      title = page['title']
      print(title)
    
      body_name = os.path.join("..", "content", title + ".md")
      with open(body_name, 'r', encoding='utf-8') as file:
          body = file.read()
    
      source = textwrap.dedent(f'''
          import streamlit as st

          st.header("{title}")
          st.image("{name}.webp", use_container_width=True)
          st.write("""
          ''')
      source += body
      source += '\n---\n'
      source += '\n""")\n'
 
      page_name = os.path.join(home_directory, name + ".py")
      with open(page_name, "w", encoding="utf-8") as fout:
          fout.write(source)
    
Generate index

::

  index = f"""
  import streamlit as st

  st.html('''
      <style>
          .stMain {{
              background-color: #e5ddc7;
          }}
      </style>
      ''')

  if "page" not in st.session_state:
      st.session_state.page = None
  
  PAGES = {get_page_list()}

  page = st.session_state.page
  pg = st.navigation([
  {init_pages()}
  ])
  pg.run()
  """

  index_name = os.path.join(home_directory, "index.py")
  with open(index_name, "w", encoding="utf-8") as fout:
      fout.write(index)