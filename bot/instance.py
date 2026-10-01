import asyncio
from disnake.ext import commands
import logging
from datetime import datetime

from bot.config import MUSIC_INSTANCES

logger = logging.getLogger(__name__)

class Instance:
    def __init__(self, instance_id, discord_id, token):
        self.instance_id = instance_id
        self.discord_id = discord_id
        self.token = token
        self.status = "stopped"
        self.started_at = None
        self.bot = None


    async def start(self):
        try:
            self.bot = commands.InteractionBot()

            @self.bot.event
            async def on_ready():
                self.status = "running"
                self.started_at = datetime.now()
                logger.info(f"{self.instance_id} запущен")

            await self.bot.start(self.token)
        except Exception:
            self.status = "stopped"
            logger.error(f"{self.instance_id} не удалось запустить")

    async def stop(self):
        self.status = "stopping"

        if self.bot:
            await self.bot.close()

        self.bot = None
        self.status = "stopped"
        self.started_at = None

class InstanceManager:

    def __init__(self):
        self.instances = {}

        for instance_id, data in MUSIC_INSTANCES.items():
            instance = Instance(
                instance_id,
                data["discord_id"],
                data["token"]
            )
            self.instances[instance_id] = instance


    def get_instance(self, instance_id):
        return self.instances.get(instance_id)


    def start_instance(self, instance_id):
        instance = self.get_instance(instance_id)

        if instance is None:
            return False

        if instance.status != "stopped":
            return False

        instance.status = "starting"
        asyncio.create_task(instance.start())
        return True

    def start_all(self):
        for instance_id in MUSIC_INSTANCES:
            self.start_instance(instance_id)


    def stop_instance(self, instance_id):
        instance = self.get_instance(instance_id)

        if instance is None:
            return False

        if instance.status != "running":
            return False

        asyncio.create_task(instance.stop())
        return True

    def stop_all(self):
        for instance_id in MUSIC_INSTANCES:
            self.stop_instance(instance_id)


    def restart_instance(self, instance_id):
        instance = self.get_instance(instance_id)

        if instance is None:
            return False

        asyncio.create_task(self._restart(instance))
        return True

    def restart_all(self):
        for instace_id in self.instances:
            self.restart_instance(instace_id)

    async def _restart(self, instance):
        await instance.stop()

        instance.status = 'starting'
        await instance.start()