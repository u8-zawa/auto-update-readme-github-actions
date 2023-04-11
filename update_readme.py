import os

with open('README_template.md', 'r') as f:
    template = f.read()

version = os.getenv('VERSION', 'N/A')

readme = template.replace('${VERSION}', version)

with open('README.md', 'w') as f:
    f.write(readme)
