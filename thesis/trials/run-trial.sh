#PBS –N thesis
#PBS –l procs=12
#PBS –l walltime=10:00:00
#PBS –j oe

#module load python/3


if [ "$PBS_ENVIRONMENT" != "PBS_INTERACTIVE" ] ; then
    cd $PBS_O_WORKDIR
fi

python3 $SCRIPT

#end of sample.job
