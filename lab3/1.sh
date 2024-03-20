docker stop my-server; docker rm my-server; # Opcjonalne czyszczenie
docker run --name my-server -p 80:80 -d nginx

sleep 3

docker exec -it my-server sh -c "echo '<!DOCTYPE html>
<html>
<head>
<title>Zmodyfikowana strona!</title>
<style>
html { color-scheme: light dark; }
body { width: 35em; margin: 0 auto;
font-family: Tahoma, Verdana, Arial, sans-serif; }
</style>
</head>
<body>
<h1>Witam na zmodyfikowanej stronie!!!</h1>
<p>If you see this page, the nginx web server is successfully installed and
working. Further configuration is required.</p>

<p>For online documentation and support please refer to
<a href="http://nginx.org/">nginx.org</a>.<br/>
Commercial support is available at
<a href="http://nginx.com/">nginx.com</a>.</p>

<p><em>Thank you for using nginx.</em></p>
</body>
</html>' > /usr/share/nginx/html/index.html"



