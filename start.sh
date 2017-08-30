docker run -e "MONGODB=172.18.0.11"  -v /root/tests:/apistar --net devnet -p 5000:5000 --ip 172.18.0.50 -it apistar
