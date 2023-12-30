# Video transmission project REPORT

## Backend

### Endpoints and auth

The requested endpoints were developed using an authentication mechanism based on JWT web token. To obtain the token an endpoint is used in the following way

![image](https://github.com/DaniWong/video-transmission/assets/5056497/9aa244c1-2008-41f4-9ec4-97f9f1924bfe)

once the token is used, we can use it as endpoint headers.

![image](https://github.com/DaniWong/video-transmission/assets/5056497/002c9fca-913e-45e6-85b2-ec6aed4ddf75)


### AI Server

The integration with the ai server uses django admin commands to process the videos. The main idea is to build a periodic asynchronous service to be processing the videos in the background. It is not specified what is the complexity of the processing and that is why I thought of it this way. The command to process the videos are python manage.py process_videos and python manage.py process_failed_videos.

It was also decided to use the factory method design pattern for future implementations of other types of ia servers.

### VMS

Regarding the VMS, I use the same approach as the ai server.
