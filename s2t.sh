
#!/bin/bash


#!/bin/bash

arecord out.wav -f S16_LE -r 16000 -d 4

if [ $# -lt 3 ]
then
	echo "$0: script de speech to text baseado na PI da Google. Modo de uso:"
	echo
	echo "   $0 NOME_DO_ARQUIVO TAXA_DE_AMOSTRAGEM IDIOMA"
	echo
	echo "   IDIOMA=1: conversão para o português brasileiro"
	echo "   IDIOMA=2: conversão para o inglês americano"
	echo
	exit
fi

KEY="AIzaSyBOti4mM-6x9WDnZIjIeyEU21OpBXqWBgw"
USERAGENT="Mozilla/5.0"
CLIENT="chromium"
URL="http://www.google.com/speech-api/v2/recognize"
PFILTER="0"

FILE=$1
RATE=$2
if [[ $FILE == *.wav ]]
then
	TYPE="l16"
elif [[ $FILE == *.flac ]]
then
	TYPE="x-flac"
fi

case ${3} in
	1) LANG="pt-BR";;
	2) LANG="en-US";;
esac
REQUEST="client=${CLIENT}&lang=${LANG}&key=${KEY}&pFilter=${PFILTER}" 
FULL_URL="${URL}?${REQUEST}"
curl "${FULL_URL}" \
	-A ${USERAGENT} \
	--data-binary "@${FILE}" \
	-H "Content-Type: audio/${TYPE}; rate=${RATE};" > stt.JSON


value=($(jq -r '.result' stt.JSON))

if [ "$value" == [] ]
then
	sed -i '1d' stt.JSON
fi

cat stt.JSON | jq '.result[0] .alternative[0] .transcript' > frase_ouvida.JSON

if [ -s frase_ouvida.JSON ]
then
	echo stt.JSON | grep -Po "(?<=transcript:).*(?=confidence)"
else
	echo "..." > frase_ouvida.JSON 	
fi
echo "Você disse: "
cat frase_ouvida.JSON