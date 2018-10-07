vault server -dev
export VAULT_ADDR='http://127.0.0.1:8200'
also can get the root token from the output message of server startup

```
Usage: vault <command> [args]

Common commands:
    read        Read data and retrieves secrets
    write       Write data, configuration, and secrets
    delete      Delete secrets and configuration
    list        List data or secrets
    login       Authenticate locally
    server      Start a Vault server
    status      Print seal and HA status
    unwrap      Unwrap a wrapped secret

Other commands:
    audit          Interact with audit devices
    auth           Interact with auth methods
    lease          Interact with leases
    operator       Perform operator-specific tasks
    path-help      Retrieve API help for paths
    policy         Interact with policies
    secrets        Interact with secrets engines
    ssh            Initiate an SSH session
    token          Interact with tokens
```

- to install
vault -autocomplete-install

- check status
vault status

- write a new secret
vault kv put secret/hello foo=world
vault kv put secret/hello foo=world excited=yes

- get a secret
vault kv get secret/hello
vault kv get -format=json secret/hello | jq -r .data.data.excited
vault kv get -field=excited secret/hello

- delete a secret
vault kv delete secret/hello

- enable a secret engine
vault secrets enable -path=kv kv
vault secrets enable kv

- list secret
vault secrets list
vault write kv/my-secret value="s3c(eT"
vault write kv/hello target=world
vault write kv/airplane type=boeing class=787
vault list kv

- disable a secret engine
vault secrets disable kv/

- enable aws engine
vault secrets enable -path=aws aws

- Configure aws engine
vault write aws/config/root \
    access_key=AKIAI4SGLQPBX6CSENIQ \
    secret_key=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

- create a role
```
vault write aws/roles/my-role policy=-<<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "Stmt1426528957000",
      "Effect": "Allow",
      "Action": [
        "ec2:*"
      ],
      "Resource": [
        "*"
      ]
    }
  ]
}
EOF
```

- generating secret
vault read aws/creds/my-role

- revoke a secret
vault lease revoke aws/creds/my-role/0bce0782-32aa-25ec-f61d-c026ff22106






