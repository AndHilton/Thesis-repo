#PBS –N thesis
#PBS –l procs=10
#PBS –l walltime=10:00:00
#PBS –j oe

#module load python/3


python3 $SCRIPT

#end of sample.job