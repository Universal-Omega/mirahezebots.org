from flask import Flask, send_file
from MirahezeBots_jsonparser import jsonparser as jp

app = Flask(__name__)


def display_content(path, config):
    with open(config['templatedpages'][path], 'r') as file:
        contents = file.read()
        with open('templates/navbar.html', 'r') as navbar:
            navbarr = navbar.read()
            index = 'href="/"'
            docs = 'href="documentation"'
            contribs = 'href="contribs"'
            about = 'href="about"'
            sourcecode = 'href="https://bots.miraheze.org/wiki/Source_Code"'
            if path == 'index':
                index = 'class="active" href="/"'
            if path == 'about':
                about = 'class="active" href="about"'
            if path == 'documentation':
                doocs = 'class="active" href="documentation"'
            if path == 'contribs':
                contribs = 'class="active" href="contribs"'
            navbarr = navbarr.format(
                indexlink=index,
                documentationlink=docs,
                contribslink=contribs,
                aboutlink=about,
                sourcecodelink=sourcecode,
                )
        with open('templates/footer.html', 'r') as footer:
                  footerr = footer.read()
        with open('templates/head.html', 'r') as head:
                  headr = head.read()
                  if path == 'index':
                      canonical = config['canonical-prefix']  # index is not canonical
                  else:
                      canonical = config['canonical-prefix']+path
                  headr = headr.format(canonical=canonical, title='Title')
        contents = contents.format(head=headr, footer=footerr, navbar=navbarr)
    return contents


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    if path.endswith('.html'):
        path = path[:5]  # ignore .html endings
    if path == "":
        path = "index"  # rewrite empty path to index
    config = jp.createdict('config.json')
    if path in config['directshow']:
        return send_file(config['directshow'][path])
    if path in config['templatedpages']:
        return display_content(path, config)
    

if __name__ == '__main__':
    app.run(debug=True)

