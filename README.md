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

### Django admin and utilities

The Video model is fully functional from the django admin. Also, audit fields were implemented in this same model.

### About Git

For this repository, please see the pull request history where I write more specific information about my work.

### About Security

To deploy the project in production environments, here are some best practices that were not implemented in the code due to lack of time:

- Set the DEBUG = False configuration.
- All important variables should be obtained from environment variables or some cloud service secrets storage.
- The CORS_ALLOW_ALL_ORIGINS setting should be set to false and only indicate the domains that are allowed to consume resources. In this case it is necessary to put the url of the front end.

## FrontEnd (Repo -> https://github.com/DaniWong/video-transmission-frontend)

Regarding the frontend, implement 3 screens only:

- Login
- Video list
- Detail of videos

Due to lack of time I didn't implement the video upload screen.

Here are some screenshots of the frontend

![image](https://github.com/DaniWong/video-transmission/assets/5056497/f8ae1e65-927c-41a0-8696-f2cb34ef3180)

![image](https://github.com/DaniWong/video-transmission/assets/5056497/58a3e5dd-8b7b-4e2a-b645-4c21f25c2b96)

![image](https://github.com/DaniWong/video-transmission/assets/5056497/8d4694e7-11f3-4df1-89de-34c918fe9f24)
