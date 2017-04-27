#!/usr/bin/env bash

ZBXGET="/usr/bin/zabbix_get"
if [ $# != 5 ]
then
    echo "Usage: $0 <JAVA_GATEWAY_HOST> <JAVA_GATEWAY_PORT> <JMX_SERVER> <JMX_PORT> <KEY>"
    exit;
fi

QUERY="{\"request\": \"java gateway jmx\",\"conn\": \"$3\",\"port\": $4,\"keys\": [\"$5\"]}"

$ZBXGET -s $1 -p $2 -k "$QUERY"