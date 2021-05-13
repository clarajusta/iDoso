#!/bin/bash

LOCAL_TOTAL=$(curl -s -H "Accept-Language: pt-br" wttr.in/?format="%l")
LOCAL="${LOCAL_TOTAL%%,*}"

TEMPERATURA=$(curl -s -H "Accept-Language: pt-br" wttr.in/$LOCAL?format="%t")

CLIMA=$(curl -s -H "Accept-Language: pt-br" wttr.in/$LOCAL?format="%C")

echo "No dia de hoje, o clima está $CLIMA, fazendo $TEMPERATURA agora em $LOCAL."