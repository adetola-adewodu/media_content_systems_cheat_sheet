from diagrams import Diagram

from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.ml import Rekognition
from diagrams.aws.ml import Transcribe
from diagrams.aws.storage import SimpleStorageServiceS3BucketWithObjects
from diagrams.aws.media import ElementalMediaconvert
from diagrams.onprem.queue import Rabbitmq
from diagrams.programming.language import Nodejs
from diagrams.gcp.ml import SpeechToText
from diagrams.gcp.ml import VideoIntelligenceAPI

graph_attr = {
    "fontsize": "45",
    "title": ""
}


with Diagram("Location based Media System Design", show=False, direction="LR",graph_attr=graph_attr):
    international_service = Nodejs("Int'l Web Service")
    us_service = Nodejs("US Web Service")
    international_metadata = RDS("Int'l Metadata")
    us_metadata = RDS("US Metadata")
    international_queue = Rabbitmq("Int'l Queue")
    us_queue = Rabbitmq("US Queue")
    media_broker = Nodejs("Broker")
    nonlinear_workflow = EC2("NonLinear/Streaming")
    linear_workflow = EC2("Linear/Broadcast")

    international_service >> international_metadata
    international_service >> international_queue >> media_broker
    us_service >> us_metadata
    us_service >> us_queue >> media_broker
    media_broker >> [nonlinear_workflow, linear_workflow]

with Diagram("Convert Media System Design", show=False, direction="LR",graph_attr=graph_attr):

    input = SimpleStorageServiceS3BucketWithObjects("input file")
    output = SimpleStorageServiceS3BucketWithObjects("output file")
    media_convert = ElementalMediaconvert("Media Convert")
    vantage_convert = EC2("Vantage")
    amberfin_dark = EC2("Amberfin Dark")
    # aws_object_detection = Rekognition("AWS Video Object Detection")
    # aws_caption = Transcribe("AWS Speech to Text")
    # gcp_object_detection = VideoIntelligenceAPI("GCP Video Intelligence")
    # gcp_caption = SpeechToText("GCP Speech To Text ")

    
    

    input >> [media_convert,vantage_convert, amberfin_dark] >> output
