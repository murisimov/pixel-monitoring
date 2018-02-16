from gtts import gTTS as gtts


def transform(text, f='record.mp3', slow=False):
    assert isinstance(text, str)
    
    record = gtts(text=text, lang='en', slow=slow)
    record.save(f)
    return f
