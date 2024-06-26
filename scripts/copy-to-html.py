import os
import re

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
src_dir = os.path.join(parent_dir, 'src')


with open(os.path.join(src_dir, 'routes/work-with-us/copy.md')) as copy_file:
  lines = copy_file.read().splitlines()

  elements = []
  curr_element = ""

  for line in lines:
    line = line.strip()

    if line == "" and curr_element.strip() != "":
      if not curr_element.strip().startswith("<h3"):
        curr_element = curr_element.replace("<<<", "</div>")
        curr_element += "</p>"

      curr_element.replace("<br/>", "\n")
      curr_element = re.sub(r'_(.*?)_', r'<i class="italic">\1</i>', curr_element)
      curr_element = re.sub(r'\*\*(.*?)\*\*', r'<bold class="font-bold">\1</bold>', curr_element)
      curr_element.replace("**", "<bold>")
      elements.append(curr_element)
      curr_element = ""
      continue

    if line.startswith("###"):
      found_arrows = ">>>" in line
      line = line.replace("###", "").replace(">>>", "")
      curr_element += f"""<h3 class="text-left text-2xl md:text-3xl font-bold {'cursor-pointer' if found_arrows else ''}" _="on click toggle .hidden on the next <div/> then toggle .expanded on the first .triangle in me">"""
      curr_element += line
      if found_arrows:
        curr_element += """<span class="triangle"></span>"""
      curr_element += "</h3>"
      if found_arrows:
        curr_element += '<div class="flex hidden flex-col gap-6">'
      continue

    if line != "" and curr_element == "":
      curr_element += "<p>"

    if line == "" and curr_element == "":
      continue

    curr_element += f" {line}"

with open(os.path.join(src_dir, 'routes/work-with-us/copy.html'), 'w') as output_file:
  output_file.write("\n".join(elements))
