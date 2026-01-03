import asyncio
import os
from asyncio import StreamWriter
from typing import AsyncIterator

CHUNK_SIZE = 100

async def readlines(reader: asyncio.StreamReader) -> AsyncIterator[bytes]:
    while line := await read_until_eol(reader):
        yield line


async def read_until_eol(reader: asyncio.StreamReader) -> bytes | None:
    """Returns a line of text or empty bytes object if EOF is received.
    """
    data = b''
    sep = os.linesep.encode()
    while data := data + await reader.read(CHUNK_SIZE):
        if sep in data:
            message, _, data = data.partition(sep)
            return message + sep

def send_initial_data_burst(writer: StreamWriter, powered_on: bool = False) -> None:
    if powered_on:
        writer.write(("ssp.power.on" + "\n").encode())
        writer.write(("ssp.procstate.[2]" + "\n").encode())
    else:
        writer.write(("ssp.power.off" + "\n").encode())
        writer.write(("ssp.procstate.[0]" + "\n").encode())

    writer.write(('ssp.brand.["StormAudio"]' + "\n").encode())
    writer.write(('ssp.model.["ISP Core 16"]' + "\n").encode())
    writer.write(("ssp.speaker.[3]" + "\n").encode())
    writer.write(("ssp.frontpanel.actbright.[100]" + "\n").encode())
    writer.write(("ssp.frontpanel.stbybright.[20]" + "\n").encode())
    writer.write(("ssp.frontpanel.stbytime.[5]" + "\n").encode())
    writer.write(("ssp.frontpanel.color.[white]" + "\n").encode())
    writer.write(("ssp.generator.off" + "\n").encode())
    writer.write(("ssp.version.[4.7r2-rc4]" + "\n").encode())
    writer.write(("ssp.msgstatus.[0]" + "\n").encode())
    writer.write(('ssp.msgstatusTxt.[0, ""]' + "\n").encode())
    writer.write(("ssp.mute.off" + "\n").encode())
    writer.write(("ssp.vol.[-55.0]" + "\n").encode())
    writer.write(("ssp.dim.off" + "\n").encode())
    writer.write(("ssp.input.[1]" + "\n").encode())
    writer.write(("ssp.inputZone2.[0]" + "\n").encode())
    writer.write(("ssp.input.start" + "\n").encode())
    writer.write(
        ('ssp.input.list.["BD-Player", 1, 1, 1, 0, 0, 0.0, 0]' + "\n").encode()
    )
    writer.write(('ssp.input.list.["Apple TV", 2, 2, 2, 0, 0, 0.0, 0]' + "\n").encode())
    writer.write(('ssp.input.list.["TV", 8, 0, 23, 0, 0, 0.0, 0]' + "\n").encode())
    writer.write(('ssp.input.list.["Musik", 9, 0, 13, 0, 0, 0.0, 0]' + "\n").encode())
    writer.write(('ssp.input.list.["Roon", 10, 0, 17, 0, 0, 0.0, 0]' + "\n").encode())
    writer.write(("ssp.input.end" + "\n").encode())
    writer.write(("ssp.preset.[247]" + "\n").encode())
    writer.write(("ssp.preset.custom.off" + "\n").encode())
    writer.write(("ssp.preset.start" + "\n").encode())
    writer.write(
        ('ssp.preset.list.["Default", 175, "["1"]", 0, 0, 0, 0, 0]' + "\n").encode()
    )
    writer.write(
        ('ssp.preset.list.["ARTopt", 246, "["1"]", 0, 0, 0, 0, 0]' + "\n").encode()
    )
    writer.write(
        ('ssp.preset.list.["ARTopt-LW", 247, "["1"]", 0, 0, 0, 0, 0]' + "\n").encode()
    )
    writer.write(("ssp.preset.end" + "\n").encode())
    writer.write(("ssp.surroundmode.[0]" + "\n").encode())
    writer.write(("ssp.loudness.[1]" + "\n").encode())
    writer.write(("ssp.lfedim.off" + "\n").encode())
    writer.write(("ssp.cspread.on" + "\n").encode())
    writer.write(("ssp.dialogcontrol.[0, 0]" + "\n").encode())
    writer.write(("ssp.dialognorm.off" + "\n").encode())
    writer.write(("ssp.IMAXMode.auto" + "\n").encode())
    writer.write(("ssp.auropreset.[0]" + "\n").encode())
    writer.write(("ssp.aurostrength.[12]" + "\n").encode())
    writer.write(("ssp.drc.off" + "\n").encode())
    writer.write(("ssp.dolbymode.[0]" + "\n").encode())
    writer.write(("ssp.dolbyvirtualizer.off" + "\n").encode())
    writer.write(("ssp.bass.[1]" + "\n").encode())
    writer.write(("ssp.treble.[1]" + "\n").encode())
    writer.write(("ssp.treb.[1]" + "\n").encode())
    writer.write(("ssp.lipsync.[0.0]" + "\n").encode())
    writer.write(("ssp.c_en.[0]" + "\n").encode())
    writer.write(("ssp.s_en.[0]" + "\n").encode())
    writer.write(("ssp.sub_en.[0]" + "\n").encode())
    writer.write(("ssp.lfe_en.[0]" + "\n").encode())
    writer.write(("ssp.brightness.[1]" + "\n").encode())
    writer.write(("ssp.trig1.off" + "\n").encode())
    writer.write(("ssp.trig1.manual.off" + "\n").encode())
    writer.write(("ssp.trig2.off" + "\n").encode())
    writer.write(("ssp.trig2.manual.off" + "\n").encode())
    writer.write(("ssp.trig3.off" + "\n").encode())
    writer.write(("ssp.trig3.manual.off" + "\n").encode())
    writer.write(("ssp.trig4.off" + "\n").encode())
    writer.write(("ssp.trig4.manual.off" + "\n").encode())
    writer.write(("ssp.trigger.start" + "\n").encode())
    writer.write(('ssp.trigger.list.["NAD M27"]' + "\n").encode())
    writer.write(('ssp.trigger.list.["Trigger 2"]' + "\n").encode())
    writer.write(('ssp.trigger.list.["Trigger 3"]' + "\n").encode())
    writer.write(('ssp.trigger.list.["Trigger 4"]' + "\n").encode())
    writer.write(("ssp.trigger.end" + "\n").encode())
    writer.write(("ssp.fs.[]" + "\n").encode())
    writer.write(("ssp.stream.[None]" + "\n").encode())
    writer.write(("ssp.format.[]" + "\n").encode())
    writer.write(("ssp.allowedmode.[0]" + "\n").encode())
    writer.write(('ssp.hdmi1.input.["HDMI 1"]' + "\n").encode())
    writer.write(('ssp.hdmi1.sync.["Detected"]' + "\n").encode())
    writer.write(('ssp.hdmi1.timing.["3840x2160@59Hz"]' + "\n").encode())
    writer.write(('ssp.hdmi1.cp.["HDCP 2.2"]' + "\n").encode())
    writer.write(('ssp.hdmi1.colorspace.["ITU-R BT.709"]' + "\n").encode())
    writer.write(('ssp.hdmi1.colordepth.["8 bit"]' + "\n").encode())
    writer.write(('ssp.hdmi1.mode.["YUV444"]' + "\n").encode())
    writer.write(('ssp.hdmi1.hdr.["SDR"]' + "\n").encode())
    writer.write(('ssp.hdmi2.input.["HDMI 1"]' + "\n").encode())
    writer.write(('ssp.hdmi2.sync.["Detected"]' + "\n").encode())
    writer.write(('ssp.hdmi2.timing.["3840x2160@59Hz"]' + "\n").encode())
    writer.write(('ssp.hdmi2.cp.["HDCP 2.2"]' + "\n").encode())
    writer.write(('ssp.hdmi2.colorspace.["ITU-R BT.709"]' + "\n").encode())
    writer.write(('ssp.hdmi2.colordepth.["8 bit"]' + "\n").encode())
    writer.write(('ssp.hdmi2.mode.["YUV444"]' + "\n").encode())
    writer.write(('ssp.hdmi2.hdr.["SDR"]' + "\n").encode())
    writer.write(("ssp.zones.start" + "\n").encode())
    writer.write(
        (
                'ssp.zones.list.[1, "Digital Zone2", 2000, 1, 0, -75, 0.0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]'
                + "\n"
        ).encode()
    )
    writer.write(("ssp.zones.end" + "\n").encode())
    writer.write(("ssp.zones.profiles.start" + "\n").encode())
    writer.write(
        ('ssp.zones.profiles.list.[1, 1, "Downmix", 1, 0, 0, 0, 0]' + "\n").encode()
    )
    writer.write(
        ('ssp.zones.profiles.list.[3, 241, "Default", 0, 0, 0, 0, 0]' + "\n").encode()
    )
    writer.write(
        ('ssp.zones.profiles.list.[3, 311, "ARTopt", 0, 0, 0, 0, 0]' + "\n").encode()
    )
    writer.write(
        ('ssp.zones.profiles.list.[3, 312, "ARTopt-LW", 1, 0, 0, 0, 0]' + "\n").encode()
    )
    writer.write(("ssp.zones.profiles.end" + "\n").encode())

async def handle_connection(reader, writer):
    addr = writer.get_extra_info("peername")

    print(f"Connected to: {addr!r}")

    send_initial_data_burst(writer)
    await writer.drain()

    async for data in readlines(reader):
        message = data.decode().strip()
        print(f"Message from client: {message!r}")

        match message:
            case "ssp.power.on":
                send_initial_data_burst(writer, True)
                await writer.drain()

            case "ssp.power.off":
                writer.write(("ssp.power.off" + "\n").encode())
                writer.write(("ssp.procstate.[0]" + "\n").encode())
                await writer.drain()

            case "ssp.procstate":
                writer.write(("ssp.procstate.[2]" + "\n").encode())
                await writer.drain()

    print(f'{addr}: Connection closed by the remote peer.')


async def main():
    server = await asyncio.start_server(handle_connection, "0.0.0.0", 23)

    addrs = ", ".join(str(sock.getsockname()) for sock in server.sockets)
    print(f"Serving on {addrs}")

    async with server:
        await server.serve_forever()


asyncio.run(main())
