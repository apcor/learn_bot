from clarifai_grpc.channel.clarifai_channel import ClarifaiChannel
from clarifai_grpc.grpc.api import resources_pb2, service_pb2, service_pb2_grpc
from clarifai_grpc.grpc.api.status import status_pb2, status_code_pb2
from pip import main
import settings
from emoji import emojize
from telegram import ReplyKeyboardMarkup, KeyboardButton
from random import choice, randint


def get_smile(user_data):
    if 'emoji' not in user_data:
        smile = choice(settings.USER_EMOJI)
        return emojize(smile, language='alias')
    return user_data['emoji']

def main_keyboard():
    return ReplyKeyboardMarkup([['Send me a dog', KeyboardButton('See my location', request_location=True)]])

def play_random_numbers(user_number):
    bot_number = randint(user_number - 10, user_number + 10)
    if user_number > bot_number:
        message = f"Your number {user_number}, my number {bot_number}. \nYou won!"
    elif user_number == bot_number:
        message = f"Your number {user_number}, my number is also {bot_number}.\nIt's a draw!"
    else:
        message = f"Your number {user_number}, my number {bot_number}.\nYou lost! :-("
    return message

def has_object_on_image(file_name, object_name):
    channel = ClarifaiChannel.get_grpc_channel()
    app = service_pb2_grpc.V2Stub(channel)
    metadata = (('authorization', f'Key {settings.CLARIFAI_API_KEY}'),)

    with open(file_name, 'rb') as f:
        file_data = f.read()
        image = resources_pb2.Image(base64=file_data)
    request = service_pb2.PostModelOutputsRequest(
        model_id='aaa03c23b3724a16a56b629203edc62c',
        inputs=[
            resources_pb2.Input(data=resources_pb2.Data(image=image))
        ])

    response = app.PostModelOutputs(request, metadata=metadata)
    # print(response)
    return check_response_for_object(response, object_name)

def check_response_for_object(response, object_name):
    if response.status.code == status_code_pb2.SUCCESS:
        for concept in response.outputs[0].data.concepts:
            if (concept.name == object_name) & (concept.value >= 0.9):
                return True 
    else:
        print(f'Image recognition error:{response.outputs[0].status.details}')
    return False


if __name__ == '__main__':
    print(has_object_on_image('images/dog_1.jpeg', 'dog'))
    print(has_object_on_image('images/dog_2.jpeg', 'dog'))
    print(has_object_on_image('images/not_dog.jpeg', 'dog'))
