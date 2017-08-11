# -*- mode: python; coding: utf-8 -*-
#
# Copyright © 2012 Roland Sieker, ospalh@gmail.com
# Inspiration and source of the URL: Tymon Warecki
# Adapted by Thomas TEMPE, thomas.tempe@alysse.org
#
# License: GNU AGPL, version 3 or later; http://www.gnu.org/copyleft/agpl.html


'''
Download Chinese pronunciations from GoogleTTS
'''

import os
import re
from gtts.tts import gTTS

from aqt import mw


download_file_extension = u'.mp3'
url_gtts = 'http://translate.google.com/translate_tts?client=t&'
user_agent_string = 'Mozilla/5.0'


def get_word_from_google(source, lang='zh'):
    filename, fullpath = get_filename("_".join([source, "G", lang]), download_file_extension)
    if os.path.exists(fullpath):
        return filename
    tts = gTTS(source, lang=lang)
    tts.save(fullpath)
    return filename

def get_filename(base, end):
    """Return the media filename for the given title. """
    # Basically stripping the 'invalidFilenameChars'. (Not tested too much).
    base = re.sub('[\\/:\*?"<>\|]', '', base)
    mdir = mw.col.media.dir()
    return base + end, os.path.join(mdir, base + end)
