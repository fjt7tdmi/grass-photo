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

import optparse
import os
import sys
import urllib.request

from bs4 import BeautifulSoup
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM

def get_github_html(user):
    url = "https://github.com/" + options.user
    with urllib.request.urlopen(url) as response:
        html = response.read()
        return html

optionParser = optparse.OptionParser()
optionParser.add_option("-u", dest="user", default=None, help="GitHub user name.")

(options, args) = optionParser.parse_args()

if options.user is None:
    print("ERROR: Specify GitHub user name.")
    sys.exit(1)

html = get_github_html(options.user)

soup = BeautifulSoup(html, "html.parser")
svg = str(soup.find("svg", attrs={"class", "js-calendar-graph-svg"}))
svg = svg.replace('<svg', '<svg xmlns="http://www.w3.org/2000/svg"')

os.makedirs("work", exist_ok=True)
with open("work/grass.svg", "w") as f:
    f.write(svg)

drawing = svg2rlg("work/grass.svg")
renderPM.drawToFile(drawing, "work/grass.png", fmt="PNG")
