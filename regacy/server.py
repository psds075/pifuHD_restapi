import uvicorn
import sys

port = 33001
debug = True
if(len(sys.argv) > 1):
    port = sys.argv[1]
if(len(sys.argv) > 2):
    if(sys.argv[2] == "False"):
        import logging
        debug = False 
        logging.basicConfig(filename='server.log',level=logging.DEBUG)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=port, reload=debug)
