Zadání pro konfiguraci load balanceru
=====================================

Vytvořte program, který načte konfigurace služeb v yaml formátu a zapíše do
API. Každá služba je uvedena v samostatném souboru. API lze spustit
v přiloženém serveru pro Virtualbox. Program má chybějící služby vytvořit
(metoda POST `/v1/services` níže), rozdíly do API aktualizovat (metoda PUT
`/v1/services/:id`) a služby, které mají atribut `deleted` smazat (metoda
DELETE `/v1/services/:id`). Program lze spouštět opakovaně, vždy provede jen ty
nejnutnější úpravy (nedojde ke smazání služby či všech serverů, pokud to není
nutné).

API běží na adrese https://172.16.16.4/ a existující služby v něm lze zobrazit
přes https://172.16.16.4:8443/, přihlašovací jméno i heslo je "dev",
autentizace je metodou HTTP basic access authentication.

Služba je definována jménem, IP adresou a číslem TCP portu, typem služby (např.
http, https) a jaká síťová politika má být na službu aplikována (např.
allow-office, allow-all). Pro typ "https" musí být nastaveno jméno certifikátu,
pro ostatní typy se posílá nil. Jméno služby je unikátní, řetězec je bez mezer
z malých alfanumerických znaků a je povoleno podtržítko. Jméno musí začínat
písmenem a nesmí končit podtržítkem. IP adresa je IPv4 nebo IPv6 a kontrola
formátu není povinná, kontroluje jej server. API jménu služby při vytvoření
přiřadí unikátní ID.

Každá služba má seznam serverů, na které je provoz balancován. Server je
definován IP adresou a číslem portu, počtem chyb (`max_fails`), po kterých je
server na určitou dobu vyřazen (`fail_timeout`). Váha (`weight`) udává poměr
požadavků balancovaných mezi servery a `status` musí mít hodnotu "ENABLED".
Pokud není v definici uvedeno, jsou použity výchozí hodnoty: max_fails: 3,
fail_timeout: 3, weight: 1.

Pokud není nějaký konfigurační soubor ve správném formátu, chybí povinné
položky nebo se nepodaří zápis do API (není vrácen HTTP status kód 200 nebo
302), program musí být ukončen s chybou (návratový kód nesmí být 0).


Příklady:
---------

```yaml
name: admins2_spoluzaci_cz
ip: 77.66.55.44
port: 443
type: https
certificate_name: wildcard-spoluzaci.cz
network_policy: allow-all
servers:
- ip: 10.0.15.14
  port: 80
  weight: 2
  max_fails: 5
  fail_timeout: 2
- ip: 10.1.15.3
  port: 80
  weight: 3
- ip: 10.4.0.13
  port: 8080
```

```yaml
name: blog
ip: 192.168.0.201
port: 8080
type: http
network_policy: allow-office
servers:
- ip: 10.0.5.4
  port: 80
- ip: 10.10.0.3
  port: 80
```

```yaml
- name: the_test
  deleted: true
```


Popis API
---------

~~~
# route: GET /v1/services?filter[:param]
        params:
                :id, :name, :type, :ip, :port
        desc:
                list collection of services
        returns:
                json representation of a collection of services filtered by params

# route: POST /v1/services
        params:
                 :name, :type, :ip, :port, :certificate_name if template type is https, :network_policy
        desc:
                create a service
                :ip and :port combination must be unique
                :name is readonly, allowed format is [a-z][a-z0-9_]*
        return:
                redirect to created service

# route: GET /v1/services/:id
        params:
        desc:
                retrieve a service :id
        returns:
                json representation of a service

# route: PUT /v1/services/:id
        params:
                :type, :ip, :port, :certificate_name if template type is https, :network_policy
        desc:
                update a service :id
        returns:
                redirect to updated service: /v1/services/:id

# route: DELETE: /v1/services/:id
        params:
        desc:
                delete a service
        return:
                200 code and empty anwser of 500

# route: GET /v1/services/:id/servers
        params:
        desc:
                get backend servers of service :id
        returns:
                json representation of a collection of backend servers for service :id

# route: POST /v1/services/:id/servers
        params:
                :ip, :port
        desc:
                assign new backend server to a service :id
        return:
                redirect to created backend server

# route: GET /v1/servers?filter[:param]
        params:
                :ip, :port
        desc:
                list collection of backend servers
        returns:
                json representation of a collection of backend servers filtered by params

# route: PUT /v1/servers?filter[:param]
        params:
                :ip, :port
        desc:
                edit collection of backend servers
        returns:
                redirect to collection of updated servers

# route: GET /v1/servers/:id
        params:
        desc:
                get a backend server :id
        returns:
                json representation of a backend server

# route: PUT /v1/servers/:id
        params:
                :ip, :port
        desc:
                edit a backend server :id
        returns:
                redirect to updated server: /v1/servers/:id

# route: DELETE /v1/servers/:id
        params:
        desc:
                delete a backend server
        return:
                200 code and empty anwser of 500

# route: GET /v1/servers/:id/geoip
        params:
        desc:
                collection of country codes
                a server can recieve traffic from all countries (collection is empty)
                or from countries specified in this collection
        returns:
                json representation of a collection of geoip country codes

# route: POST /v1/servers/:id/geoip
        params:
                :code
        desc:
                add country code to a collection
        return:
                redirect to GET /v1/servers/:id/geoip

# route: DELETE /v1/servers/:id/geoip/:country_code
        params:
        desc:
        return:
                200 code and empty anwser of 500

~~~

### Příklad

```bash
$ cat a.json 
{
    "data": {
        "certificate_name": "zzz"
    }
}
$ curl --header "Content-Type: application/json" --header "Accept: application/json"  -XPUT --data @a.json -i -k -udev:dev  https://172.16.16.4/services/1
HTTP/1.1 302 Found
Server: nginx/1.10.3
Date: Tue, 23 Apr 2019 12:57:30 GMT
Content-Type: text/html
Content-Length: 0
Connection: keep-alive
Location: /services/1
```
