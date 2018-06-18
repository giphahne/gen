
mod=$1

>&2 echo "fetching dataset for module: ${mod}"

dsfilename=$(casperjs scripts/fetch_dataset.js \
					  $mod \
					  --u=${ROSALIND_USER} \
					  --p=${ROSALIND_API_KEY}
		  )
mv $dsfilename data/
dsfullfile=$(realpath data/$dsfilename)

>&2 echo -e "got dataset: ${dsfullfile}\n"

#export dsf=$dsfullfile
echo "${mod} ${dsfullfile}"


