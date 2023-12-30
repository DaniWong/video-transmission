
from __future__ import annotations
from abc import ABC, abstractmethod

from video_transmission.models import Video, ProcessedStatus


# ===================================================
# FACTORY METHOD TO GET AI ENGINE
# ===================================================

class AiEngineCreator(ABC):
    """
    The Creator class declares the factory method that is supposed to return an
    object of a AiEngine class. The Creator's subclasses usually provide the
    implementation of this method.
    """

    @abstractmethod
    def factory_method(self):
        """
        Here get the concret ai engine to be use
        """
        pass

    def process_video(self, video) -> str:
        """
        Also note that, despite its name, the Creator's primary responsibility
        is not creating ai engines. Usually, it contains some core business logic
        that relies on Ai engine objects, returned by the factory method.
        Subclasses can indirectly change that business logic by overriding the
        factory method and returning a different type of ai engine from it.
        """

        # Call the factory method to create a Ai engine object.
        ai_engine = self.factory_method()

        # Now, use the ai engine object to process videos.
        result = ai_engine.process(video)

        return result


"""
Concrete Creators override the factory method in order to change the resulting
ai engine's type.
"""


class AiComputerVisionCreator(AiEngineCreator):
    """
    Note that the signature of the method still uses the abstract ai engine type,
    even though the concrete ai engine is actually returned from the method. This
    way the Creator can stay independent of concrete ai engine classes.
    """

    def factory_method(self) -> AiEngine:
        return AiComputerVisionEngine()


class AiEngine(ABC):
    """
    The Ai engine interface declares the operations that all concrete ai engines
    must implement.
    """

    @abstractmethod
    def process(self, video) -> str:
        pass


class AiComputerVisionEngine(AiEngine):

    def process(self, video) -> str:
        return f"Processed data from a video {video.title} from Ai computer vision engine"


# This constanst is an example in how can we choose an ai engine.
# Another idea to choose ai engine is to have a config file to get ai engine
DEFAULT_CREATOR_CLASS = AiComputerVisionCreator


def process_videos(video_list):
    engine = DEFAULT_CREATOR_CLASS()  # Here we use the concret creator choosed
    for video in video_list:
        result = engine.process_video(video)
        print(video, result)
        video.video_processed_data = result
        video.video_process_status = ProcessedStatus.PROCESSED
        video.save()


# ===================================================================
# COMMANDS TO BE USE AS PERIODIC TASKS
# Since the complexity of the algorithm is unknown, here we can use an asynchronous queuing 
# and task handling system or even call an external api.
# ===================================================================

def process_pending_videos():
    print('Processing videos')
    videos = Video.objects.filter(video_process_status=ProcessedStatus.TO_PROCESS)
    process_videos(videos)

def process_failed_videos():
    print('Processing failed videos')
    videos = Video.objects.filter(video_process_status=ProcessedStatus.PROCESSED_FAILED)
    process_videos(videos)
