# Nomad get started

- use vagrant
sudo nomad agent -dev
vagrant ssh
nomad node status
nomad server members

- jobs
nomad job init
nomad job run example.nomad
nomad status example
nomad alloc status 8ba85cef
nomad alloc logs 8ba85cef redis
nomad job plan example.nomad
nomad job run -check-index 7 example.nomad
nomad job run example.nomad
nomad job stop example

- clustering
```
# Increase log verbosity
log_level = "DEBUG"

# Setup data dir
data_dir = "/tmp/server1"

# Enable the server
server {
    enabled = true

    # Self-elect, should be 3 or 5 for production
    bootstrap_expect = 1
}
```
nomad agent -config server.hcl

```
# Increase log verbosity
log_level = "DEBUG"

# Setup data dir
data_dir = "/tmp/client1"

# Give the agent a unique name. Defaults to hostname
name = "client1"

# Enable the client
client {
    enabled = true

    # For demo assume we are talking to server1. For production,
    # this should be like "nomad.service.consul:4647" and a system
    # like Consul used for service discovery.
    servers = ["127.0.0.1:4647"]
}

# Modify our port to avoid a collision with server1
ports {
    http = 5656
}
```
sudo nomad agent -config client1.hcl

nomad job run example.nomad
nomad status example

- web UI 
http://localhost:4646
