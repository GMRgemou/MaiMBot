from nonebot import on_command, get_driver
from nonebot.adapters.onebot.v11 import Bot, MessageEvent
from nonebot.permission import SUPERUSER
from nonebot.rule import to_me
from nonebot.log import logger
import asyncio

# 可以改为你希望的密钥
shutdown = on_command("miyao", rule=to_me(), permission=SUPERUSER, priority=5)

@shutdown.handle()
async def handle_shutdown(bot: Bot, event: MessageEvent):
    logger.info("接收到关闭命令")
    # 发送确认消息
    await bot.send(event, "睡觉了喵")
    # 获取事件循环并停止
    loop = asyncio.get_running_loop()
    loop.stop()
    logger.info("机器人已关闭")