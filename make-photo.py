# Copyright 2018 Akifumi Fujita
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import argparse
import os
import sys
import urllib.request

from bs4 import BeautifulSoup
from bs4 import Tag
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM

def get_github_html(user):
    url = "https://github.com/" + user
    with urllib.request.urlopen(url) as response:
        html = response.read()
        return html

def format_svg(svg):
    svg['xmlns'] = "http://www.w3.org/2000/svg"
    svg['height'] = 432
    svg['width'] = 768

    rect = Tag(name='rect')
    rect['x'] = '0'
    rect['y'] = '0'
    rect['width'] = '768'
    rect['height'] = '432'
    rect['fill'] = 'gray'

    svg.find("g").insert_before(rect)
    svg.find("g")["transform"] = "translate(40, 160)"
    return svg

parser = argparse.ArgumentParser()
parser.add_argument("-u", dest="user", default=None, help="GitHub user name.")

args = parser.parse_args()

if args.user is None:
    print("ERROR: Specify GitHub user name.")
    sys.exit(1)

html = get_github_html(args.user)

soup = BeautifulSoup(html, "html.parser")
svg = soup.find("svg", attrs={"class", "js-calendar-graph-svg"})
svg = format_svg(svg)

os.makedirs("work", exist_ok=True)
with open("work/grass.svg", "w") as f:
    f.write(str(svg))

drawing = svg2rlg("work/grass.svg")
renderPM.drawToFile(drawing, "work/grass.png", fmt="PNG")
