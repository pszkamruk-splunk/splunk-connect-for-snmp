{{- define "splunk-connect-for-snmp.mongo_uri" -}}
{{- if eq .Values.mongodb.architecture "replicaset" }}
{{- printf "mongodb+srv://%s-mongodb-headless.%s.svc.%s/?tls=false&ssl=false&replicaSet=rs0" .Release.Name .Release.Namespace .Values.mongodb.clusterDomain}}
{{- else }}
{{- printf "mongodb://%s-mongodb:27017" .Release.Name }}
{{- end }}  
{{- end }}  

{{- define "splunk-connect-for-snmp.celery_url" -}}
{{- printf "redis://%s-redis-headless:6379/0" .Release.Name }}
{{- end }}

{{- define "splunk-connect-for-snmp.redis_url" -}}
{{- printf "redis://%s-redis-headless:6379/1" .Release.Name }}
{{- end }}

{{- define "splunk-connect-for-snmp.name" -}}
{{- default (printf "%s" .Chart.Name ) .Values.nameOverride | trunc 63 | trimSuffix "-" }}
{{- end }}

{{- define "splunk-connect-for-snmp.podSecurityContext" }}
{{- if .Values.podSecurityContext }}
{{ .Values.podSecurityContext }}
{{- else }}
podSecurityContext:
  fsGroup: 10001
{{- end }}
{{- end }}


{{- define "splunk-connect-for-snmp.securityContext" }}
{{- if .Values.securityContext }}
{{ .Values.securityContext }}
{{- else }}
    capabilities:
      drop:
        - ALL
    readOnlyRootFilesystem: true
    runAsNonRoot: true
    runAsUser: 10001
    runAsGroup: 10001
{{- end }}
{{- end }}

{{- define "splunk-connect-for-snmp.worker.podAntiAffinity" -}}
{{- if (.Values.worker.podAntiAffinity) }}
{{- default .Values.worker.podAntiAffinity }}
{{- else }}
{{- default "soft" }}
{{- end }}
{{- end }}