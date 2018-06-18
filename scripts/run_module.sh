

mod=$1
dsf=${2:-${dsf}}

#export outf=${dsf}_output
outf=${dsf}_output

>&2 echo "running module: ${mod}, using dataset: ${dsf}"

# redirect stdout from running our module:
python scripts/run_module.py --module $mod --dsfile $dsf --outfile $outf 1>&2

>&2 echo "done. output result to: ${outf}"

echo "${mod} ${outf}"

