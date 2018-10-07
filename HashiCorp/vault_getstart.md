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

- built-in help
vault path-help aws
vault path-help aws/creds/my-non-existent-role

- create/revoke/login valut token
vault token create
vault token revoke 463763ae-0c3b-ff77-e137-af668941465c
vault login a402d075-6d59-6129-1ac7-3718796d4346

- other auth methods
vault auth enable -path=github github
vault auth enable github
vault auth enable -path=my-github github
vault write auth/github/config organization=hashicorp
vault write auth/github/map/teams/my-team value=default,my-policy
vault auth list
vault auth help github
vault auth help aws
vault auth help userpass
vault auth help token
vault login -method=github
vault login <initial-root-token>
vault token revoke -mode path auth/github
vault auth disable github

- Policy

```
# Normal servers have version 1 of KV mounted by default, so will need these
# paths:
path "secret/*" {
  capabilities = ["create"]
}
path "secret/foo" {
  capabilities = ["read"]
}

# Dev servers have version 2 of KV mounted by default, so will need these
# paths:
path "secret/data/*" {
  capabilities = ["create"]
}
path "secret/data/foo" {
  capabilities = ["read"]
}
```

vault policy fmt my-policy.hcl
vault policy write my-policy my-policy.hcl
vault policy list
vault policy read my-policy
vault token create -policy=my-policy
vault login a4ebda12-23bf-5cf4-f80e-803ee2f37aab
vault kv put secret/bar robot=beepboop
vault kv put secret/foo robot=beepboop
vault write auth/github/map/teams/default value=my-policy

- Deploy valut
```
HCL file
storage "consul" {
  address = "127.0.0.1:8500"
  path    = "vault/"
}

listener "tcp" {
 address     = "127.0.0.1:8200"
 tls_disable = 1
}
```
consul agent -dev
vault server -config=config.hcl
vault operator init

- Vault API call
```
 curl \
    --request POST \
    --data '{"secret_shares": 1, "secret_threshold": 1}' \
    http://127.0.0.1:8200/v1/sys/init
```







