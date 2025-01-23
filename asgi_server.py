import os
import sys

import uvicorn

if __name__ == '__main__':
    root_path = os.path.dirname(os.path.dirname(__file__))
    sys.path.append(os.path.normpath(os.path.join(root_path, 'apps')))
    uvicorn.run(
        'strawberry_workshop.asgi:application',
        host='0.0.0.0',
        port=8000,
        lifespan='off',
        loop='asyncio',
        reload=True,
        timeout_graceful_shutdown=3,
    )
