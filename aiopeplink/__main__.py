import asyncio
import aiohttp

from interfaces.connectivity import Connectivity
from peplink import PeplinkAPI

# For testing
import creds


async def main():
    async with aiohttp.ClientSession() as session:
        connectivity = Connectivity(session, creds.host, creds.username, creds.password)
        api = PeplinkAPI(connectivity)

        location = await api.async_get_location()

        # Print location
        print(location.longitude)
        print(location.latitude)


asyncio.run(main())
