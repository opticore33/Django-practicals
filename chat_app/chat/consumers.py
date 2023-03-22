import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync

class chatConsumer(WebsocketConsumer):
    #to handle initial request come from client
    def connect(self):
        self.room_group_name = 'test'

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()

        # self.send(text_data=json.dumps({    #convert a subset or dictionary into a json string
        #     'type':'connection_established',
        #     'message':'You are now connected!',
        # })) 

    # to handle recieved massages from client    
    def receive(self,text_data):
        text_data_json = json.loads(text_data) #json.loads convert json string into python dictionary
        message = text_data_json['message']
        # print('Message: ', message)

        async_to_sync(self.channel_layer.group_send)(
             self.room_group_name,
             {
                'type':'chat_message',
                'message':message
             }
        )

        # self.send(text_data=json.dumps({
        #     'type':'chat',
        #     'message':message
        # }))

    def chat_message(self, event):
        message = event['message']

        self.send(text_data=json.dumps({
            'type':'chat',
            'message':message
        }))
    # to handle event when client disconnect from this consumer
    # def disconnect(self):
    #     pass