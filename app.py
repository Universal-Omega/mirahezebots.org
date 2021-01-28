with open('templates/about.html', 'r') as file:
    contents = file.read()
    with open('templates/footer.html', 'r') as footer:
              footerr = footer.read()
    with open('templates/head.html', 'r') as head:
              headr = head.read()
              headr = headr.format(canonical='url', title='Title')
    contents = contents.format(head=headr, footer=footerr)
print(contents)
