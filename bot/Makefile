build:
	sudo docker build --no-cache  -t sample-bot .
run:
	sudo docker run -d -p 5005:5005 --restart always --name sample-bot  sample-bot 
remove:
	sudo docker rm -f sample-bot 
	sudo docker rm -f bmc-action-action-1
rebuild:
	sudo docker build --no-cache  -t sample-bot   .
	sudo docker rm -f sample-bot   || true
	sudo docker rm -f  sample-bot 	
	sudo docker run --restart always -p 5005:5005 -itd  --name sample-bot  sample-bot 
