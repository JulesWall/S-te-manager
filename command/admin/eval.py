import discord
from config import OWNER, FOOTER
from db.function.Querry import *
from classes.checkers import *
from Syno.Syno import *
 
import io
import contextlib
import textwrap
import traceback
import os

class Eval:
    def __init__(self, message : discord.Message, bot : discord.Client()):
        self.bot = bot
        self.message = message
        
    async def run(self):
        if self.message.author.id not in OWNER : return None
        code = " ".join(self.message.content.split(" ")[1:])
        code, shell, one_line = self.clean_code(code)
        buffer = io.StringIO()
        result = f"Input :\n```py\n{code}\n```"
        ret = ""
        local = {
            'self':self,
            'Querry':Querry
        }
        try:
            with contextlib.redirect_stdout(buffer):
                if one_line:
                    output = eval(code, local)
                    if output is None:
                        output = ""
                    output = self.clean_output(str(output) + "\n" + buffer.getvalue())
                    result += f"\nOutput :\n```\n{output}\n```" + ret
                else:
                    exec(f"async def main() :\n {textwrap.indent(code, '    ')}", local)
                    ret = await local["main"]()
                    if ret is not None:
                        ret = f"\nreturn :\n```\n{ret}```"
                    else:
                        ret = ""
                    if buffer.getvalue() == "":
                        output = "/"
                    else:
                        output = self.clean_output(buffer.getvalue())
                    result += f"\nOutput :\n```\n{output}\n```" + ret
        except:
            result += f"""\nerror :\n```\n{traceback.format_exc()}```\n"""
        finally:
            embed = discord.Embed(title = "EVAL", description = result, color = 0xCC0000)
            embed.set_footer(text=FOOTER)
            await self.message.channel.send(embed=embed)

    
    def clean_code(self, code):
        shell = False
        one_line = False
        if "--print " in code:
            shell = True
            code = code.replace("--print ", "")
        elif "-p " in code:
            shell = True
            code = code.replace("-p ", "")
        code = code.split("\n")
        if code[0].startswith("```"):
            code = code[1:]
        if code[-1].startswith("```"):
            code = code[:-1]
        if len(code) == 1:
            if "=" not in code[0]:
                one_line = True
        code = "\n".join(code)
        return code, shell, one_line

    def clean_output(self, output):
        lvl_indent = 0
        var = ""
        space = False
        for a in output:
            if a in ("[", "{", "("):
                lvl_indent += 1
                var += a + "\n" + "    " * lvl_indent
            elif a in ("]", "}", ")"):
                lvl_indent -= 1
                var += "\n" + "    " * lvl_indent + a
            elif a == ",": var += ",\n" + "    " * lvl_indent
            elif a in ("'", '"'):
                if space: space = False
                else: space = True
                var += a
            elif a == " ":
                if space: var += a
            else: var += a
        return var        
