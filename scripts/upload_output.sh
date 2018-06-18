
mod=$1
outf=${2:-${outf}}

>&2 echo "uploading result in file: ${outf} to module: ${mod}"

casperjs scripts/upload_answer.js \
		 $mod \
		 $outf \
		 --u=${ROSALIND_USER} \
		 --p=${ROSALIND_API_KEY}
