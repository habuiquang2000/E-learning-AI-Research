from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .gTTS_module import text2Audio
# from .cache import remove_cache


def gTTs(r, language="en", text="say it"):
    """ 
    To return json dynamic TTS .mp3 link response :
    {mp3 : "mp3 static link ..."}
    @param: language language to speak in (default: "en")
    @param: text text to speak out (default: "say it")
    """

    audio_path = text2Audio(
        language=language,
        text=text
    ).replace("%5C", "/")
    
    
    return JsonResponse(
        {
            "mp3": audio_path
        }
    )


@login_required
def gTTs_auth(r, language="en", text="say it"):
    """ 
    To return json dynamic TTS .mp3 link response only for
    authenticated users: {mp3 : "mp3 static link ..."}
    @param: language language to speak in (default: "en")
    @param: text text to speak out (default: "say it")
    """
    return gTTs(r, language, text)
