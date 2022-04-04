from nonebot import on_command
from nonebot.rule import to_me
from nonebot.matcher import Matcher
from nonebot.adapters import Message, MessageSegment, MessageTemplate
from nonebot.adapters.onebot.v11.message import Message as OneBotMessage
from nonebot.params import Arg, CommandArg, ArgPlainText

test = on_command("test", aliases={"测试"}, priority=5)


@test.handle()
async def _(matcher: Matcher, args: Message = CommandArg()):
    
    await test.finish(OneBotMessage('123'))

