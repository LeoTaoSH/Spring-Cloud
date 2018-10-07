# Consul get started
- start Agent
consul agent -dev

- members
consul members
curl localhost:8500/v1/catalog/nodes

- define a service
sudo mkdir /etc/consul.d
echo '{"service": {"name": "web", "tags": ["rails"], "port": 80}}' \
    | sudo tee /etc/consul.d/web.json
consul agent -dev -config-dir=/etc/consul.d
dig @127.0.0.1 -p 8600 web.service.consul
dig @127.0.0.1 -p 8600 web.service.consul SRV
dig @127.0.0.1 -p 8600 rails.web.service.consul
curl http://localhost:8500/v1/catalog/service/web
curl 'http://localhost:8500/v1/health/service/web?passing'

- connect
socat -v tcp-l:8181,fork exec:"/bin/cat"
nc 127.0.0.1 8181
cat <<EOF | sudo tee /etc/consul.d/socat.json
{
  "service": {
    "name": "socat",
    "port": 8181,
    "connect": { "proxy": {} }
  }
}
EOF
consul connect proxy -service web -upstream socat:9191
nc 127.0.0.1 9191
cat <<EOF | sudo tee /etc/consul.d/web.json
{
  "service": {
    "name": "web",
    "port": 8080,
    "connect": {
      "proxy": {
        "config": {
          "upstreams": [{
             "destination_name": "socat",
             "local_bind_port": 9191
          }]
        }
      }
    }
  }
}
EOF
consul intention create -deny web socat
nc 127.0.0.1 9191

- Cluster
vagrant up
vagrant ssh n1
consul agent -server -bootstrap-expect=1 \
    -data-dir=/tmp/consul -node=agent-one -bind=172.20.20.10 \
    -enable-script-checks=true -config-dir=/etc/consul.d
vagrant ssh n2
consul agent -data-dir=/tmp/consul -node=agent-two \
    -bind=172.20.20.11 -enable-script-checks=true -config-dir=/etc/consul.d
vagrant ssh n1
consul members
dig @127.0.0.1 -p 8600 agent-two.node.consul

- health check
vagrant@n2:~$ echo '{"check": {"name": "ping",
  "args": ["ping", "-c1", "google.com"], "interval": "30s"}}' \
  >/etc/consul.d/ping.json
vagrant@n2:~$ echo '{"service": {"name": "web", "tags": ["rails"], "port": 80,
  "check": {"args": ["curl", "localhost"], "interval": "10s"}}}' \
  >/etc/consul.d/web.json
curl http://localhost:8500/v1/health/state/critical

- kv data
consul kv get redis/config/minconns
consul kv put redis/config/minconns 1
consul kv put redis/config/maxconns 25
consul kv put -flags=42 redis/config/users/admin abcd1234
consul kv get -detailed redis/config/minconns

- web UI
consul agent -ui
http://localhost:8500/ui