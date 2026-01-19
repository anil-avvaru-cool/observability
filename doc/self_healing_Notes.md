## Command to run Ansible playbook

```bash
ansible-playbook restart-webserver-playbook.yaml -i inventory.ini --ask-become-pass
 ansible-playbook restart-webserver-playbook-v2.yaml -e "target_host=node1" -e "service_name=apache2"  -i inventory.ini --ask-become-pass
```

## Auto heal trigger payload
```json
{
  "problemId": "{{ event()['display_id'] }}",
  "title": "{{ event()['event.name'] }}",
  "severity": "{{ event()['event.category'] }}",
  "hostName": "{{event()['host.name'][0] }}"
}

```

## Listener verification
```bash
curl -X POST http://127.0.0.1:5000/dynatrace -H "Content-Type: application/json" -d @data.json
```