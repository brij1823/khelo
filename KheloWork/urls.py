from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', Home.as_view()),
    path('temp', Temp.as_view()),
    path('submitQuery', submitQuery),
    path('sendBattingData', sendBattingDataWebcam),
    path('uploadBattingVideo', upload_batting_video),
    path('getImageData', getImageData),
    path('image', Image.as_view()),
    path('uploadCustom', uploadCustom.as_view()),

    path('uploadGymVideoCustom', uploadGymVideoCustom),
    path('sendImageDataLooperGym', sendLooperDataGym),
    path('sendGymDataVideo', sendGymDataVideo),
    path('return_frames', return_frames),


    path('uploadCricketVideoCustom', uploadCricketVideoCustom),
    path('sendImageDataLooperCricket', sendLooperDataCricket),
    path('return_frames_cricket', return_frames_cricket),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
