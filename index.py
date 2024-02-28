import asyncio
import re
import websockets
import orjson
from python_socks.async_.asyncio import Proxy
from regex_patterns import market_patterns
from aiohttp import web
from pympler import asizeof

events_data = {}

config = {
    "cmd": "subscribe", 
    "auth_key":"your_key", 
    "needed_bk":["bookmaker:prematch"], 
    "needed_sport":["soccer"]
}
message = orjson.dumps(config)

async def sock():
    proxy_url = 'socks5://wucwmqgi:hokz0ynuxa32@45.155.68.129:8133'
    proxy = Proxy.from_url(proxy_url)

    dest_host = 'api.oddscp.com'
    dest_port = 8001

    conn = await proxy.connect(dest_host, dest_port)

    async with websockets.connect(
        "ws://api.oddscp.com:8001",
        ping_interval=None,
        sock=conn, 
    ) as websocket:
        await websocket.send(message)
        async for msg in websocket:
            data = orjson.loads(msg)
            process_message(data)
            size_in_mb = asizeof.asizeof(events_data) / (1024 ** 2)
            print('New message. Total size: ', size_in_mb, " Mb")

def parse_market_name(market_name):
    for pattern_name, patterns in market_patterns.items():
        if not isinstance(patterns, list):
            patterns = [patterns]
        for pattern in patterns:
            pattern = pattern.strip("!")
            
            match = re.match(pattern, market_name)
            if match:
                return {**match.groupdict(), "type": pattern_name}
    return {"type": "unknown", "market_name": market_name}

def process_message(data):
    if len(data) < 4:
        return 
    
    bk_name, msg_type, event_id = data[:3]
    
    if msg_type == "update_event":
        event_info = data[3]
        if event_id not in events_data:
            events_data[event_id] = {"info": event_info, "markets": []}
        else:
            events_data[event_id]["info"].update(event_info)
    elif msg_type == "update_markets":        
        markets_info = data[3]
        for market in markets_info:
            market_name = market[0]
            parsed_market = parse_market_name(market_name)
            market.append(parsed_market)
        if event_id not in events_data:
            events_data[event_id] = {"info": {}, "markets": markets_info}
        else:
            events_data[event_id]["markets"].extend(markets_info)
    
    #print(f"Updated data for event {event_id}: {events_data[event_id]}")

async def print_events_data_every_minute():
    while True:
        await asyncio.sleep(60)  
        print(events_data)  

async def sendData(request):
    return web.Response(text=orjson.dumps(events_data, option=orjson.OPT_INDENT_2).decode('utf-8'), content_type='application/json')

async def start_web_server():
    app = web.Application()
    app.router.add_get('/odds_data', sendData)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, 'localhost', 8080)
    await site.start()

async def main():    
    websocket_task = asyncio.create_task(sock())
    web_server_task = asyncio.create_task(start_web_server())
    await asyncio.gather(websocket_task, web_server_task)

if __name__ == '__main__':
    asyncio.run(main())