from channels.generic.websocket import AsyncWebsocketConsumer


class NotifConsumers(AsyncWebsocketConsumer):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.group_name = ''

    async def connect(self):
        print('connect')
        self.group_name = 'infochannel'

        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard('infochannel', self.channel_name)

    async def infochannel_message(self, event):
        print(event['notif'])        
        await self.send(text_data=event['notif'])