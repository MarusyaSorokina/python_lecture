from jinja2 import Environment, FileSystemLoader
from jinja2 import Template


file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

tm = env.get_template('homef.html')
msg = tm.render()

print(msg)