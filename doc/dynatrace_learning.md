
---

## 1. Core Dynatrace Architecture (Must-Know)

### OneAgent

* Automatic, code-level instrumentation
* Injects into:

  * OS processes
  * JVM / .NET / Node / PHP runtimes
* Collects:

  * Metrics, traces, logs (optional)
* Smart placement rules

### ActiveGate

* Secure gateway between Dynatrace and your environment
* Use cases:

  * Cloud API polling (AWS, Azure, GCP)
  * Synthetic execution (private)
  * Extension execution
* **Not a webhook relay** (common misconception)

---

## 2. Entity Model (Very Important)

Understand **how Dynatrace models reality**.

### Core entities

* Host
* Process
* Process Group
* Service
* Application
* Kubernetes entities (Node, Pod, Namespace)

### Entity relationships

* Host → Process → Service
* Service → Service (service flow)
* This relationship graph drives **Davis AI**

---

## 3. Smartscape & Topology

* Auto-discovered dependency graph
* Real-time topology
* Used for:

  * Root cause analysis
  * Blast radius analysis
  * Impact assessment

---

## 4. Davis AI (Critical Concept)

### What Davis does

* Baselines metrics automatically
* Detects anomalies (not static thresholds)
* Performs **causal root cause analysis**
* Groups symptoms into **single problem**

### Key ideas

* Causation > correlation
* Problem vs event
* Root cause entity selection

---

## 5. Problems, Events, and Alerts

### Problems

* Aggregated, AI-driven incidents
* One problem = many symptoms

### Events

* Deployments
* Configuration changes
* Annotations

### Alerting profiles

* Filter when notifications fire
* Severity, zones, tags

---

## 6. Metrics, Logs, and Traces (Three Pillars)

### Metrics

* Built-in + custom metrics
* Time-series
* DQL / Metrics v2

### Distributed Tracing

* End-to-end request visibility
* Service flow latency breakdown
* PurePath®

### Logs

* Log ingest vs log monitoring
* Log enrichment via context
* Cost control is critical

---

## 7. Service & Application Monitoring

### Services

* Automatically detected
* Request types, response time
* Failure rate, throughput

### Applications (RUM)

* User sessions
* Frontend performance
* User actions, errors

---

## 8. Process & Infrastructure Monitoring

### Process monitoring rules

* Availability checks
* Custom process detection
* Foundation for auto-healing

### Host monitoring

* CPU, memory, disk, network
* OS-level health

---

## 9. Kubernetes & Cloud-Native Concepts

### Kubernetes monitoring

* Pods, nodes, namespaces
* Workloads & services
* Cluster events

### Cloud integrations

* AWS, Azure, GCP
* Metrics pulled via ActiveGate
* Entity tagging critical

---

## 10. Tagging & Management Zones (Extremely Important)

### Tags

* Key-value metadata
* Drive:

  * Alert routing
  * Automation targeting
  * Cost allocation

### Management Zones

* Logical partitions
* RBAC boundaries
* Alert scoping

---

## 11. Automation & Self-Healing

### Workflows (New Platform)

* Event-driven automation
* HTTP actions
* Conditional logic

### Webhooks

* Outbound notifications
* Integration with:

  * Ansible
  * Lambda
  * ServiceNow
  * GitOps pipelines

### Guardrails

* Severity filters
* Cooldowns
* Approvals

---

## 12. APIs & Query Languages

### APIs

* Problems API
* Entities API
* Metrics API
* Events API

### Query languages

* **DQL** (Dynatrace Query Language)
* Metrics v2 selectors

---

## 13. Security & Compliance

### Application Security

* Vulnerability detection
* Runtime protection (RASP)

### Access control

* IAM / RBAC
* Token scopes

---

## 14. Cost & License Management

* Host units
* DEM units
* Log ingest costs
* Retention strategies

---

## 15. Operational Best Practices

* Avoid alert storms
* Prefer problems over metrics alerts
* Always tag early
* Automate with safety
* Use entity IDs in automation

---

## 16. Learning Priority (Recommended Order)

1. OneAgent & Entity Model
2. Smartscape & Davis AI
3. Problems & Alerting Profiles
4. Services & Tracing
5. Tagging & Management Zones
6. Workflows & Webhooks
7. APIs & DQL
8. Kubernetes / Cloud (if applicable)

---

## 17. If Your Goal Is…

| Goal         | Focus Areas                        |
| ------------ | ---------------------------------- |
| Operations   | Problems, Davis, Infra             |
| SRE          | Automation, Workflows, APIs        |
| Architect    | Entity model, Smartscape           |
| Dev          | Tracing, Services, RUM             |
| Auto-healing | Process rules, Workflows, Webhooks |

---
