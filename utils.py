import random 
import time
import math
import os
import aiohttp
import asyncio
import aiofiles
from pyrogram.errors import FloodWait
from datetime import datetime, timedelta


class Timer:
    def __init__(self, time_between=5):
        self.start_time = time.time()
        self.time_between = time_between

    def can_send(self):
        if time.time() > (self.start_time + self.time_between):
            self.start_time = time.time()
            return True
        return False


# lets do calculations
def hrb(value, digits=2, delim="", postfix=""):
    """Return a human-readable file size."""
    if value is None:
        return None
    chosen_unit = "B"
    for unit in ("KB", "MB", "GB", "TB"):
        if value > 1000:
            value /= 1024
            chosen_unit = unit
        else:
            break
    return f"{value:.{digits}f}" + delim + chosen_unit + postfix


def hrt(seconds, precision=0):
    """Return a human-readable time delta as a string."""
    pieces = []
    value = timedelta(seconds=seconds)

    if value.days:
        pieces.append(f"{value.days}day")

    seconds = value.seconds

    if seconds >= 3600:
        hours = int(seconds / 3600)
        pieces.append(f"{hours}hr")
        seconds -= hours * 3600

    if seconds >= 60:
        minutes = int(seconds / 60)
        pieces.append(f"{minutes}min")
        seconds -= minutes * 60

    if seconds > 0 or not pieces:
        pieces.append(f"{seconds}sec")

    if not precision:
        return "".join(pieces)

    return "".join(pieces[:precision])


timer = Timer()


async def progress_bar(current, total, reply, start):
    if timer.can_send():
        now = time.time()
        diff = now - start
        if diff < 1:
            return
        else:
            perc = f"{current * 100 / total:.1f}%"
            elapsed_time = round(diff)
            speed = current * 3 / elapsed_time
            remaining_bytes = total - current
            if speed > 0:
                eta_seconds = remaining_bytes / speed
                eta = hrt(eta_seconds, precision=1)
            else:
                eta = "-"
            sp = str(hrb(speed)) + "/s"
            tot = hrb(total)
            cur = hrb(current)
            bar_length = 10
            completed_length = int(current * bar_length / total)
            remaining_length = bar_length - completed_length

            symbol_pairs = [
                ("◾️", "◽️"),
                ("⚫️", "⚪️"),
                ("🔴", "🔵")
            ]
            chosen_pair = random.choice(symbol_pairs)
            completed_symbol, remaining_symbol = chosen_pair

            progress_bar = completed_symbol * completed_length + remaining_symbol * remaining_length

            try:
                await reply.edit(
                    f'`🦋⃪꯭ ─‌⃛┼ 𝞄⃕𝖋𝖋 समय यात्री Sᴛʀᴀɴɢᴇʀ ʙᴏʏs THE BOYS🥵⃝⃝ᬽ꯭ ⃪꯭ \n'
                    f'🙆‍♂️ {progress_bar}\n'
                    f'├👩‍🎓 Progress ➤ | {perc} |\n'
                    f'├👀 Speed ➤ | {sp} |\n'
                    f'├💗 Processed ➤ | {cur} |\n'
                    f'├💬 Size ➤ | {tot} |\n'
                    f'├💢 ETA ➤ | {eta} |\n'
                    f'🦋 Sᴛʀᴀɴɢᴇʀ ʙᴏʏs THE BOYS🥵⃝⃝ᬽ꯭ ⃪꯭ on`'
                )
            except FloodWait as e:
                time.sleep(e.x)


# ==============================
# NEW PARALLEL DOWNLOADER
# ==============================
async def download_file(url, output_path, chunk_size=5_000_000, max_connections=10):
    """
    Parallel downloader using aiohttp
    url: source link
    output_path: where to save file
    chunk_size: per connection chunk (default 5MB)
    max_connections: how many parts to download at once
    """
    async with aiohttp.ClientSession() as session:
        # Get file size
        async with session.head(url) as resp:
            file_size = int(resp.headers.get("Content-Length", 0))

        # Split into ranges
        ranges = [(i, min(i + chunk_size - 1, file_size - 1)) for i in range(0, file_size, chunk_size)]

        async def fetch_range(start, end, part_no):
            headers = {"Range": f"bytes={start}-{end}"}
            async with session.get(url, headers=headers) as resp:
                part_file = f"{output_path}.part{part_no}"
                async with aiofiles.open(part_file, "wb") as f:
                    async for chunk in resp.content.iter_chunked(1024 * 512):
                        await f.write(chunk)
                return part_file

        # Download in parallel
        tasks = [fetch_range(start, end, idx) for idx, (start, end) in enumerate(ranges)]
        part_files = await asyncio.gather(*tasks)

        # Merge parts
        async with aiofiles.open(output_path, "wb") as out:
            for part_file in part_files:
                async with aiofiles.open(part_file, "rb") as pf:
                    chunk = await pf.read()
                    await out.write(chunk)
                os.remove(part_file)

    return output_path
        
